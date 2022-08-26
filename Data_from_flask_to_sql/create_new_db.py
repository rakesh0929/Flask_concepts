import mysql.connector as connection
# import test



try:
    mydb = connection.connect(host="localhost", database = 'task_ineuron',user="root", passwd="Rakesh@12345678",use_pure=True,port=3307)
    # check if the connection is established
    print(mydb.is_connected())
    test.add()

    query = "CREATE TABLE task (data1 INT(10) ,data2 INT(10), result = )"
    query1 = "INSERT INTO task VALUES ()"


    cursor = mydb.cursor() #create a cursor to execute queries
    cursor.execute(query)

    cursor = mydb.cursor() #create a cursor to execute queries
    cursor.execute(query1)

    print("Table Created!!")
    mydb.close()
except Exception as e:
    mydb.close()
    print(str(e))