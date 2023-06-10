import mysql.connector as bd
import json

with open('keys.json') as json_file:
    keys = json.load(json_file)

def convertirDatoBinario(filename):
    # Convert digital data to binary format
    try:
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData
    except:
        return 0

def escribirArchivo(data, path):
    # Convert binary data to proper format and write it on your computer
    with open(path, 'wb') as file:
        file.write(data)

def obtenerUsuarios():
    try:
        con = bd.connect(host=keys["host"], user=keys["user"], password=keys["password"], database=keys["database"])
        cursor = con.cursor()
        sql = "SELECT idUser, name FROM `user`"

        cursor.execute(sql)
        records = cursor.fetchall()

        usuarios = [(row[0], row[1]) for row in records]

        return usuarios
    except bd.Error as e:
        print(f"Error al obtener la lista de usuarios: {e}")
    finally:
        if con.is_connected():
            cursor.close()
            con.close()

