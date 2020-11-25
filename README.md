# RSA Algorithm
 
The RSAtool is a python script I have written in order to practically demonstrate the weakness of bad RSA principles. All other scripts and online tools I have found could not handle very big digits, a problem I have solved by using gmpy2 library.

In the case here, p and q are prime numbers that do not have a big difference between them.

By providing a public key (modulus and the exponent), the script will allow you to decrypt a ciphertext associated with the key.

## Prerequisites
- Python 3
- gmpy2 [Documentation](https://gmpy2.readthedocs.io/en/latest/overview.html) [Source](https://pypi.org/project/gmpy2/) (has its own pre-requisites)