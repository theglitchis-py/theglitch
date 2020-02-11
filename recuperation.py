import mysql.connector
def connexion_base():
    try:
        cnx = mysql.connector.connect(
            host="localhost",
            database='xxx',
            user="xxx",
            passwd="secret")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Password pas correct")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database no detect")
        else:
            print(err)

        # mytest.execute("SELECT PAYS FROM clients order by PAYS ")
        # mytest.execute("SELECT `NO_COMMANDE`, `SOCIETE`, `NO_EMPLOYE`, `DATE_COMMANDE`, `DATE_ENVOI`, PORT FROM `commandes`, `clients` WHERE `clients`.`CODE_CLIENT`=`commandes`.`CODE_CLIENT`; ")
    while True:
        mytest = cnx.cursor()
        mytest.execute("select level, name from gestionnaire;")
        result = mytest.fetchall()
        return result
