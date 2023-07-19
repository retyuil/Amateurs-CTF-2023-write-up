import os
import random
from Crypto.Util.strxor import strxor
from math import gcd

accepted = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789-{}[] _ ' , : ; \n . @ & ~ # | % $ ! ? + = * % * £ $ ^ / - & ° "


res = b""
with open('out.txt', 'r') as f:
    plaintext = f.read()
    plaintext = bytes.fromhex(plaintext)
    for l in range(79):
        cpt = 0
        maxi = 0
        resi = 0
        for i in range(256):
            j = 79
            clé = res
            clé += bytes([i])
            clé = bytes.fromhex(clé.hex() + (j-(l+1))*2*'0')
            clé = clé*60000
            chaine = (strxor(clé[0:len(plaintext)],plaintext))
            for k in range(len(plaintext)//100): 
                if chr(chaine[k*j + l]) in accepted:
                    cpt += 1
            if cpt > maxi:
                maxi = cpt
                resi = bytes([i])
                print("Max : ", maxi)
                #print("J : ", j)
            cpt = 0
        res += resi
        print("res", res)
    
print("Résultat : ", res)


with open('out.txt', 'r') as f:
    plaintext = f.read()
    plaintext = bytes.fromhex(plaintext)  
    print(len(plaintext))
    clé = res
    clé = clé*22000
    chaine = (strxor(clé[0:16336],plaintext[0:16336]))
    print(chaine.decode(errors = "ignore"))



