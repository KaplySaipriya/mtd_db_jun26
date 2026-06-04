import db_connect2 as dbc


def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS priya_table (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        designation VARCHAR(255),
        salary INT
    )
    """

    try:
        connection = dbc.db_connect()

        if connection is None:
            return

        cursor = connection.cursor()

        cursor.execute(query)
        connection.commit()

        print("Table Created Successfully")

        cursor.close()
        dbc.db_disconnect(connection)

    except Exception as e:
        print("Error While Creating Table:", e)


# Function Call
create_table()