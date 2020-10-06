# Importar Biblioteca necessária
import sys

# Argumentos da Linha de comando
sequencia_dna  = sys.argv[1]

# Verificando se não há números na sequência de DNA
print(sequencia_dna.isalpha())


# Não permitir que o usuário continue o programa se ele não colocar uma sequência
if sequencia_dna.isalpha() == False:
    exit()

# Verificar se está de acordo com o que o exercicio pediu
try:
    n1 = int(sys.argv[2])
    n2 = int(sys.argv[3])
    n3 = int(sys.argv[4])
    n4 = int(sys.argv[5])
except ValueError:
    print("Por favor insira valores inteiros")
    sys.exit(1)

# Criando uma variável para evitar que chame a função len o tempo todo
tamanho_sequencia = len(sequencia_dna)

# Verificar se os nuúmeros inseridos são menores que a sequência de DNA
if n1 > tamanho_sequencia:
    print("O valor de n1 é maior que o tamanho da sequencia de Dna, por favor, insira um valor menor")
    exit()
elif n2 > tamanho_sequencia:
    print("O valor de n2 é maior que o tamanho da sequencia de Dna, por favor, insira um valor menor")
    exit()
elif n3 > tamanho_sequencia:
    print("O valor de n3 é maior que o tamanho da sequencia de Dna, por favor, insira um valor menor")
    exit()
elif n4 > tamanho_sequencia:
    print("O valor de n4 é maior que o tamanho da sequencia de Dna, por favor, insira um valor menor")
    exit()
else:
    print("Os valores foram inseridas de forma correta")


# Variavel que armazenam os testes dos intens 3 e 4
v3 = False
v4 = False

# Extrair a sequência CDS1
  
CDS1 = sequencia_dna[n1-1: n2]
print(CDS1)

# Conferir se inicia com ATG

if CDS1[0:3] in "ATG":
    print("O códon é de inicio")
    v3 = True
else:
    print("O Códon não é de início")


# Extrair a sequência CDS2

CDS2 = sequencia_dna[n3-1:n4]
print(CDS2)


# Conferir se termina com um dos códons de parada " TAA","TAG" e "TGA"
if CDS2[-3:] in ['TAA', 'TAG', 'TGA']:
     print("O códon é de parada")
     v4 = True
else:
    print("O Códon não é de parada")


# Caso os intens 3 e 4 sejam verdadeiros, concatenar a sequência
if v3 and v4:
    seq_concatenada = CDS1 + CDS2
    print("Sequencia concatenada", (seq_concatenada))
else:
    print("Como os critérios não foram atendidas a sequência não foi concatenada")


