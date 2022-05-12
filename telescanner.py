#-----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
                                            # # # TEL(ES)CANNER # # #
                                           # # # Demon Huntress # # #
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

#DESCRIPCIÓN
"""
Este programa extrae los posibles teléfonos de España que figuren previamente en comentarios de grupos de facebook,
scrapeados mediante la aplicacion APIFY "Facebook Latest Comments Scraper", por lo que este programa está condicionado
a su formato de salida (.json).

- Ejecuta este script e introduce en la consola el archivo JSON ej.: "miArchivo.json"
- Se generará un archivo ".txt" con todos los números. Guardado en la carpeta "/Output"

Los archivos generados por APIFY deben colocarse en el directorio "APIFY/JSON". Además, allí se encontrará un archivo
de prueba llamado "fblcs_test.json"
"""

import re
import json
import os
from pathlib import Path

regEx = "[+](34)[6-7][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]|" \
        "(34)[6-7][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]|" \
        "[6-7][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]|" \
 \
        "[+](34)\s[6-7][0-9][0-9]\s[0-9][0-9]\s[0-9][0-9]\s[0-9][0-9]|" \
        "[+](34)\s[6-7][0-9][0-9]\s[0-9][0-9]\s[0-9][0-9][0-9][0-9]|" \
        "[+](34)\s[6-7][0-9][0-9]\s[0-9][0-9][0-9][0-9][0-9][0-9]|" \
        "[+](34)\s[6-7][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]|" \
        "[+](34)\s[6-7][0-9][0-9]\s[0-9][0-9][0-9]\s[0-9][0-9][0-9]|" \
        "[+](34)\s[6-7][0-9][0-9][0-9][0-9][0-9]\s[0-9][0-9][0-9]|" \
        "[+](34)[6-7][0-9][0-9]\s[0-9][0-9]\s[0-9][0-9]\s[0-9][0-9]|" \
        "[+](34)[6-7][0-9][0-9][0-9][0-9]\s[0-9][0-9]\s[0-9][0-9]|" \
        "[+](34)[6-7][0-9][0-9]\s[0-9][0-9][0-9][0-9][0-9][0-9]|" \
        "[+](34)[6-7][0-9][0-9][0-9][0-9]\s[0-9][0-9][0-9][0-9]|" \
 \
        "(34)\s[6-7][0-9][0-9]\s[0-9][0-9]\s[0-9][0-9]\s[0-9][0-9]|" \
        "(34)\s[6-7][0-9][0-9]\s[0-9][0-9]\s[0-9][0-9][0-9][0-9]|" \
        "(34)\s[6-7][0-9][0-9]\s[0-9][0-9][0-9][0-9][0-9][0-9]|" \
        "(34)\s[6-7][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]|" \
        "(34)\s[6-7][0-9][0-9]\s[0-9][0-9][0-9]\s[0-9][0-9][0-9]|" \
        "(34)\s[6-7][0-9][0-9][0-9][0-9][0-9]\s[0-9][0-9][0-9]|" \
        "(34)[6-7][0-9][0-9]\s[0-9][0-9]\s[0-9][0-9]\s[0-9][0-9]|" \
        "(34)[6-7][0-9][0-9][0-9][0-9]\s[0-9][0-9]\s[0-9][0-9]|" \
        "(34)[6-7][0-9][0-9]\s[0-9][0-9][0-9][0-9][0-9][0-9]|" \
        "(34)[6-7][0-9][0-9][0-9][0-9]\s[0-9][0-9][0-9][0-9]|" \
 \
        "[6-7][0-9][0-9]\s[0-9][0-9]\s[0-9][0-9]\s[0-9][0-9]|" \
        "[6-7][0-9][0-9]\s[0-9][0-9]\s[0-9][0-9][0-9][0-9]|" \
        "[6-7][0-9][0-9]\s[0-9][0-9][0-9][0-9][0-9][0-9]|" \
        "[6-7][0-9][0-9][0-9][0-9]\s[0-9][0-9]\s[0-9][0-9]|" \
        "[6-7][0-9][0-9][0-9][0-9][0-9][0-9]\s[0-9][0-9]|" \
        "[6-7][0-9][0-9][0-9][0-9]\s[0-9][0-9][0-9][0-9]|" \
        "[6-7][0-9][0-9]\s[0-9][0-9][0-9]\s[0-9][0-9][0-9]|" \
        "[6-7][0-9][0-9][0-9][0-9][0-9]\s[0-9][0-9][0-9]|" \
        "[6-7][0-9][0-9]\s[0-9][0-9][0-9][0-9][0-9][0-9]"

# ----------------------------------------------------------------------------------------------------------------------

tlfCount = 0
tlfList = []
tlfMatch = ""
regExfind34 = "\A[+](34)|\A(34)|\s[+]34|\s34"

os.system('cls')

while True:

    print("##### TEL(es)CANNER #####")
    print("1) Presiona 1 para guardar números nuevos")
    print("2) Presiona 2 para salir")
    read = input()

    if read == "1":
        print("Introduce el nombre del archivo (ej.: file.json): ")

        datadir = Path("""./APIFY/FBLCS""")
        readJSON = datadir/str(input())
        # dataset_facebook-latest-comments-scraper_2022-04-24_13-47-51-325.json
        try:
            with open(readJSON, "r", encoding='utf8') as readFile:
                file = json.load(readFile)
            for element in file:
                for comment in element['comments']:
                    aux = str(comment['text'])
                    aux = aux.replace(" ", "")
                    tlfMatch = re.search(regEx, aux)

                    if tlfMatch:
                        tlfCount += 1
                        tlfList.append(tlfMatch.group(0))

            tlfList = ' '.join(tlfList)
            tlfList = re.sub(regExfind34, " ", tlfList)
            tlfList = tlfList.split(" ")

            if tlfList[0] == "":
                tlfList.remove("")

            exist = False
            nuevoNum = []
            if os.path.exists("Output/listaNumeros.txt"):
                with open("Output/listaNumeros.txt", "r") as fileTlf:
                    leer = fileTlf.read()
                    leer = list(leer.split("\n"))
                    leer.pop()

                for list in tlfList:
                    if not list in leer:
                        exist = True
                        nuevoNum.append(list)
                        with open("Output/listaNumeros.txt", "a") as fileTlf:
                            fileTlf.write(list + "\n")

                    if tlfList.index(list) + 1 == len(tlfList) and exist == False:
                        print("No se encontraron números nuevos")
                        tlfList = []
                        tlfCount = 0
                        os.system('pause')
                        os.system('cls')

                    if exist == True:
                        print("Números nuevos añadidos:")
                        for item in nuevoNum:
                            print(item, " ")
                        os.system('pause')
                        os.system('cls')
            else:
                with open("Output/listaNumeros.txt", "w") as fileTlf:
                    for linea in tlfList:
                        fileTlf.write(linea + "\n")

                if tlfCount >= 1:
                    print("Se han encontrado", tlfCount, "teléfonos:", tlfList)
                    tlfList = []
                    tlfCount = 0
                else:
                    print("No se han encontrado teléfonos")

                print("Archivo creado")
                os.system('pause')
                os.system('cls')

        except:
            print("El archivo no es válido o no existe")
            os.system('pause')
            os.system('cls')
            
    elif read == "2":
        os.system('cls')
        break

    else:
        print("Opción inválida")
        os.system('pause')
        os.system('cls')