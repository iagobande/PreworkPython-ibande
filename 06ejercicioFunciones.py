'''
1. Ejercicio: Define una función que tome dos números y retorne su suma
'''
def suma(): 
    x = 5
    y = 3
    print(x + y)
suma()
'''
2. Ejercicio: Define una función que tome un número y retorne su factorial.
'''
numero = 3
def factorial(numero):
  if numero <= 0:
    print('El factorial de un número negativo no existe')
  elif numero == 0:
    return 1
  else:
    factorial = 1
    while numero > 1:
      factorial *=  numero
      numero -= 1
  return factorial
print('El factorial de', numero, 'es', factorial(numero))
'''
3. Ejercicio: Define una función que tome un número y determine si es primo.
'''