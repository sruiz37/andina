largestNumber=9999999999999999945
number=int(input("Introduzca un numero o escriba -1 para detener: "))
while number != -1:
    if number > largestNumber:
        largestNumber=number
    number=int(input("Introduzca un numero o escriba -1 para detener: "))
print ("El numero mas grande es:", largestNumber)