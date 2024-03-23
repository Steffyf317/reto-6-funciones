# reto 6: funciones
## 1. Dada la figura, hallar el área superficial y el volumen de la misma
### Con una función y valores preestablecidos
[![imagen1.png](https://i.postimg.cc/zGDk9SdM/imagen1.png)](https://postimg.cc/vcj9n9wL)
```python
import math

r1:int = 10 #radio de la esfera
r2:int = 5 #radio del cono
h: int = 7 #Altura del cono
a: float = (h**2+r2**2)**(0.5)

def calcular_area_y_volumen_figura (r1:int, r2:int, h: int) -> float:
  area_figura = 4*math.pi*r1**2 + math.pi*r2*(r2+a) #suma de las areas de la esfera y del cono
  volumen_figura = (4/3)*math.pi*r1**3 + (1/3)*math.pi*r2**2*h #Suma de los volúmenes de la esfera y el cono respectivamente
  return area_figura , volumen_figura

if __name__ == "__main__":
  area_y_volumen_calculado = calcular_area_y_volumen_figura (r1, r2, h)
  print("El área y el volumen de la figura es respectivamente " + str(area_y_volumen_calculado))
```

### Con dos funciones y valores ingresados por el teclado
```python
import math

def calcular_area_figura (r1:int, r2:int, h: int) -> float:
  area_figura = 4*math.pi*r1**2 + math.pi*r2*(r2+a) #suma de las areas de la esfera y del cono
  return area_figura

def calcular_volumen_figura(r1:int, r2:int, h: int) -> float:
  volumen_figura = (4/3)*math.pi*r1**3 + (1/3)*math.pi*r2**2*h #Suma de los volúmenes de la esfera y el cono respectivamente
  return volumen_figura

if __name__ == "__main__":
  r1:int = int(input("Ingrese el radio de la esfera "))
  r2:int = int(input("Ingrese el radio de la base del cono "))
  h: int = int(input("Ingrese la altura del cono "))
  a: float = (h**2+r2**2)**(0.5)
  area_calculada = calcular_area_figura (r1, r2, h)
  volumen_calculado = calcular_volumen_figura(r1, r2, h)
  print("El área de la figura es " + str(area_calculada) + " y el volumen es " +str(volumen_calculado))
```

## 2. Calcular el area y el perímetro de la figura
[![imagen2.png](https://i.postimg.cc/6qj1Pjr9/imagen2.png)](https://postimg.cc/2LWwbx9J)
### Con una función y valores preestablecidos
```python
import math

r:int = 2 #radio de los círculos
a:int = 5 #altura del rectángulo
b:int = 9 #base del rectángulo

def calcular_area_y_perimetro (r:int, a:int, b: int) -> float:
  area_figura = a*b + 2*(math.pi*r**2) #suma de las áreas
  perimetro_figura = 2*a+2*b + 2*(2*math.pi*r) #suma de los perimetros
  return perimetro_figura , area_figura
if __name__ == "__main__":
  area_y_perimetro_calculados = calcular_area_y_perimetro (r,a,b)
  print(area_y_perimetro_calculados)
```
### Con dos funciones y valores ingresados por el usuario
```python
import math

def calcular_area (r:int, a:int, b: int) -> float:
  area_figura = a*b + 2*(math.pi*r**2) #suma de las áreas
  return area_figura

def calcular_perimetro (r:int, a:int, b: int) -> float:
  perimetro_figura = 2*a+2*b + 2*(2*math.pi*r) #suma de los perimetros
  return perimetro_figura

if __name__ == "__main__":
  r:int = int(input("Ingrese el radio de los círculos ")) #radio de los círculos
  a:int = int(input("Ingrese la altura del rectángulo ")) #altura del rectángulo
  b:int = int(input("Ingrese la base del rectángulo ")) #base del rectángulo
  area_calculada = calcular_area(r,a,b)
  perimetro_calculado = calcular_perimetro(r,a,b)
  print("El perimetro de la figura es " +str(perimetro_calculado)+ " y el area es " +str(area_calculada))
```

## 3.Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.
```python
N:int = 50 #Cantidad de gallinas
M:int = 40 # Cantidad de gallos
K:int = 92 #Cantidad de pollitos
peso_gallinas: int = 6 #kilos
peso_gallos: int = 7 #kilos
peso_pollitos: int = 1 #kilo

def cantidad_carne_aves(N,M,K) -> int:
  kilos_carne = N*peso_gallinas + M*peso_gallos + K*peso_pollitos
  return kilos_carne

if __name__ == "__main__":
  kilos_aves_total = cantidad_carne_aves(N,M,K)
  print(kilos_aves_total)
```

## 4. Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.
```python
def calcular_precio_compra (P:int, M:int, H:int, B:int) -> int:
  precio_compra = P*300 + M*3300 +H*350
  if B == precio_compra:
    print("No sobra nada ni se debe nada de dinero")
    return(0)
  elif B < precio_compra:
    deuda = abs(B-precio_compra)
    print("La deuda es de " +str(deuda) " Pesos")
    return (deuda)
  else:
    vueltas = B-precio_compra
    print("Las vueltas son " +str(vueltas)+ " Pesos")
    return(vueltas)

if __name__ == "__main__":
  P = int(input("Ingrese la cantidad de panes comprados "))
  M = int(input("Ingrese el número de bolsas de leche compradas "))
  H = int(input("Ingrese la cantidad de huevos comprados "))
  B = int(input("Ingrese la cifra del billete "))
  deuda_o_vueltas = calcular_precio_compra(P,M,H,B)
```

## 5. Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.
```python
def calcular_valor_prestamo (C:int, i:float, n:int ) ->float:
  capital_a_pagar = C*((1+i))**n #Formula del interes compuesto
  return capital_a_pagar

if __name__ == "__main__":
  C = int(input("Ingrese el valor solicitado para préstamo ")) #Pesos
  i = float(input("Ingrese el valor decimal de la tasa de interés del préstamo "))
  n = int(input("Ingrese la cantidad de meses para pagar el préstamo "))
  capital_final = calcular_valor_prestamo(C,i,n)
  print("El valor del préstamo es de " +str(capital_final)+ " Pesos")
```

## 6. El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.
```python
def calcular_personas_contagiadas (D: int, C:int) -> int:
  total_contagiados = C*(2)**D #formula basada en el crecimiento poblacional de bacterias, solo que aqui no se tiene en cuenta el euler sino la duplicacion de individuos contagiados
  return total_contagiados

if __name__ == "__main__":
  C = int(input("Ingrese el número actual de contagiados "))
  D = int(input("Ingrese el número de días de contagio a partir de hoy "))
  personas_contagiadas = calcular_personas_contagiadas (D,C)
  print ("El número de personas contagiadas en " +str(D)+ " días es de " +str(personas_contagiadas))
```

## 7. Operaciones
```python
def calcular_mediana (n1: float, n2:float, n3:float, n4:float, n5:float) -> float:
  if n1 > n2:
    n1, n2 = n2, n1
    if n1 > n3:
        n1, n3 = n3, n1
    if n1 > n4:
        n1, n4 = n4, n1
    if n1 > n5:
        n1, n5 = n5, n1

  if n2 > n3:
    n2, n3 = n3, n2
    if n2 > n4:
        n2, n4 = n4, n2
    if n2 > n5:
        n2, n5 = n5, n2

  if n3 > n4:
    n3, n4 = n4, n3
    if n3 > n5:
        n3, n5 = n5, n3

  if n4 > n5:
    n4, n5 = n5, n4

  mediana = n3  
  return mediana 
  

def calcular_promedio (n1: float, n2:float, n3:float, n4:float, n5:float) -> float:
   prom = (n1+n2+n3+n4+n5)/5
   return prom

def cal_prom_multiplicativo (n1: float, n2:float, n3:float, n4:float, n5:float) -> float:
   prom_multiplicativo = (n1*n2*n3*n4*n5)**(0.5)
   return prom_multiplicativo

def orden_ascendente (n1: float, n2:float, n3:float, n4:float, n5:float) -> float:
  if n1 > n2:
    n1, n2 = n2, n1
    if n1 > n3:
        n1, n3 = n3, n1
    if n1 > n4:
        n1, n4 = n4, n1
    if n1 > n5:
        n1, n5 = n5, n1

  if n2 > n3:
    n2, n3 = n3, n2
    if n2 > n4:
        n2, n4 = n4, n2
    if n2 > n5:
        n2, n5 = n5, n2

  if n3 > n4:
    n3, n4 = n4, n3
    if n3 > n5:
        n3, n5 = n5, n3

  if n4 > n5:
    n4, n5 = n5, n4

  return n1,n2,n3,n4,n5 
  

def orden_descendente (n1: float, n2:float, n3:float, n4:float, n5:float) -> float:
  if n1 > n2:
    n1, n2 = n2, n1
    if n1 > n3:
        n1, n3 = n3, n1
    if n1 > n4:
        n1, n4 = n4, n1
    if n1 > n5:
        n1, n5 = n5, n1

  if n2 > n3:
    n2, n3 = n3, n2
    if n2 > n4:
        n2, n4 = n4, n2
    if n2 > n5:
        n2, n5 = n5, n2

  if n3 > n4:
    n3, n4 = n4, n3
    if n3 > n5:
        n3, n5 = n5, n3

  if n4 > n5:
    n4, n5 = n5, n4

  return n5,n4,n3,n2,n1

def potencia (n1: float, n2:float, n3:float, n4:float, n5:float) -> float:
  if n1 > n2:
    n1, n2 = n2, n1
    if n1 > n3:
        n1, n3 = n3, n1
    if n1 > n4:
        n1, n4 = n4, n1
    if n1 > n5:
        n1, n5 = n5, n1

  if n2 > n3:
    n2, n3 = n3, n2
    if n2 > n4:
        n2, n4 = n4, n2
    if n2 > n5:
        n2, n5 = n5, n2

  if n3 > n4:
    n3, n4 = n4, n3
    if n3 > n5:
        n3, n5 = n5, n3

  if n4 > n5:
    n4, n5 = n5, n4

  potencia_mayor_numero = n5**n1
  return potencia_mayor_numero

def calcular_raiz_cubica (n1: float, n2:float, n3:float, n4:float, n5:float) -> float:
  if n1 > n2:
    n1, n2 = n2, n1
    if n1 > n3:
        n1, n3 = n3, n1
    if n1 > n4:
        n1, n4 = n4, n1
    if n1 > n5:
        n1, n5 = n5, n1

  if n2 > n3:
    n2, n3 = n3, n2
    if n2 > n4:
        n2, n4 = n4, n2
    if n2 > n5:
        n2, n5 = n5, n2

  if n3 > n4:
    n3, n4 = n4, n3
    if n3 > n5:
        n3, n5 = n5, n3

  if n4 > n5:
    n4, n5 = n5, n4

  raiz_cubica = (n1)**(1/3)
  return raiz_cubica
```

## 8. Importar funciones
```python
import funciones 

if __name__ == "__main__":
  n1 = float(input("Ingrese el primer número "))
  n2 = float (input("Ingrese el segundo número "))
  n3 = float(input("Ingrese el tercer número "))
  n4 = float (input("Ingrese el cuarto número "))
  n5 = float(input("Ingrese el quinto número "))


  promedio = funciones.calcular_promedio (n1,n2,n3,n4,n5)

  mediana = funciones.calcular_mediana (n1,n2,n3,n4,n5)

  promedio_multiplicativo = funciones.cal_prom_multiplicativo (n1,n2,n3,n4,n5)

  orden_ascendente = funciones.orden_ascendente (n1,n2,n3,n4,n5)

  orden_descendente = funciones.orden_descendente (n1,n2,n3,n4,n5)

  potencia_mayor_numero = funciones.potencia (n1,n2,n3,n4,n5)

  raiz_c_menor_num = funciones.calcular_raiz_cubica (n1,n2,n3,n4,n5)


  print("El promedio es " +str(promedio))
  print("La mediana es " +str(mediana))
  print("El promedio multiplicativo es " +str(promedio_multiplicativo))
  print("El orden ascendente de los número es ", n1 , n2 , n3 , n4, n5)
  print("El orden descendente de los números es ", n5,n4,n3,n2,n1)
  print("La potencia del mayor número elevado al menor número es ", potencia_mayor_numero)
  print("La raiz cúbica del menor número es ", raiz_c_menor_num)
```

## 9. pip en python
"Pip es el sistema de gestión de paquetes que se utiliza para instalar y administrar las bibliotecas externas en Python. Con Pip, es fácil instalar y actualizar paquetes. El sistema de gestión se asegura de que todas las dependencias se instalan correctamente y siempre mantiene todo actualizado. Además, Pip tiene una gran cantidad de paquetes disponibles, por lo que siempre puede encontrar lo que necesita". (Consultado en https://apuntes.de/python/uso-de-pip-y-gestion-de-paquetes-en-python-administracion-de-dependencias/#gsc.tab=0)

## 10. Listado de módulos populares para python
·NumPy
·SciPy
·SymPy
·Matplotlib
·Scikit-learn

Estas se instalan con pip como se muestra en el ejemplo (para Windows):
```python
pip install Matplotlib
```
