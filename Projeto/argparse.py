# Importando as Bibliotecas necessárias

from Bio import SeqIO
from Bio. Seq import Seq

sequencia = list(SeqIO.parse("covid.txt", 'fasta'))


# Para 3 nucleotídeos

# Sequências são declaradas como objeto por isso precisa do método "Seq". Não dá para ser usado como uma string sequencia = "ATGGGC"


cont = {}

# Loop para mostrar quais nucleotideos serão contados
for i in ['A', 'T', 'C', 'G']:
  for j in ['A', 'T', 'C', 'G']:
    for a in  ['A', 'T', 'C', 'G']:
      cont[i+j+a] = 0

# Loop para a contagem dos trinucleotídeos
sequencia=sequencia[0]
for k in range(len(sequencia)-2):
  cont[sequencia[k]+sequencia[k+1]+sequencia[k+2]] += 1

print(cont)