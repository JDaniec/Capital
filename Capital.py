print("-------------------Capital compuesto-----------------")
print("-----------------------------------------------------")
print("-----------------------------------------------------")

C = int(input("Ingrese el valor del capital: "))
n = 0
D = 2*C

while ( C<= D):
    C = C + C*(5/100)
    n = n + 1
    print("Mes" + str(n))
    print(str(C))
    
print("Los meses son " +str(n))

