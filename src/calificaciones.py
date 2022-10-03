from math import *

respuestas_totales= int(input("Cuantos respuestas diste "))

aciertos = int(input("Cuantos respuestas son aciertos "))

errores = int(input("Cuantos errores tienes "))

   
nota_cuestionario = ((int(aciertos) * 10) / int(respuestas_totales)) - (( (int(errores)) * 10) / (50 - (int(respuestas_totales))))

print (respuestas_totales)
print (aciertos)
print (errores)

print(nota_cuestionario)

    
