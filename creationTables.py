import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
)

moncurseur = mydb.cursor()

moncurseur.execute("CREATE TABLE clients (code INT AUTO_INCREMENT, nom VARCHAR(255) NOT NULL, postnom VARCHAR(255) NOT NULL, prenom VARCHAR(255) NOT NULL, adresse VARCHAR(255) NOT NULL, num_telephone INT NOT NULL), PRIMARY KEY (code); CREATE TABLE comptes (code INT NOT NULL, solde VARCHAR(255) NOT NULL, client_code INT, type_compte VARCHAR(255), date_creation DATE() NOT NULL, PRIMARY KEY (code), FOREIGN KEY(client_code) REFERENCES clients(code)); CREATE TABLE operation (numero INT NOT NULL, type_operation VARCHAR(255), compte INT NOT NULL, date_operation DATE() NOT NULL, montant INT(255), PRIMARY KEY(numero), FOREIGN KEY(compte) REFERENCES comptes(code))")