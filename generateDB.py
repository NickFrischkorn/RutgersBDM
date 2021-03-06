#!/usr/bin/python3
import pymysql

# This file can be ran to generate the database
db = pymysql.connect("localhost","root","password")
cursor = db.cursor()

cursor.execute("CREATE DATABASE bdm;")
cursor.execute("USE bdm;")

cursor.execute("CREATE TABLE stock"
               "(ticker VARCHAR(10) NOT NULL, "
               "exchange VARCHAR(10) NOT NULL, "
               "PRIMARY KEY(ticker));")

cursor.execute("CREATE TABLE price"
               "(ticker VARCHAR(10) NOT NULL, "
               "date DATE NOT NULL, "
               "close FLOAT(5,2) NOT NULL, "
               "PRIMARY KEY(ticker, date));")

cursor.execute("CREATE TABLE buyNsell"
               "(ticker VARCHAR(10) NOT NULL, "
               "buy_or_sell VARBINARY(4) NOT NULL, "
               "date DATE NOT NULL, "
               "timestamp TIME NOT NULL, "
               "price FLOAT(5,2) NOT NULL, "
               "num_of_shares int(10) NOT NULL, "
               "PRIMARY KEY(ticker, date, timestamp));")

cursor.execute("INSERT INTO stock (ticker, exchange) VALUES"
               "('AAPL','NASDAQ'), "
               "('GOOG','NASDAQ'), "
               "('MSFT', 'NASDAQ'), "
               "('IBM','NYSE'), "
               "('TSLA', 'NYSE'), "
               "('AMZN', 'NYSE');")

cursor.execute("INSERT INTO price (ticker, date, close) VALUES"
               "('AAPL', '2020-03-25', 100.00),"
               "('AAPL', '2020-03-26', 101.50),"
               "('AAPL', '2020-03-22', 106.50),"
               "('GOOG', '2020-03-25', 100.00),"
               "('GOOG', '2020-03-26', 130.00),"
               "('GOOG', '2020-03-22', 110.00)," 
               "('MSFT', '2020-03-25', 184.50),"
               "('MSFT', '2020-03-26', 188.50),"
               "('MSFT', '2020-03-22', 210.00),"
               "('IBM', '2020-03-25', 72.00),"
               "('IBM', '2020-03-26', 70.00),"
               "('IBM', '2020-03-22', 10.00),"
               "('TSLA', '2020-03-25', 138.50),"
               "('TSLA', '2020-03-26', 138.00),"
               "('TSLA', '2020-03-22', 137.50),"
               "('AMZN', '2020-03-25', 103.00),"
               "('AMZN', '2020-03-26', 195.00),"
               "('AMZN', '2020-03-22', 200.00);")

cursor.execute("INSERT INTO buyNsell (ticker, buy_or_sell, date, timestamp, price, num_of_shares) VALUES"
               "('IBM', 'BUY', '2020-03-25', '11:55:00', 273.00, 1100),"
               "('IBM', 'BUY', '2020-03-26', '10:45:00', 271.00, 2400),"
               "('IBM', 'SELL', '2020-03-22', '12:09:00', 270.50, 2500),"
               "('GOOG', 'BUY', '2020-03-25', '12:22:00', 86.00, 2200),"
               "('GOOG', 'SELL', '2020-03-25', '14:00:00', 87.00, 1000),"
               "('GOOG', 'SELL', '2020-03-26', '10:22:00', 87.50, 1000),"
               "('GOOG', 'BUY', '2020-03-26', '13:28:00', 87.00, 800),"
               "('GOOG', 'SELL', '2020-03-22', '11:45:00', 86.00, 500),"
               "('AAPL', 'BUY', '2020-03-25', '10:01:00', 99.00, 1000),"
               "('AAPL', 'BUY', '2020-03-25', '11:22:00', 99.50, 1000),"
               "('AAPL', 'BUY', '2020-03-26', '14:22:00', 100.00, 1000),"
               "('AAPL', 'SELL', '2020-03-26', '14:29:00', 120.00, 9000),"
               "('AAPL', 'SELL', '2020-03-22', '14:42:00', 103.00, 3000),"
               "('MSFT', 'BUY', '2020-03-25', '11:45:00', 186.00, 1500),"
               "('MSFT', 'SELL', '2020-03-26', '10:45:00', 188.00, 1000),"
               "('MSFT', 'BUY', '2020-03-22', '12:03:00', 187.00, 5000),"
               "('MSFT', 'BUY', '2020-03-25', '11:48:00', 187.50, 3000),"
               "('MSFT', 'SELL', '2020-03-26', '12:15:00', 189.00, 200);")

db.close()
