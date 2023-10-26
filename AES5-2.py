# -*- coding: utf-8 -*-
#AES加密
import base64
from Crypto.Cipher import AES
import tkinter as tk
from tkinter import Label, Entry, Button, Text, END

iv = ''  # 偏移量
key = ''  # 密钥

# 补足字节方法
def pad(value):
    BLOCK_SIZE = 16  # 设定字节长度
    count = len(value)
    if count % BLOCK_SIZE != 0:
        add = BLOCK_SIZE - (count % BLOCK_SIZE)
    else:
        add = 0
    text = value + ("\0".encode() * add)  # 这里的"\0"必须编码成bytes，不然无法和text拼接
    return text

# 将明文用AES加密
def AES_en(data):
    # 将长度不足16字节的字符串补齐
    data = pad(data.encode())
    # 创建加密对象
    AES_obj = AES.new(key.encode("utf-8"), AES.MODE_CBC, iv.encode("utf-8"))
    # 完成加密
    AES_en_str = AES_obj.encrypt(data)
    # 用base64编码一下
    AES_en_str = base64.b64encode(AES_en_str)
    # 最后将密文转化成字符串
    AES_en_str = AES_en_str.decode("utf-8")
    return AES_en_str

def AES_de(data):
    # 解密过程逆着加密过程写
    # 将密文字符串重新编码成二进制形式
    data = data.encode("utf-8")
    # 将base64的编码解开
    data = base64.decodebytes(data)
    # 创建解密对象
    AES_de_obj = AES.new(key.encode("utf-8"), AES.MODE_CBC, iv.encode("utf-8"))
    # 完成解密
    AES_de_str = AES_de_obj.decrypt(data)
    # 去掉补上的空格
    AES_de_str = AES_de_str.strip()
    # 对明文解码
    AES_de_str = AES_de_str.decode("utf-8")
    return AES_de_str.strip(b'\x00'.decode())

def encrypt(data, key, iv):
    data = AES_en(data, key, iv)
    return data

def decrypt(data, key, iv):
    data = AES_de(data, key, iv)
    return data


# 原始密文和密钥
original_ciphertext = "l2RqRDfFtIho+GYA1XwPKQ=="
key = "1212121212121212"
iv = "1212121212121212"

# 导入必要的库
import base64
from Crypto.Cipher import AES

# 解密原始密文
def decrypt_cbc(ciphertext, key, iv):
    cipher = AES.new(key.encode("utf-8"), AES.MODE_CBC, iv.encode("utf-8"))
    plaintext = cipher.decrypt(base64.b64decode(ciphertext))
    return plaintext

# 输出原始密文的解密结果
original_plaintext = decrypt_cbc(original_ciphertext, key, iv)
print("原始密文:", original_plaintext)

#将第一个密文分组的第一个字节更改为0xFF
tampered_ciphertext = base64.b64decode(original_ciphertext)
tampered_ciphertext = bytearray(tampered_ciphertext)
tampered_ciphertext[0] = 0xFF

# 解密篡改后的密文
tampered_ciphertext = base64.b64encode(tampered_ciphertext).decode("utf-8")
tampered_plaintext = decrypt_cbc(tampered_ciphertext, key, iv)
print("修改分组后密文:", tampered_plaintext)
