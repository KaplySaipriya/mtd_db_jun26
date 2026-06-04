import pymysql

def insert_row():
    query = """
    INSERT INTO priya_table(name, designation, salary)
    VALUES('Sai Priya', 'Developer', 50000)
    """

    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='priya@1208',
            database='airline_db',
            port=3306,
            charset='utf8'
        )

        cursor = connection.cursor()

        res = cursor.execute(query)
        connection.commit()

        if res == 1:
            print("Row inserted successfully")

        cursor.close()
        connection.close()

        print("DB DISCONNECTED")

    except Exception as e:
        print("Error:", e)

insert_row()