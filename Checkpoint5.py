# Ejercicio 1

words = ["Rubens", "Ballester", "Lillo"]

for word in words:
    print(word)


# Ejercicio 2
    
def suma(a, b, c):
    return a + b + c
print(suma(1, 2, 3))

# Ejercicio 3

suma = lambda a, b, c: a + b + c
print(suma(1, 2, 3))

# Ejercicio 4

nombre = "Enrique"

lista_nombre = ["Jessica", "Paul", "George", "Henry", "Adán"]

for i in lista_nombre:
    if nombre == i:
        print(f"El nombre {nombre} coincide con un nombre de la lista")
        break
else:
    print(f"El nombre {nombre} no está en la lista") 
        
         
