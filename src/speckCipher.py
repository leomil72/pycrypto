#
# IMPLEMENTATION OF SPECK64/128 CIPHER IN DART PROGRAMMING LANGUAGE
#
# Key features of the algorithm:
# block size: 64-bits (in 2 32-bits words)
# key size: 128-bits (in 4 32-bits words)
# Nr. of rounds: 27
# Word size: 32-bits
#
# OFB cipher mode of operation
# This mode of operation manages files as streams of data
#
# Written by Leonardo Miliani (2023)
# Release under the terms of the CC license BY-NC-SA 4.0 or later

import os       # needed to access to filesystem
import secrets  # needed to generate random numbers


class SpeckCipher:
    ### Implementation of Speck64/128 Cipher
    def __init__(self, BLOCK_SIZE = 64, KEY_SIZE = 128, ROUNDS = 27, WORD_SIZE_N = 32, KEY_WORDS_M = 4):
        self.BLOCK_SIZE = BLOCK_SIZE
        self.KEY_SIZE = KEY_SIZE
        self.ROUNDS = ROUNDS
        self.WORD_SIZE_N = WORD_SIZE_N
        self.KEY_WORDS_M = KEY_WORDS_M
        self.BYTES_PER_BLOCK = 8

    # encrypt a file
    def encryptFile(self, fileName, key):
        cipherText = [0, 0]
        plainText = [0, 0]
        # get roundkey from key
        roundKey = self.keySchedule(self.bytesToWord32(key))
        # create and store IV (initialization vector)
        initVect = self.generateIV()
        dataBytes = self.word32ToBytes(initVect)
        # prepare output file
        fileOutput = open(fileName + '.enc', "wb")
        # write IV
        fileOutput.write(bytearray(dataBytes))
        # open input file
        fileSize = os.path.getsize(fileName)
        fileInput = open(fileName, "rb")
        blockSizeInBytes = self.BLOCK_SIZE // self.BYTES_PER_BLOCK
        padding = -1
        # read blocks of BYTES_PER_BLOCK bytes
        for i in range(0, fileSize, blockSizeInBytes):
            block = fileInput.read(blockSizeInBytes)
            endIndex = i + blockSizeInBytes
            endIndex = fileSize if endIndex > fileSize else endIndex
            # check if pad is necessary
            if len(block) < blockSizeInBytes:
                padding = blockSizeInBytes - (endIndex % blockSizeInBytes)
                if padding != blockSizeInBytes:
                    block = self.padding(block, blockSizeInBytes)
            # encrypt the block and write it into the output file
            block_list = list(block)
            plainText = self.bytesToWord32(block_list)
            cipherText = self.encrypt(plainText, roundKey, initVect)
            encBlock = self.word32ToBytes(cipherText)
            fileOutput.write(bytearray(encBlock))
        # if file lenght is a mul of BYTES_PER_BLOCK, add another block
        if padding == blockSizeInBytes:
            block = [self.BYTES_PER_BLOCK] * blockSizeInBytes
            plainText = self.bytesToWord32(block)
            cipherText = self.encrypt(plainText, roundKey, initVect)
            encBlock = self.word32ToBytes(cipherText)
            fileOutput.write(bytearray(encBlock))
        # when exiting from 'with', automatically files are flushed and closed
        fileOutput.flush()
        fileOutput.close()
        fileInput.close()


    def decryptFile(self, fileName, key):
        cipherText = [0, 0]
        plainText = [0, 0]
        # get roundkey from key
        roundKey = self.keySchedule(self.bytesToWord32(key))
        # check if file name contains ".enc"
        if fileName[-4:] == ".enc":
            destFileName = fileName[:-4]
        else:
            destFileName = fileName
        destFileName += ".dec"
        # prepare output file
        fileOutput = open(destFileName, "wb")
        # open input file
        fileSize = os.path.getsize(fileName)
        fileInput = open(fileName, "rb")
        blockSizeInBytes = self.BLOCK_SIZE // self.BYTES_PER_BLOCK
        # create IV (initialization vector)
        initVect = [0, 0]
        for i in range(0, fileSize, blockSizeInBytes):
            endIndex = i + blockSizeInBytes
            endIndex = fileSize if endIndex > fileSize else endIndex
            block = list(fileInput.read(blockSizeInBytes))
            if i == 0:
                # the first block contains the IV...
                initVect = self.bytesToWord32(block)
            else:
                # ...while the other ones contain normal data...
                cipherText = self.bytesToWord32(block)
                plainText = self.decrypt(cipherText, roundKey, initVect)
                decBlock = self.word32ToBytes(plainText)
                # ...except for the last one, that is padded
                if endIndex == fileSize:
                    # get the lenght of padding
                    print(decBlock[7], chr(decBlock[7]))
                    lnpd = decBlock[7]
                    print(lnpd)
                    # remove the extra bytes and write the remaining data
                    while lnpd > 0:
                        decBlock.pop()
                        lnpd -= 1
                # write into output file
                fileOutput.write(bytearray(decBlock))
        fileOutput.flush()
        fileOutput.close()
        fileInput.close()


    # 32-bits left rotation function
    def Rol(self, x, r):
        tmp = (x >> (self.WORD_SIZE_N - r)) & 0x00000000ffffffff
        return (((x << r) | tmp) & 0x00000000ffffffff)
    
    
    # 32-bits right rotation function
    def Ror(self, x, r):
       tmp = (x << (self.WORD_SIZE_N - r)) & 0x00000000ffffffff
       return (((x >> r) | tmp) & 0x00000000ffffffff)
    

    # initialization vector: returns two random 32-bits integer
    def generateIV(self):
        return[secrets.randbits(32), secrets.randbits(32)]

    
    # convert blocks of 4 bytes into 32-bits words using little-endian order:
    # first byte into the right-most 8-bits, and so on up to the left
    def bytesToWord32(self, inBytes):
        lenght = len(inBytes)
        outWords = [0] * (lenght // 4)
        j = 0
        for i in range(0, lenght, 4):
            outWords[j] = inBytes[i] | (inBytes[i + 1] << 8) | (inBytes[i + 2] << 16) | (inBytes[i + 3] << 24)
            j += 1
        return outWords
    

    # revert a 32-bits word into 4 bytes using little-endian order:
    # right-most 8-bits into the first byte, and so on up to the left
    def word32ToBytes(self, inWords):
        lenght = len(inWords)
        outBytes = [0] * (lenght * 4)
        j = 0
        for i in range(0, lenght):
            outBytes[j] = inWords[i] & 0xff
            outBytes[j + 1] = (inWords[i] >> 8) & 0xff
            outBytes[j + 2] = (inWords[i] >> 16) & 0xff
            outBytes[j + 3] = (inWords[i] >> 24) & 0xff
            j += 4
        return outBytes
    
    # key scheduler: gets a key and prepare a round key buffer
    def keySchedule(self, key):
        subKey = [0] * self.ROUNDS
        key = key
        A, B, C, D = key[0], key[1], key[2], key[3]

        for i in range(0, self.ROUNDS, 3):
            subKey[i] = A
            B = self.Ror(B, 8)
            B = (B + A) & 0x00000000ffffffff
            B ^= i
            A = self.Rol(A, 3)
            A ^= B

            subKey[i + 1] = A
            C = self.Ror(C, 8)
            C = (C + A) & 0x00000000ffffffff
            C ^= (i + 1)
            A = self.Rol(A, 3)
            A ^= C

            subKey[i + 2] = A
            D = self.Ror(D, 8)
            D = (D + A) & 0x00000000ffffffff
            D ^= (i + 2)
            A = self.Rol(A, 3)
            A ^= D
        return subKey


    # encrypt a block using the round key and the IV, and returns a crypted block
    def encrypt(self, PlainText, roundKey, initVect):
        cipherText = PlainText.copy()
        plainText = PlainText.copy()
        for i in range(0, self.ROUNDS):
            initVect[1] = self.Ror(initVect[1], 8)
            initVect[1] = (initVect[1] + initVect[0]) & 0x00000000ffffffff
            initVect[1] ^= roundKey[i]
            initVect[0] = self.Rol(initVect[0], 3)
            initVect[0] ^= initVect[1]
        cipherText[0] = plainText[0] ^ initVect[0]
        cipherText[1] = plainText[1] ^ initVect[1]
        return cipherText
  

    # decrypt a block using the round key and the IV, and returns a decrypted block
    def decrypt(self, CipherText, roundKey, initVect):
        plainText = CipherText.copy()
        cipherText = CipherText.copy()
        for i in range(0, self.ROUNDS):
            initVect[1] = self.Ror(initVect[1], 8)
            initVect[1] = (initVect[1] + initVect[0]) & 0x00000000ffffffff
            initVect[1] ^= roundKey[i]
            initVect[0] = self.Rol(initVect[0], 3)
            initVect[0] ^= initVect[1]
        plainText[0] = cipherText[0] ^ initVect[0]
        plainText[1] = cipherText[1] ^ initVect[1]
        return plainText
  

    # string padding
    def padding(self, txt, lng, truncate = False):
        """Pad a string 'txt' to 'lng' lenght, eventually truncating it if longer than 'lng'"""
        # is truncation required (used for passwords)?
        if truncate:
            text = str(txt)
            if len(text) % lng == 0:
                # lenght is correct: return the given string
                return text
            else:
                # return padded (with spaces) & truncated string
                return text.ljust(len(text) + lng - (len(text) % lng))
        # convert the byte string into a list of ints
        val = [x for x in txt]
        res = []
        # check if the string is already padded mod lng
        if len(val) == lng:
            # return passed string if lenght is correct
            res = val.copy()
        elif len(txt) > lng:
            # return 'lng' chars if string is longer
            res = val[:lng]
        else:
            # padd string if string is shorter with 'lng'
            diff = lng -len(val)
            res = val.copy()
            while len(res) < lng:
                res.append(diff)
        return bytes(res)
