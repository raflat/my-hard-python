'''Introduzione a Python'''

#Print
print("Hello World!")
print("__________________________")
print("")
print("")

#Variabili
a = 5
print(a)

#Operatori
a += 10
print(a)

b = 13.0

c = a + b
print(c)

c = a * b
print(c)

c = a - b
print(c)

c = a / b
print(c)

c = a ** b
print(c)

#Tipi
print(type(a))
print(type(b))

b = "enkkone"
print(b)
print(type(b))
c = "Ms."
d = " Cappa"
e = c + d
print(e)

a = True
b = False
print(a)
print(b)
print(type(a))
print(type(b))

var_and = a and b
var_or = a or b
var_not = not b
print(var_and)
print(var_or)
print(var_not)

f = not(a and b)
print(f)
f = (a and b) or (a and b)
print(f)

f = 10
g = f == 10
print(g)

#Len
print(len(c))
print(len(d))
print(len(e))

#If
if a or b:
    print("ramo vero riga 1")
    print("ramo vero riga 1")

    if a:
        print("puzzi")
else:
    print("ramo falso riga 1")

#Input da tastiera
a = input("Dammi un dato: ")
print(a)

a = int(input("Dammi un numero: "))
print(a)

b = int(input("Dammi un altro numero: "))
print(b)

c = a ** b
print("risultato = " + str(c))
