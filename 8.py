
import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='viutilo1',
         autocommit=True
         )

maakoodi = input("Anna kaksikirjaiminen maakoodi")
sql = "SELECT name, continent FROM country WHERE iso_country =  '" + maakoodi + "'"
print(sql)
kursori = yhteys.cursor()
kursori.execute(sql)

tulos = kursori.fetchall()
for rivi in tulos:
    print(f"{rivi[0]}, {rivi[1]}")