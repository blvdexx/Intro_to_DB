import mysql.connector
try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = 'root',
        passwd = 'root'
        
    )
    cursor = mydb.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    mydb.commit()

    print(f"Database 'alx_book_store' created successfully!")
    mydb.close()


except mysql.connector.Error:
    print(f'Database creation failed!')

