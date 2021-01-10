# RSA Algorithm
 
The RSAtool is a python script I have written in order to practically demonstrate the weakness of bad RSA principles. All other scripts and online tools I have found could not handle very large numbers, a problem I have solved by using gmpy2 library.

In the case here, p and q are prime numbers such that | p - q | < 10,000.

By providing a public key (modulus and the exponent), the script will allow you to decrypt a ciphertext associated with the key.

The average execution time I had when testing it on my xubuntu VM, was 0.00065 seconds.

The output format of the script:
```
--------------------------------------------------------------------
p = 
q = 
--------------------------------------------------------------------
decrypted message = 
====================================================================
re-encrypted message = 
====================================================================
(whether or not the re-encrypted message matches the original ciphertext)!
```

## Prerequisites
- Python 3
- gmpy2 [Documentation](https://gmpy2.readthedocs.io/en/latest/overview.html) [Source](https://pypi.org/project/gmpy2/) (has its own pre-requisites)