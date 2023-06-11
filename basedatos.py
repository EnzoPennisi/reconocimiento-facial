import mysql.connector as bd
import json

with open('keys.json') as json_file:
    keys = json.load(json_file)

def convertirDatoBinario(filename):
    try:
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData
    except:
        return 0

def escribirArchivo(data, path):
    with open(path, 'wb') as file:
        file.write(data)
        
def registrarUsuario(name, photo):
    id = 0
    inserted = 0

    try:
        con = bd.connect(host=keys["host"], user=keys["user"], password=keys["password"], database=keys["database"])
        cursor = con.cursor()
        sql = "INSERT INTO `user`(name, photo) VALUES (%s,%s)"
        pic = convertirDatoBinario(photo)

        if pic:
            cursor.execute(sql, (name, pic))
            con.commit()
            inserted = cursor.rowcount
            id = cursor.lastrowid
    except bd.Error as e:
        print(f"Failed inserting image: {e}")
    finally:
        if con.is_connected():
            cursor.close()
            con.close()
    return {"id": id, "affected":inserted}

def obtenerUsuario(name, path):
    id = 0
    rows = 0

    try:
        con = bd.connect(host=keys["host"], user=keys["user"], password=keys["password"], database=keys["database"])
        cursor = con.cursor()
        sql = "SELECT * FROM `user` WHERE name = %s"

        cursor.execute(sql, (name,))
        records = cursor.fetchall()

        for row in records:
            id = row[0]
            escribirArchivo(row[2], path)
        rows = len(records)
    except bd.Error as e:
        print(f"Failed to read image: {e}")
    finally:
        if con.is_connected():
            cursor.close()
            con.close()
    return {"id": id, "affected": rows}

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

def borrarUsuario(user_id):
    try:
        con = bd.connect(host=keys["host"], user=keys["user"], password=keys["password"], database=keys["database"])
        cursor = con.cursor()
        sql = "DELETE FROM `user` WHERE idUser = %s"

        cursor.execute(sql, (user_id,))
        con.commit()
    except bd.Error as e:
        print(f"Error al borrar el usuario: {e}")
    finally:
        if con.is_connected():
            cursor.close()
            con.close()
            
def actualizarNombreUsuario(user_id, new_name):
    try:
        con = bd.connect(host=keys["host"], user=keys["user"], password=keys["password"], database=keys["database"])
        cursor = con.cursor()
        sql = "UPDATE `user` SET name = %s WHERE idUser = %s"
        cursor.execute(sql, (new_name, user_id))
        con.commit()
    except bd.Error as e:
        print(f"Error updating user name: {e}")
    finally:
        if con.is_connected():
            cursor.close()
            con.close()