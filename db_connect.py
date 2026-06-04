import pymysql
connection =pymysql.connect(user='root',password='priya@1208',port=3306,database='airline_db',charset='utf8',host='localhost')
print('DB CONNNECTED')
connection.close()
print('DB DISCONNNECTED')
