"""
Dada una cadena de caracteres como entrada, es necesario obtener el número de veces que aparece cada letra 
en la cadena. Decides almacenar los datos en un diccionario, con las letras como claves y los recuentos
correspondientes  como valores. Crea un programa que tome una cadena de caracteres como entrada
y genere un diccionario que represente el número de letras. 
 
Ejemplo de entrada 
hello 
 
Ejemplo de salida 
{'h': 1, 'e': 1, 'l': 2, 'o': 1}
"""

text = input() 
dict = {} 

for i in text :
    b=1
    if i in dict :
        dict [i] +=1
    else :
        dict[i] = b
print (dict )