#!/usr/bin/python3
import pymysql

# This file is ran to double check answers without having to individually enter each query into the web application.

# Open connection to the database
db = pymysql.connect("localhost", "root", "password", "bdm")
# Start a cursor object using cursor() method
cursor = db.cursor()

# find the tickers and all closing prices of all stocks exchanged in 2020
q1 = cursor.execute("SELECT DISTINCT bs.ticker, p.close FROM buyNsell bs, price p WHERE bs.ticker = p.ticker && bs.date BETWEEN '2019-12-31' AND '2021-01-01';")
print("Question 1: ", cursor.fetchall())

# Find all tickers (i.e. for all dates) whose closing price is both higher
# than ‘IBM’ on ‘3/25/2020’ and no higher than ‘GOOG’ on ‘3/25/2020’.
q2 = cursor.execute("SELECT DISTINCT pb.ticker FROM  price p, price pa, price pb WHERE ((p.ticker = 'GOOG' && p.date = '2020-3-25') && (pa.ticker = 'IBM' && pa.date = '2020-3-25') && (pb.ticker != 'IBM' && pb.ticker != 'GOOG' && pb.date = '2020-3-25') && (pb.close <= p.close && pb.close > pa.close));")
print("Question 2: ", cursor.fetchall())

# Find the tickers of all stocks that closed at the highest price on ‘3/25/2020’.
# (we are asking for “all stocks” since there may be more than one with the same “highest price”)
q3 = cursor.execute("SELECT DISTINCT p.ticker FROM price p WHERE p.ticker NOT IN (SELECT DISTINCT pa.ticker FROM price p, price pa WHERE p.date = '2020-3-25' && pa.date = '2020-3-25' && pa.close < p.close);")
print("Question 3: ", cursor.fetchall())

# Find the tickers of all stocks in ‘NYSE’ whose closing price on ‘3/25/2020’ was
# either strictly below $20 or strictly above $100
q4 = cursor.execute("SELECT DISTINCT p.ticker FROM price p WHERE p.date = '2020-3-25' && (p.close<20 OR p.close>100) && p.ticker IN (SELECT DISTINCT s.ticker FROM stock s WHERE (s.exchange = 'NYSE'));")
print("Question 4: ", cursor.fetchall())

# Find all tickers in ‘NYSE’ of the stocks whose closing price showed the
# highest increase between ‘3/25/2020’ and ‘3/26/2020’ in ‘NYSE’ and
# whose closing price was (in ‘NYSE’) strictly above $100 for the entire 2020
q5 = cursor.execute("SELECT DISTINCT s.ticker FROM stock s WHERE s.ticker NOT IN "
                    "(SELECT DISTINCT r.ticker FROM price p, price q, price r, price s WHERE p.date = '2020-3-25' "
                    "&& q.date = '2020-3-26' && p.ticker = q.ticker && r.date = '2020-3-25' && s.date = '2020-3-26' &&  "
                    "r.ticker = s.ticker &&  p.ticker != r.ticker && q.close-p.close>s.close-r.close) && s.ticker NOT IN "
                    "(SELECT DISTINCT p.ticker FROM price p WHERE p.date BETWEEN '2019-12-31' AND '2021-01-01' && p.close<=100) "
                    "&& s.ticker IN (SELECT DISTINCT s.ticker FROM stock s WHERE s.exchange = 'NYSE');")
print("Question 5: ", cursor.fetchall())

# In addition, to the above queries, also do in SQL the following one:
# Find the dates where the total price (i.e. price times num of shares)
# of ‘AAPL’ the ﬁrm (i.e. the trading ﬁrm which is using this database) sold
# was higher than what the ﬁrm bought in ‘NASDAQ’
q6 = cursor.execute("SELECT DISTINCT buy.date FROM (SELECT b.date, SUM(b.price * b.num_of_shares) AS summed FROM buyNsell b, stock s WHERE s.ticker = b.ticker AND s.exchange = 'NASDAQ' AND b.buy_or_sell = 'BUY' GROUP BY b.date) AS buy, (SELECT b.date, SUM(b.price * b.num_of_shares) AS summed FROM buyNsell b WHERE b.buy_or_sell = 'SELL' AND b.ticker = 'AAPL' GROUP BY b.date) AS sell WHERE buy.date = sell.date AND sell.summed > buy.summed;")
print("Question 6:", cursor.fetchall())

db.close()