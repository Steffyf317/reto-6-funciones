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