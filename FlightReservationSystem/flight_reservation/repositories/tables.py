import mysql.connector
import pandas as pd
from sqlalchemy import create_engine


#establish a connection to the MySQL database
connection = mysql.connector.connect(
    host = "localhost",
    user="admin",
    password="admin",
    database="flight"
)

# Create a cursoor object for executing SQL queries
mycursor = connection.cursor()

# Drop existing tables if they exist(to start fresh)
tables = ['FlightReservation', 'Flight', 'Account_Role', 'Role', 'Account', 'Airport', 'Airline', 'Address']
for table in tables:
    mycursor.execute(f"SET FOREIGN_KEY_CHECKS = 0;")  # Disable foreign key checks
    mycursor.execute(f"DROP TABLE IF EXISTS {table};")
    mycursor.execute(f"SET FOREIGN_KEY_CHECKS = 1;")  # Re-enable foreign key checks

#create address table
mycursor.execute("""
CREATE TABLE Address (
    address_id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(255),
    state VARCHAR(255),
    country VARCHAR(255)       
)
""")
# Create airline table
mycursor.execute("""
CREATE TABLE Airline (
    code VARCHAR(10) PRIMARY KEY,
    name VARCHAR(255)
)
""")

# Create airport table
mycursor.execute("""
CREATE TABLE Airport (
    code VARCHAR(10) PRIMARY KEY,
    name VARCHAR(255),
    address_id INT,
    FOREIGN KEY (address_id) REFERENCES Address(address_id)
)
""")
# Create role table
mycursor.execute("""
CREATE TABLE Role (
    role_id INT AUTO_INCREMENT PRIMARY KEY,
    role_name VARCHAR(255)
)
""")
# Create account table
mycursor.execute("""
CREATE TABLE Account (
    account_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE,
    password VARCHAR(255),
    status VARCHAR(255)
)
""")
# Create Account_Role table for many-to-many relationship between Account and Role
mycursor.execute("""
CREATE TABLE Account_Role (
    account_id INT,
    role_id INT,
    PRIMARY KEY (account_id, role_id),
    FOREIGN KEY (account_id) REFERENCES Account(account_id),
    FOREIGN KEY (role_id) REFERENCES Role(role_id)
)
""")

# Create flight table
mycursor.execute("""
CREATE TABLE Flight (
    flight_no INT AUTO_INCREMENT PRIMARY KEY,
    airline_code VARCHAR(10),
    distance_km DECIMAL(10, 2),
    dep_time DATETIME,
    arri_time DATETIME,
    dep_port VARCHAR(10),
    arri_port VARCHAR(10),
    booked_seats INT DEFAULT 0,
    FOREIGN KEY (airline_code) REFERENCES Airline(code),
    FOREIGN KEY (dep_port) REFERENCES Airport(code),
    FOREIGN KEY (arri_port) REFERENCES Airport(code)
)
""")

# Create FlightReservation table
mycursor.execute("""
CREATE TABLE FlightReservation (
    reservation_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    flight_no INT,
    account_id INT,
    seats INT,
    creation_date DATETIME,
    payment_amount DECIMAL (10, 2),
    FOREIGN KEY (flight_no) REFERENCES Flight(flight_no),
    FOREIGN KEY (user_id) REFERENCES Account(account_id)
)
""")

# Commit the changes to the database
connection.commit()
# Close the cursor and connection
mycursor.close()
connection.close()

print("Tables created successfully.")

