from flask import Flask , render_template , request , redirect, url_for 
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '1234567890',
    'database': 'online_vote_db',
    'port': '3306',
}

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = '1234567890'
# app.config['MYSQL_DB'] = 'online_vote_db'

@app.route("/")
def homepage():
    return render_template('homepage.html')

@app.route('/login', methods=['GET','POST'])
def logIn():
    
    # Check if it's a POST request
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        # Connect to the database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Use parameterized query to prevent SQL injection
        query = "SELECT user_name, password FROM user WHERE user_name = %s AND password = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchall()

        cursor.close()
        connection.close()

        if user:
            # If user exists, redirect to the vote page
            return redirect(url_for('votepage'))
        else:
            # If the username or password is incorrect, render the login template with an error message
            return render_template('login.html', error="Invalid username or password")

    # If it's a GET request, render the login template
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # Check if it's a POST request
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Check if the passwords match
        if password != confirm_password:
            return render_template('signup.html', error='Passwords do not match')

        # Hash the password before storing it in the database
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        # Connect to the database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Use parameterized query to prevent SQL injection
        query = "INSERT INTO user (user_name, email, password) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, email, hashed_password))

        # Commit the changes to the database
        connection.commit()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Redirect to the login page after successful signup
        return redirect(url_for('login'))

    # If it's a GET request, render the signup template
    return render_template('signup.html')

@app.route('/votepage')
def votepage():
    
    # OPEN CONNECTION
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    # SEND : SQL 
    cursor.execute("SELECT * FROM CANDIDATE ")
    # GET DATA
    data = cursor.fetchall()    
    print(data)
    # CLOSE CONNECTION
    cursor.close()
    connection.close()
    return render_template('votepage.html', data = data)

@app.route('/scorepage', methods=["GET"])
def scorepage():
    id = request.args.get("id")
     # OPEN CONNECTION
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    # SEND : SQL 
    cursor.execute(f"UPDATE CANDIDATE SET vote = vote + 1 WHERE  id = {id}")
    connection.commit()
    cursor.close()
    connection.close()
    return render_template('scorepage.html')

@app.route('/resultpage', methods=["GET"])
def resultpage():
     # OPEN CONNECTION
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM CANDIDATE ORDER BY vote desc")
    data = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    return render_template('resultpage.html', data=data)

if __name__ == '__main__':
    app.run(port=5000,debug=True)
   
 
