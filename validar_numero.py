"""Se te da un número de entrada, y necesitas comprobar si es un número 
de teléfono válido. 
Un número de teléfono válido tiene exactamente 8 dígitos y comienza 
con 1, 8 o 9.  
Genera "Valid" si el número es válido y "Invalid", si no lo es.  
  
Ejemplo de entrada 
81239870 
  
Ejemplo de salida 
Valid"""


import re
#tu código va aquí 


try:
    x=int(input())
    if  9999999 < x and x < 100000000:
        s= str(x)
        test1 = r"1"
        test8 = r"8"
        test9 = r"9"
        if re.match (test1, s):
            print("Valid")
        elif re.match (test8,s):
            print ("Valid")
        elif re.match (test9,s):
            print ("Valid")
        else :
            print ("Invalid")
    else:
        print ("Invalid")
except :
    print ("Invalid")

