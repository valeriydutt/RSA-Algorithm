#!/usr/bin/env python
import gmpy2
import time

"""
N = RSA modulus
e = public key exponent
y = plaintext cipher
"""
try:
   input = raw_input
except NameError:
   pass
try:
   chr = unichr
except NameError:
   pass
N=int(input('Enter modulus N: '))
e=int(input('Enter exponent e: '))
y=int(input('Enter cipher y: '))

"""
Fermat's Factorization Method applies such that
k = a^2-b^2 = (a+b)(a-b) where (a+b) and (a-b) are factors of k
"""
def fermat_factor(n):
    assert n % 2 != 0
 
    a = gmpy2.isqrt(n)
    b2 = gmpy2.square(a) - n
 
    while not gmpy2.is_square(b2):
        a += 1
        b2 = gmpy2.square(a) - n
 
    p = a + gmpy2.isqrt(b2)
    q = a - gmpy2.isqrt(b2)
 
    return int(p), int(q)

"""
Knowing e, p and q, we can decipher y
"""
def decryptRSA(p, q):
    phi = (p-1)*(q-1)
    d = gmpy2.invert(e,phi)
    message = gmpy2.powmod(y, d, N)
 
    return int(message)

"""
To double check our decrypted message, we can encrypt it back and compare it to y
"""
def encryptRSA(m):
    cipher = gmpy2.powmod(m, e, N)
    return int(cipher)
 
if __name__ == "__main__":
    start_time = time.clock()
    (p, q) = fermat_factor(N)
 
    print("--------------------------------------------------------------------")
    print("p = {}".format(p))
    print("q = {}".format(q))
    print("--------------------------------------------------------------------")
    (m) = decryptRSA(p, q)
 
    print("decrypted message = {}".format(m))
 
    (c) = encryptRSA(m)
    print("====================================================================")
    print("re-encrypted message = {}".format(c))
    print("====================================================================")
    if(c == y):
        print("The re-encrypted message matches the ciphertext! We have successfully decrypted y in ", time.clock() - start_time, "seconds!")
    else:
        print("There is a mismatch between your encrypted text and the original ciphertext!")