ventas = [120, 80, 200, 150, 90, 300, 50]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

dia_alto=0
dia_bajo=0
dia_normal=0

for i in range (len(ventas)):
    venta=ventas[i]
    dia=dias[i]
    #print(i)

#for i in ventas :
    if venta>=200:
        dia_alto+=1
        print(dia, ":", venta, "- venta alta")


    elif venta>100 and venta<200:
            dia_normal+=1
            print(dia, ":", venta, "- venta normal")


    else:
        dia_bajo+=1
        print (dia, ":", venta, "- venta baja")

print("venta baja", dia_bajo)
print("venta normal", dia_normal)
print("venta alta", dia_alto)
