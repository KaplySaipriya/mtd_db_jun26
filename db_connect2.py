import pymysql

def db_connect():
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='priya@1208',
            database='airline_db',
            port=3306,
            charset='utf8'
        )
        print("DB CONNECTED")
        return connection

    except Exception as e:
        print("DB Connection Failed:", e)
        return None


def db_disconnect(connection):
    try:
        connection.close()
        print("DB DISCONNECTED")
    except Exception as e:
        print("DB Disconnect Failed:", e)
    


