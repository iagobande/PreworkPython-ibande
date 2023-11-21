'''
1.1 Dado el siguiente diccionario, cambia el valor de la clave edad a 25.
    persona = {'nombre': 'Juan', 'edad': 10}
'''
persona = {"nombre": "Juan", "edad": 10}
persona['edad'] = 30
print(persona['edad'])
'''
1.2 Declara una variable "precio" y asignarle el valor 25. Luego, crea una variable "impuesto" y asignale el valor de "precio" multiplicado por 0.21
    Muestra ambos valores por consola de esta forma:
    El precio es 25 y el impuesto es 5.25
'''
precio = 25
impuesto = (precio * 0.21)
print('El precio es',precio, 'y el impuesto es',impuesto)
'''
1.3 Dado el siguiente diccionario, imprime con un print el valor de la clave "apellido".
    persona = {'nombre': "Juan", 'apellido': "Pérez"}
'''
persona = {'nombre': "Juan", 'apellido': "Pérez"}
print(persona['apellido'])
'''
1.4 Crea un diccionario llamado "producto" que tenga las claves "nombre", "precio" y "cantidad".
Asigna valores a estas claves y luego muestra el diccionario completo por consola
'''
producto = {
    'nombre': 'Porras',
    'Precio': 3.50,
    'Cantidad': 3
    }
print(producto)
