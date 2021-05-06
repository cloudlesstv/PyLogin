import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    database="mydatabase"
)

mycursor = mydb.cursor()


def main():
    print("")
    print("")
    print("Was möchtest du tun?")
    print("(R)egistrieren / (L)öschen / (A)nmelden / (B)eenden")
    action = input("Aktion: ")
    print("")
    print("")
    if action == "R":
        register()
    elif action == "L":
        delete()
    elif action == "A":
        login()
    elif action == "B":
        exit("Intended")


def register():
    print("")
    print("")
    username = input("Name: ")
    password = input("Passwort: ")

    sql1 = "SELECT* FROM login WHERE username = '{}'  AND password = '{}';".format(username, password)
    mycursor.execute(sql1)

    result = mycursor.fetchall()
    if not str(result) == "[('" + username + "', '" + password + "')]":
        sql = "INSERT INTO login (username, password) VALUES (%s, %s)"
        val = (username, password)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Account wurde erstellt.")
        main()
    else:
        print("Du bist bereits registriert.")
        main()
    print("")
    print("")


def delete():
    print("")
    print("")
    username = input("Name: ")
    password = input("Passwort: ")

    sql = "SELECT* FROM login WHERE username = '{}'  AND password = '{}';".format(username, password)

    mycursor.execute(sql)

    result = mycursor.fetchall()
    if not str(result) == "[]":
        sql = "DELETE FROM login WHERE username = '{}'".format(username)
        mycursor.execute(sql)
        mydb.commit()
        print("Account wurde entfernt.")
    else:
        print("Dieser Account existiert nicht.")
        main()
    print("")
    print("")
    main()


def login():
    print("")
    print("")
    username = input("Name: ")
    password = input("Passwort: ")

    sql = "SELECT* FROM login WHERE username = '{}'  AND password = '{}';".format(username, password)

    mycursor.execute(sql)

    result = mycursor.fetchall()
    if not str(result) == "[]":
        print("Hallo,", username)
        main()
    else:
        print("Dieser Account existiert nicht.")
        main()
    print("")
    print("")


main()
