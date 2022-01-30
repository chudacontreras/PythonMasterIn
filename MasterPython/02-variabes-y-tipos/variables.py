"""

Una Variable es una contenedor de infromacion
que dentro guarda un dato, se pueden crear 
muchas variables y que cada una tenga un dato distinto

python es debilmente tipado.

"""
# crear variables y asignarles un valor 

texto = "Master en python"
texto2 = "con Chuda"
numero = 25
decimal = 3,9

# mostarr valor de las variables
print(texto)
print(texto2)
print(numero)
print(decimal)

print("---------------------------------------------")

# sustituir valor de algunas variables / resignar valores 
numero = 87
decimal = 7,8

print(numero)
print(decimal)
print("---------------------------------------------")

# concatenacion
nombre1 = "Jesus"
nombre2 = "Israel"
apellido1 = "Contereas"
apellido2  = "Urquiola"

print(nombre1 + " " + nombre2 + " " + apellido1 + " " + apellido2)
print(f"{nombre1} {nombre2} {apellido1} {apellido2}")
print("{} {} {} {}".format(nombre1, nombre2, apellido1, apellido2))
print(nombre1, nombre2, apellido1, apellido2)