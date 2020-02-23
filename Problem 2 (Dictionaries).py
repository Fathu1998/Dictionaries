s=input("Enter the DNA sequence")
s=s.upper()
print(s)
codon_table = {'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',
'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
'UAC':'Y', 'UAU':'Y', 'UAA':'_', 'UAG':'_',
'UGC':'C', 'UGU':'C', 'UGA':'_', 'UGG':'W'}
RNA=""
Protein=""
for i in s:
    if i=="T":
        RNA=RNA+"U"
    else:
        RNA=RNA+i
for i in range(0,len(RNA),3):
    Protein+=codon_table[RNA[i:i+3]]
print ("The translated protein sequence is", Protein)        
