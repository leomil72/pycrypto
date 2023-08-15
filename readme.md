# p y C R Y P T O

**pyCrypto** is an encryption/decryption/hashing app written in Python 3 that
relies via pySide6 on the Qt framework to design the GUI.

pyCrypto uses the *cryptography* package which provides cryptographic primitives
to Python apps. *Cryptography*, in turn, relies on the OpenSSL library for all of
cryptographic operations.

## Usage of the program
When launched, the app show a single window app with 2 tabs: the first one
allows access to encryption and decryption of a file while the second one allows
the user to calculate the hash of a file or text.

### Encryption/Decryption
Firstly, choose a file by clicking of the "Open file" icon. Then, select a cipher,
the size of the key and the mode of operation of the selected cipher. Not all the
options ara available for all the ciphers.

Secondly, select the operation to perfom, encryptio or decryption, and then run
the app. pyCrypto will encrypt/decrypt the selected file and will create an
encrypted/decrypted file: when encrypting, it will create a new file with the same
nale of the original file with the ".enc" suffix; when decrypting, it will decrypt
an ".enc"rypted file and will create a new file with the ".dec" suffix.

### Hashing
An *hash*, or cryptographic hash function, is a particular algorithm that, given
a selected text or piece of data, returns a "digest", or checksum, normally
expressed as a hexadecimal string. The security of a hash algorithm lies in the 
fact that different data must always give a different result. Checksums are used
not only to check the correctness of data (MD5 strings used to check whether files
downloaded from the internet have not arrived corrupted are famous) but also to 
store, for example, passwords on unsecured mass storages.

Select a file, or enter a text, choose the preferred hash algorithm, and run the
app.

## Cipher algorithms
Among the cryptographic algorithms offered by the *cryptography* package, the
following symmetric key algorithms were selected. "Symmetric key" refers to an
algorithm where decryption is done with the same key used for data encryption.

The selected algorithms are: AES, CAST5, Camellia and ChaCha20.

### AES
AES, which stands for Advanced Encryption Standard, is a cryptographic standard
created by the U.S. National Security Agency (NSA) to replace the old DES. It 
has been adopted as a cryptographic algorithm for cataloging top secret documents.
The implementation used in pyCrypto uses 128-bit blocks with 128/192/256-bit keys
and OFB and CBC modes of operation

### CAST5
CAST5 is a block cipher approved for use in the Canadian government. The lenght
of its key my vary from 40 to 128 bits. The implementation in pyCrypto uses
128-bit keys. The block size is set to 128 bits.

### Camellia
Camellia is a block cipher approved for use by the European NESSIE project and the
japanese CRYPTREC project. It is considered to have comparable security and performance
to AES but is not as widely used. Camellia uses blocks of 128 bits and key sizes 
of 128, 192 and 256 bits. The cipher was named for the flower Camellia japonica, 
because the cipher was developed in Japan.

### ChaCha20
ChaCha20 is a symmetric algorithm that derives by Salsa20: the latter was developed
in 2005 to be submitted as a candidate to the eSTREAM European Union cryptographic
project. ChaCha20 is a modification of Salsa20 which has a new internat structure
that increases both security and performance of the algorithm. Since the implementation
of ChaCha20 supported by 'cryptography' is not standard compliant, some restrictions
have been introduced: ChaCha20 can only be used with 256-bits keys. Since ChaCha20 
is a stream algorithm, there is no need to select an mode of operation as in the 
case of other algorithms, that are block ciphers.

## Mode of operations
Wikipedia says: "A block cipher by itself is only suitable for the secure cryptographic 
transformation (encryption or decryption) of one fixed-length group of bits called 
a block. A mode of operation describes how to repeatedly apply a cipher's single-block 
operation to securely transform amounts of data larger than a block." 

This means that a block cipher algorithm can operate on only one block of data
at a time: the way to operate on a larger volume of data is established precisely
by the chosen mode of operation, that is, by how the algorithm flows the blocks 
of data and how it binds them to each other. Some ways are safer than others: for
example, CTR mode, which stands for "Counter", is not considered cryptographically
secure. Instead, CBC mode, which stands for "Cipher Block Chaining", is, which 
is why it was implemented in pyCrypto. The other mode implemented, the OFB, which 
stands for "Output Feedback", is also considered cryptographically secure. In 
addition, the OFB transforms a block cipher into a stream cipher for which input 
data padding is not required.

Padding is the operation of inserting *n* additional bytes so that the block of
data to be processed has the same size of the block of data that can handle the
cipher. For example, if a block of data to be passed to AES is only 80-bits large,
we must add 48 extra bits because the block of data that AES can process must be
128-bits wide. With stream ciphers, and with block ciphers used with a mode of 
operation that transforms them into the former, this necessity lapses.

## Hash algorithms
### BLAKE2b
This hash algorithm was developed to replace the older, but broken, MD5 and SHA1
algorithms. Since not full RFC-compliant due to OpenSSL limitations, BLAKE2b
doesn't accept keying, personalization and salting features. BLAKE2b is optimized
for 64-bits systems and it's set to return a 64-byte message digest.

### SHA-2
SHA-2 (Secure Hash Algorithm) is a set of hash algorithms developed by U.S.
NSA to replace the older SHA-1, that has not been considered secure due to its
limited hash lenght. SHA-2 comes in three variants, depending on the lenght of
the message digest that is returned: 256, 384, and 512 bits.

### MD5
MD5, that stands for Message Digest 5, is an hash algorithm developed by Ron Rivest
in the '90s of the XX century. It was quickly replaced by other algorithms because
it was soon discovered that it suffered from several structural weaknesses. From 
then on its use was deprecated and today it is only used as a checksum for the 
verification, for example, of data downloaded from the Internet.

## Security
The security of a cryptographic algorithm lies in the secrecy and robustness of
the password used to encrypt the data. The more robust the password, i.e., long
and consisting of many characters, the more difficult the data is to retrieve.
It is also important not to spread over insecure channels, for any reason, the
password used. pyCrypto relies on the cryptography package, which, in turn, 
relies on OpenSSL. Cryptographic algorithms are considered secure, with a few 
exceptions that will be shown below.

### Clarification
The software is a "proof of concept" and should therefore not be used where real,
certified data security is required. In these cases, the use of a cryptographically
secure algorithm, certified by the appropriate Agencies of your country, is recommended.

## Usage
To run the app, open a terminal in the directory where the .py files reside and
write the following command:

> python pycrypto.py

### Dependencies
To run the app first you need to install the following Python dependencies with
'pip':

> pip install cryptography

> pip install pyside6

### Qt Creator
The app was developed using Qt Creator 11 under Manjaro Linux. Qt Creator is free
for open source users.

## License
This software is released under the terms of the GNU General Public License v3.0
or later. It is allowed to derive works from this software but they must be
released under the same license. Please always quote the original author of the
software.

## Warranty
The software is provided "AS IS" without any warranty, either expressed or implied,
including, but not limited to, the implied warranties of merchantability and fitness
for a particular purpose. The author will not be liable for any special, incidental,
consequential or indirect damages due to loss of data or any other reason.

---
*Last document revision on 2023/08/15*
