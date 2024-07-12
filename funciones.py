def sueldos_trabajadores(sueldos) :
  import random 
  for sueldo in range(10) : 
        sueldo = random.randint(300000,2500000)
        sueldos.append(sueldo)
    
def sueldos_detector(sueldos) : 
    for i in sueldos : 
        if i > 0   : 
            print(f"Los sueldos menores a 800000 son : {sueldos}")
        elif i > 800000 and sueldos < 250000 :
            print(f"Los sueldos entre 8000000 y 2500000 son :{sueldos}")
        elif i > 2500000 : 
            print(f"Los sueldos mayores a 2500000 son :{sueldos}")

def sueldo_estadistica(sueldos) : 
    sueldo_mas_b =  min(sueldos)
    print(f"El sueldo mas bajo  es : {sueldo_mas_b}")

    sueldo_mas_alto = max(sueldos)
    print(f"El sueldo mas alto es : {sueldo_mas_alto}")

    sueldos_suma = 0
    for i in sueldos :
        sueldos_suma += i
    
    promedio = sueldos_suma/10

    print(f"El promedio de los sueldos es : {promedio}")

def sueldos_reporte(sueldos) : 

    for i in sueldos :  
        descuento_salud = i * 0.07
        descuento_afp = i * 0.12
        total_descuento = descuento_salud + descuento_afp
        sueldo_liquido = i - total_descuento

        print(f"El suelo {i} tiene desceunto por afp : {descuento_afp}, por salud : {descuento_salud} y su liquido es {sueldo_liquido}")