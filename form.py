#!/usr/bin/python3
print("Content-Type: text/html")
print()

import pymysql
import cgi
import cgitb
cgitb.enable()
form = cgi.FieldStorage()
db = pymysql.connect("localhost","root","password","bdm")
cursor = db.cursor()
query = form.getvalue('fname')
cursor.execute(query)

rows = cursor.fetchall()
desc = cursor.description

for y in desc:
        print(y[0])

print("<table>")
print("\n")
for row in rows:
        print("<tr>")
        print("<td>", row ,"</td>")
        print("</tr>")
print("</table>")

db.close()




