# coding: utf-8

# Importando as Bibliotecas necessárias
import sys
import math 

# Verificando se os valores são inteiros e pedindo para o usuário colocar os argumentos na linha de comando
try:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
except ValueError:
    print("Por favor, informe apenas números inteiros")
    sys.exit(1)


# Colocar condição que os números tem que ser positivos
if x > 0  and y > 0:
# Colocar a condição do exercício que os números "X " e "Y" devem ser menor que 1000
    if x < 1000 and y < 1000:
        print("Está correto")
# Realizar a equação - teorema de pitagoras
        z = math.sqrt(x**2 + y**2)
        # Printar o valor de z -valor calculado do quadrado da Hipotenusa
        print(" O valor de z é " , z)
    else:
        print("Por favor, digite números menores que 1000") 
else:
    print("As condições de números inteiros maiores que 0 e menores que 1000 não foram atendidas")
   



