#!/usr/bin/env python
import gmpy2

"""
N = RSA modulus
e = public key exponent
y = plaintext cipher
"""
N = 66034789842315311047168748281598639181887663942254337252417649233287630627173387890882607005899538301776265566983968235336137472316898569968136071381556832587083683991708018685765677316014182488675669044474767295709083915164817097485581784476177726861133178662159329481050362025564548720913803947875743719831
e = 65537
y = 57860681627503455594962235338592437164500156842758217546336370028825389545142630465572220714725494652040846943379079541654591864361250259043508312286936844168995154183859237197189825252496503122764283284571060075704978901559923841532332738106087150559801706554355149553136195255064853865618530709371410125270

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
 
    return message

"""
To double check our decrypted message, we can encrypt it back and compare it to y
"""
def encryptRSA(m):
    cipher = gmpy2.powmod(m, e, N)
    return cipher
 
if __name__ == "__main__":
    (p, q) = fermat_factor(N)
 
    print("p = {}".format(p))
    print("q = {}".format(q))
 
    (m) = decryptRSA(p, q)
 
    print("m = {}".format(m))
 
    (c) = encryptRSA(m)
 
    print("c = {}".format(c))

    if(c == y):
        print("The encrypted message matches the ciphertext!")
    else:
        print("There is a mismatch between your encrypted text and the original ciphertext!")