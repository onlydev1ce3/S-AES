from Crypto.Cipher import AES
import os
from Crypto import Random
import base64

class AESUtil:

    __BLOCK_SIZE_16 = BLOCK_SIZE_16 = AES.block_size

    @staticmethod
    def encryt(string, key, iv):

        cipher = AES.new(key, AES.MODE_CBC, iv)
        x = AESUtil.__BLOCK_SIZE_16 - (len(string) % AESUtil.__BLOCK_SIZE_16)
        # 如果最后一块不够16位需要用字符进行补全
        if x != 0:
            string = string + chr(x)*x
        msg = cipher.encrypt(string.encode('utf-8'))
        return msg

    @staticmethod
    def decrypt(en_str, key, iv):
        cipher = AES.new(key, AES.MODE_CBC, iv)
        msg = cipher.decrypt(en_str)
        padding_len = msg[len(msg)-1]
        return msg[0:-padding_len]


if __name__ == "__main__":

    string = '1212121212121212'
    key = b"d41d8cd98f00b204e9800998ecf8427e"   # 32位
    iv = b"1234567812345678"    # 16位
    res = AESUtil.encryt(string, key, iv)
    print('加密结果为：')
    print(res)  
    print("解密结果为")
    print(AESUtil.decrypt(res, key, iv))  
