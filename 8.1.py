import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='viutilo1',
         autocommit=True
         )

SyötäICAO = input("Anna ICAO")
sql = "SELECT name, municipality FROM airport WHERE ident = '" + SyötäICAO + "'"

print(sql)
kursori = yhteys.cursor()
kursori.execute(sql)

tulos = kursori.fetchall()
for rivi in tulos:
    print(f"{rivi[0]}, {rivi[1]}")