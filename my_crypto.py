# This Python file uses the following encoding: utf-8

# This file is part of pyCrypto, an encryption/decryption/hashing
# app developed in Python and based on PySide6
# Written by Leonardo Miliani in 2023
# Released under the terms of the GNU General Public License v3.0 or later
#
# Please read the readme file for instructions and details
#

import struct, os  # needed to pack nonce and to access to filesystem
import secrets  # needed to generate random numbers
from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes,
)

from cryptography.hazmat.primitives import (
    hashes
)

class MyCrypto():
    def __init__(self, algorithm, keysize = 0, blocksize = 0, iv_size = 0, mode = ""):
        super().__init__()
        self.algorithm = algorithm
        self.keysize = keysize
        self.blocksize = blocksize
        self.blocksize_byte = self.blocksize // 8
        self.mode = mode
        self.ivsize = iv_size
        self.nonce = 0 # used by ChaCha20 only

    # set algorithm for encryption/decryption
    def set_crypto_alg(self, algorithm, key, mode):
        if algorithm == "AES":
            cipher = Cipher(algorithms.AES(key), mode)
        elif algorithm == "Camellia":
            cipher = Cipher(algorithms.Camellia(key), mode)
        elif algorithm == "ChaCha20":
            cipher = Cipher(algorithms.ChaCha20(key, self.nonce), mode = None)
        else:
            cipher = Cipher(algorithms.CAST5(key), mode)
        return cipher

    # encrypt a file
    def encryptFile(self, file_name, key):
        # create IV (initialization vector)
        inVec = self.IV(self.ivsize)
        # initialize encryption algorithm
        mode = None
        if self.algorithm == "ChaCha20":
            counter = 0
            iv = secrets.token_bytes(8)
            self.nonce = struct.pack("<Q", counter) + iv
            inVec = self.nonce
        else:
            if self.mode == "OFB":
                mode = modes.OFB(inVec)
            else:
                mode = modes.CBC(inVec)
        cipher = self.set_crypto_alg(self.algorithm, key, mode)
        encryptor = cipher.encryptor()
        # prepare output file
        fileOutput = open(file_name + '.enc', "wb")
        # write IV at the beginning of the file
        fileOutput.write(inVec)
        # open input file
        fileSize = os.path.getsize(file_name)
        fileInput = open(file_name, "rb")
        if self.mode == "OFB":
            # read data in blocks of blocks of 'blocksize' bytes
            for i in range(0, fileSize, self.blocksize_byte):
                block = fileInput.read(self.blocksize_byte)
                # encrypt the block and write it into the output file
                cipherText = encryptor.update(bytes(block))
                fileOutput.write(bytearray(cipherText))
        else:
            padding = -1
            # read data in blocks of 'blocksize' bytes
            for i in range(0, fileSize, self.blocksize_byte):
                block = fileInput.read(self.blocksize_byte)
                # encrypt the block and write it into the output file
                endIndex = i + self.blocksize_byte
                endIndex = fileSize if endIndex > fileSize else endIndex
                # check if input data is finished
                if len(block) < self.blocksize_byte:
                    # check if pad is necessary
                    padding = self.blocksize_byte - (endIndex % self.blocksize_byte)
                    if padding != self.blocksize_byte:
                        # add padding
                        blck = self.padding(block, self.blocksize_byte, pad = padding)
                        block = [ord(x) for x in blck]
                # encrypt the block and write it into the output file
                cipherText = encryptor.update(bytes(block))
                fileOutput.write(bytearray(cipherText))
            # if file lenght is a mul of block_size, add another block
            if padding == self.blocksize_byte:
                block = [self.blocksize_byte] * self.blocksize_byte
                cipherText = encryptor.update(bytes(block))
                fileOutput.write(bytearray(cipherText))
        # finalize cipher
        cipherText = encryptor.finalize()
        if len(cipherText) > 0:
            fileOutput.write(bytearray(cipherText))
        # close files
        fileOutput.flush()
        fileOutput.close()
        fileInput.close()


    def decryptFile(self, file_name, key):
        fileSize = os.path.getsize(file_name)
        # remove tailing ".enc" from filename
        if file_name[-4:] == ".enc":
            outputfile_name = file_name[:-4]
        else:
            outputfile_name = file_name
        # prepare output file
        fileOutput = open(outputfile_name + '.dec', "wb")
        # open input file
        fileInput = open(file_name, "rb")
        # the first block contains the IV...
        inVec = fileInput.read(self.blocksize_byte)
        self.nonce = inVec
        # initialize encryption algorithm
        mode = None
        if self.algorithm != "ChaCha20":
            if self.mode == "OFB":
                mode = modes.OFB(inVec)
            else:
                mode = modes.CBC(inVec)
        cipher = self.set_crypto_alg(self.algorithm, key, mode)
        decryptor = cipher.decryptor()
        # ... while the other ones the data
        if self.mode == "OFB":
            for i in range(self.blocksize_byte, fileSize, self.blocksize_byte):
                # read a block
                block = fileInput.read(self.blocksize_byte)
                decBlock = decryptor.update(block)
                # write the decrypted block into output file
                fileOutput.write(bytearray(decBlock))
        else:
            endIndex = self.blocksize_byte
            endIndex = fileSize if endIndex > fileSize else endIndex
            # read block sequentially
            for i in range(self.blocksize_byte, fileSize, self.blocksize_byte):
                # compute the end of the next block
                endIndex = i + self.blocksize_byte
                endIndex = fileSize if endIndex > fileSize else endIndex
                # read another block
                block = fileInput.read(self.blocksize_byte)
                decBlock = decryptor.update(block)
                # the last block is padded
                if endIndex == fileSize:
                    # remove the extra bytes added for padding:
                    # gets the value of the last cell and removes an equal number of bytes
                    decBlock = decBlock[:-decBlock[-1]]
                # write the block into output file
                fileOutput.write(bytearray(decBlock))
        # finalize the cipher: write any leftover bytes 
        plainText = decryptor.finalize()
        if len(plainText) > 0:
            fileOutput.write(bytearray(plainText))
        # close files
        fileOutput.flush()
        fileOutput.close()
        fileInput.close()
    

    # initialization vector
    def IV(self, ivsize):
        return secrets.token_bytes(ivsize // 8)


    # string padding
    def padding(self, txt, lng, pad = 0, truncate = False):
        text = str(txt)
        # if it's a byte array, remove un-necessary chars
        if text.find("b'") != -1:
            text = text[2:-1]
        pad = pad
        # is truncate required?
        if truncate:
            if len(text) % lng == 0:
                # lenght is equal: return the given string
                return text
            else:
                # return padded string
                return text.ljust(len(text) + lng - (len(text) % lng))
        # check if the string is already padded mod lng
        if len(text) == lng:
            # return passed string
            return text
        elif len(text) > lng:
            return text[:lng]
        else:
            # return padded string
            return text.ljust(len(text) + lng - (len(text) % lng), chr(pad))


    # text hashing
    def hash_text(self, txt):
        # set hash algorithm
        digest = self.set_hash_algorithm(self.algorithm)
        # compute hash
        digest.update(txt)
        # return hash
        return digest.finalize()


    # file hashing
    def hash_file(self, file_name):
        # set hash algorithm
        digest = self.set_hash_algorithm(self.algorithm)
        # open input file
        fileSize = os.path.getsize(file_name)
        fileInput = open(file_name, "rb")
        # read data in blocks of bytes
        for i in range(0, fileSize, 128):
            block = fileInput.read(128)
            # pass the block to the hash
            digest.update(block)
        return digest.finalize()


    # set hash algorithm
    def set_hash_algorithm(self, algorithm):
        if algorithm == "BLAKE2":
            digest = hashes.Hash(hashes.BLAKE2b(64))
        elif algorithm == "MD5":
            digest = hashes.Hash(hashes.MD5())
        elif algorithm[:-3] == "SHA":
            type = algorithm[3:]
            if type == "256":
                digest = hashes.Hash(hashes.SHA256())
            elif type == "384":
                digest = hashes.Hash(hashes.SHA384())
            elif type == "512":
                digest = hashes.Hash(hashes.SHA512())
        return digest
