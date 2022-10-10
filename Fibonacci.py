"""
La secuencia de Fibonacci es una de las fórmulas más famosas de las matemáticas. 
Cada número de la secuencia es la suma de los dos números que la preceden. 
Por ejemplo, aquí está la secuencia de Fibonacci para 10 números, empezando por 0: 0,1,1,2,3,5,8,13,21,34. 
  
Escribe un programa para tomar el número positivo N (la variable num en la plantilla de código) 
como entrada, calcula recursivamente y saca los primeros números N de la secuencia de Fibonacci 
(empezando por 0). 
  
Ejemplo de entrada 
6 
  
Ejemplo de salida 
0 
1 
1 
2 
3 
8


"""

num = int(input()) 
 
 
def fibonacci(n): 
 #completa la función recursiva 
    a=1
    b=1
    if n==1:
        print('0')
    elif n==2:
        print('0','1')
    else:
        print('0')
        print(a)
        print(b)
        for i in range(n-3):
            total = a + b
            b=a
            a= total
            print(total)
         
 
fibonacci(num)
