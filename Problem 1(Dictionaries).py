P=input("Enter the protein sequence")
P=P.upper()
print(P)
S={"A": 71.07, "R":156.18, "N":114.08, "D":115.08, "C":103.10, "Q":128.13, "E":129.11, "G": 57.05, "H":137.14, "I":113.15, "L":113.15, "K":128.17, "M":131.19, "F":147.17, "P": 97.11, "S": 87.07, "T":101.10, "W":186.20, "Y":163.17, "V": 99.13}
m = 18.02
for i in P:
    m=m+S[i]
print("The molecular weight is",m)

    
    
