-- CREATE DATABASE : online_vote_db
CREATE SCHEMA `online_vote_db` DEFAULT CHARACTER SET utf8 ;

-- CREATE TABLE : CANDIDATE
CREATE TABLE `online_vote_db`.`candidate` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(200) NULL,
  `description` VARCHAR(1000) NULL,
  `vote` INT UNSIGNED NULL,
  PRIMARY KEY (`id`));

-- create user table
CREATE TABLE `online_vote_db`.`user` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(200) NOT NULL,
  `password` VARCHAR(100) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`user_id`));


-- insert
INSERT INTO users (id, username, password, email) VALUES
(1, 'SilverFox42', 'LunaStar@87', 'silverfox42@example.com'),
(2, 'ElectricWave56', 'Neptune123!', 'electricwave56@example.com'),
(3, 'CosmicExplorer77', 'GalaxyPass@44', 'cosmicexplorer77@example.com'),
(4, 'QuantumJumper21', 'SolarFlare&12', 'quantumjumper21@example.com'),
(5, 'StardustWanderer', 'Celestial#98', 'stardustwanderer@example.com'),
(6, 'LunarVoyager39', 'Astro1234!', 'lunarvoyager39@example.com'),
(7, 'NebulaSeeker84', 'CometFire$56', 'nebulaseeker84@example.com'),
(8, 'OrionNavigator', 'SpaceTime*23', 'orionnavigator@example.com'),
(9, 'GravitySurfer67', 'SkyWatcher!31', 'gravitysurfer67@example.com'),
(10, 'SolarSailor55', 'Eclipse&78', 'solarsailor55@example.com');
