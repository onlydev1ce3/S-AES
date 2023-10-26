# -*- coding: utf-8 -*-
#AES加密
import base64
from Crypto.Cipher import  AES
import tkinter as tk
from tkinter import Label, Entry, Button, Text, END

iv=''#偏移量
key=''#密钥

#补足字节方法
def pad(value):
    BLOCK_SIZE = 16  # 设定字节长度
    count=len(value)
    if(count%BLOCK_SIZE !=0):
        add=BLOCK_SIZE-(count%BLOCK_SIZE)
    else:
        add=0
    text=value+("\0".encode()*add) # 这里的"\0"必须编码成bytes，不然无法和text拼接
    return text
# 将明文用AES加密
def AES_en(data):
    # 将长度不足16字节的字符串补齐
    data=pad(data.encode())
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
    AES_de_str =AES_de_str.strip()
    # 对明文解码
    AES_de_str = AES_de_str.decode("utf-8")
    return AES_de_str.strip(b'\x00'.decode())


# AES加密相关函数，略去之前的代码

def encrypt(data, key, iv):
    data = AES_en(data, key, iv)
    return data

def decrypt(data, key, iv):
    data = AES_de(data, key, iv)
    return data

def encrypt_callback():
    global key, iv
    key = key_entry.get()
    iv = iv_entry.get()
    plaintext = plaintext_entry.get()
    if key and iv and plaintext:
        encrypted_text = AES_en(plaintext)
        result_text.delete(1.0, END)
        result_text.insert(1.0, f"加密为：{encrypted_text}")

def decrypt_callback():
    global key, iv
    key = key_entry.get()
    iv = iv_entry.get()
    ciphertext = ciphertext_entry.get()
    if key and iv and ciphertext:
        decrypted_text = AES_de(ciphertext)
        result_text.delete(1.0, END)
        result_text.insert(1.0, f"解密为：{decrypted_text}")

# 创建GUI窗口
window = tk.Tk()
window.title("AES加密解密工具")

# 标签和输入框
key_label = Label(window, text="密钥:")
key_label.pack()
key_entry = Entry(window)
key_entry.pack()

iv_label = Label(window, text="偏移量:")
iv_label.pack()
iv_entry = Entry(window)
iv_entry.pack()

plaintext_label = Label(window, text="明文:")
plaintext_label.pack()
plaintext_entry = Entry(window)
plaintext_entry.pack()

ciphertext_label = Label(window, text="密文:")
ciphertext_label.pack()
ciphertext_entry = Entry(window)
ciphertext_entry.pack()

# 加密和解密按钮
encrypt_button = Button(window, text="加密", command=encrypt_callback)
encrypt_button.pack()

decrypt_button = Button(window, text="解密", command=decrypt_callback)
decrypt_button.pack()

# 结果文本框
result_text = Text(window, height=5, width=40)
result_text.pack()

# 启动GUI主循环
window.mainloop()
 