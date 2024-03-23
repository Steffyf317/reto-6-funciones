#Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:

  
  
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