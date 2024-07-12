import csv
from funciones import sueldos_trabajadores,sueldos_detector,sueldo_estadistica,sueldos_reporte

trabajadores = ["Juan Pérez” ,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]

sueldos = []

while True : 
    opcion = int(input("Eliga una opcion :"))

    if opcion == 1 :
        sueldos_trabajadores(sueldos)
    if opcion == 2 :
        sueldos_detector(sueldos)
    if opcion == 3 : 
        sueldo_estadistica(sueldos)
    if opcion == 4 : 
        sueldos_reporte(sueldos)
    if opcion == 5 : 
        print("Usted a salido del programa : ")
        print("Desarrolado por Gabriel Duran")
        print("RUT : 21.764.994-9")

        with open('archivo.csv','a',newline='') as archivo_csv :
            cabecillas = ["Sueldos"]

            escritor_csv = csv.DictWriter(archivo_csv, fieldname=cabecillas)

            

