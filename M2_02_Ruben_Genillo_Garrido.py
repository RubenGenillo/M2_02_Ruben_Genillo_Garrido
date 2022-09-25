#Creo 5 variables con 5 notas numéricas
nota1 = 5
nota2 = 9
nota3 = 2
nota4 = 7
nota5 = 2

#Hago la media aritmética
print("La nota media es ", (nota1+nota2+nota3+nota4+nota5)/5) #La nota media es  5.0

#Redondeo el resultado de (365 / 12) * 14.7 a tan solo 2 decimales
print("{:.2f}".format((365 / 12) * 14.7)) #447.12


#Creo dos variables username y password que almacenaran dos strings
username = "Ruben"
password = "Osaka"

#Compruebo que username sea mayor o igual que tres y menor que diez
print("Username:", str(len(username)>= 3 and len(username)<10)) #Username: True

#Compruebo que password sea igual a "Tokio" o que sea igual a "Python"
print("Password:", str(password == ("Tokio" or "Python"))) #Password: False

#Creo dos variables y le asigno el número que quiero
num1 = 35
num2 = 273

#Incremento el valor de num1 en 1
num1 += 1
print(num1) #36

#Decremento el valor de num2 en 2
num2 -= 2
print(num2) #271

#Multiplico num1 por 3 y actualizo su valor
num1 *= 3
print(num1) #108

#Dividido num2 entre 2 y actualizo su valor
num2 /= 2
print(num2) #135.5