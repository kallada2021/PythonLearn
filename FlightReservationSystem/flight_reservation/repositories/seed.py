# Import necessary libraries and connectors
import mysql.connector
import pandas as pd
from sqlalchemy import create_engine

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host = "localhost",
    user = "admin",
    password = "admin",
    database = "flight"
)

# create a cursor object to perform queries
# mycursor = connection.cursor()

# # Create a Dataframe with the data
# df = pd.read_csv('../dataset/airlines.csv')

# # Create a SQL Alchemy engine to connect to the MySQL database
# engine = create_engine("mysql+mysqlconnector://admin:admin@localhost/flight")

# # Convert the Pandas DataFrame to a format for MySQL table insertion
# df.to_sql('Airline', con=engine, if_exists="append", index=False)

# connection.commit()

# # print(mycursor.rowcount, "record inserted.")
# # mycursor.execute("Select * from Airline")

################################################################################################################

# Load the dataframe from the CSV file
# df = pd.read_csv('../dataset/airports.csv')

# create a cursor object to perform queries
mycursor = connection.cursor()

# Function to insert into the Address table and get address_id
# def insert_address(city, state, country):
#     mycursor.execute("""
#         INSERT INTO Address(city, state, country)
#         VALUES(%s, %s, %s)
#          """, (city, state, country))
#     connection.commit() # Saving changes
#     return mycursor.lastrowid  # Get the last inserted address_id

# # Iterate over each row in the dataframe
# for index, row in df.iterrows():
#     # Extract city, state, country
#     city = row['city']
#     state = row['state']
#     country = row['country']

#     # Insert into Address and get address_id
#     address_id = insert_address(city, state, country)

#     # Insert into Airport using the code, name, and address_id
#     mycursor.execute("""
#         INSERT INTO Airport (code, name, address_id)
#         VALUES (%s, %s, %s)
#     """, (row['code'], row['name'], address_id))

#     connection.commit() # Saving changes

# print(mycursor.rowcount, "record inserted.")
# mycursor.execute("Select * from Airline")

################################################################################################################

flights_df = pd.read_csv('../dataset/flights.csv')
# print(flights_df.columns)

mycursor = connection.cursor()

# Prepare an SQL query to insert data into the Flight table
# flight_no

insert_flight_query = """
    INSERT INTO Flight (airline_code, distance_km, dep_time, arri_time, dep_port, arri_port, booked_seats)
    VALUES(%s, %s, %s, %s, %s, %s, 0 )
"""

# select only the relevant columds
relevant_columns = ['airline_code', 'distance_km', 'dep_time', 'arri_time', 'dep_port', 'arri_port']

# Convert the selected columns to tuples (rows of data)
flight_data = [tuple(row) for row in flights_df[relevant_columns].values]

# Execute the insert query for each row of flight data
batch_size = 1000 

for i in range(0, len(flight_data), batch_size):
    batch = flight_data[i:i+batch_size]
    mycursor.executemany(insert_flight_query, batch)
    connection.commit()

print(f"{len(flight_data)} flights inserted into the database.")
