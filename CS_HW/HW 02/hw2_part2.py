# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 12:59:26 2021

@author: Oscar
"""

sentence = input("Enter a string to encode ==> ")
print (sentence + "\n")
#input sentence
def encrypt(encnum, one, two):
    return encnum.replace(one, two)
#replace one part of the sentence with another
encrypt0 = encrypt(sentence, ' a', '%4%')
encrypt1 = encrypt(encrypt0, 'he', '7!')
encrypt2 = encrypt(encrypt1, 'e' , '9(*9(')
encrypt3 = encrypt(encrypt2, 'y' , '*%$')
encrypt4 = encrypt(encrypt3, 'u' , '@@@')
encrypt5 = encrypt(encrypt4, 'an' , '-?')
encrypt6 = encrypt(encrypt5, 'th' , '!@+3')
encrypt7 = encrypt(encrypt6, 'o' , '7654')
encrypt8 = encrypt(encrypt7, '9' , '2')
encrypt9 = encrypt(encrypt8, 'ck' , '%4')
#encrypting sentence is this order
diff = len(encrypt9) - len(sentence)
#difference if the length of each sentence
def decrypt (decnum, one, two):
    return decnum.replace(one, two)
#replace encrypted with decryted strings
deci0 = decrypt(encrypt9, '%4' , 'ck')
deci1 = decrypt(deci0,'2' , '9')
deci2 = decrypt(deci1,'7654' , 'o')
deci3 = decrypt(deci2,'!@+3' , 'th')
deci4 = decrypt(deci3,'-?' , 'an')
deci5 = decrypt(deci4,'@@@' , 'u')
deci6 = decrypt(deci5,'*%$' , 'y')
deci7 = decrypt(deci6,'9(*9(' , 'e')
deci8 = decrypt(deci7,'7!', 'he')
deci9 = decrypt(deci8,'%4%', ' a')
#decrypting in this order

print ("Encrypted as ==> " + encrypt9)
print ("Difference in length ==>", diff)
print ("Deciphered as ==>", deci9)

if (deci9 == sentence):
    print ("Operation is reversible on the string.")
else:
    print ("Operation is not reversible on the string.")
