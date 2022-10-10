"""
Se te da una clase Zumo, que tiene las propiedades nombre y capacidad. 
Necesitas completar el código para permitir la adición de dos objetos
Zumo, resultando en un nuevo objeto Zumo con la combinación de
capacidad nombres de los dos zumos que han sido añadidos. 
  
Por ejemplo, si añades un zumo de naranja con capacidad 1.0
y un zumo de manzana con capacidad 2.5 capacity, el zumo resultante
debería tener: 
nombre: Orange&Apple 
capacidad: 3.5 
  
Los nombres se han combinado usando un símbolo & .
"""

class Juice: 
    def __init__(self, name, capacity): 
        self.name = name 
        self.capacity = capacity 
    def __add__(self, other):
        return Juice (self.name+"&"+other.name, self.capacity + other.capacity) 
    def __str__(self): 
        return (self.name + ' ('+str(self.capacity)+'L)') 
 
 
a = Juice('Orange', 1.5) 
b = Juice('Apple', 2.0) 
 
result=a+b 
print(result)
