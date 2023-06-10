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

