def binarioADecimal():
    num=input('Escriba su numero BINARIO: ')
    long=len(num)
    decimal=0

    for x in range(long):
        num1=int(num[long - 1 - x])
        decimal +=  (2*(num1))**(x) 

    print("El decimal es:", decimal)


def decimalABinario():
    num=int(input('Escriba su numero DECIMAL: '))
    numBinario=''

    while num > 0:
            numBinario = str(num % 2) + numBinario
            num = num // 2
    
    print("El binario es:", numBinario)

opt=int(input('1 para decimal a binario y 2 para binario a decimal... '))
if opt == 1:
    decimalABinario()
elif opt == 2:
    binarioADecimal()
else:
    print('Opcion invalida intente de nuevo')