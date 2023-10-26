from Crypto.Cipher import AES
import os
import time

def generate_key():
    return os.urandom(32)  # 生成一个随机的32字节密钥

def pad(text):
    # 使用PKCS7填充文本，确保长度为16的倍数
    padding_length = AES.block_size - len(text) % AES.block_size
    padding = bytes([padding_length] * padding_length)
    return text + padding

def unpad(padded_text):
    # 删除PKCS7填充
    padding_length = padded_text[-1]
    return padded_text[:-padding_length]

def encrypt(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_text = pad(plaintext)
    return cipher.encrypt(padded_text)

def decrypt(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_text = cipher.decrypt(ciphertext)
    return unpad(padded_text)

# 模拟已知的明文-密文对
plaintext1 = b'Hello, World!1234'  # 明文1
plaintext2 = b'Hello, World!5678'  # 明文2

key = generate_key()  # 生成一个随机密钥
iv = os.urandom(16)  # 生成一个随机初始化向量

# 加密明文1和明文2
ciphertext1 = encrypt(plaintext1, key, iv)
ciphertext2 = encrypt(plaintext2, key, iv)

# 记录开始时间
start_time = time.time()

# 尝试中间相遇攻击
for possible_key in range(2**32):  # 假设密钥是32位
    intermediate_value = decrypt(ciphertext1, possible_key.to_bytes(16, 'big'), iv)
    
    if intermediate_value == decrypt(ciphertext2, key, iv):
        print(f"Found possible key: {possible_key.to_bytes(16, 'big')}")
        break

# 记录结束时间
end_time = time.time()

# 计算破解所需的时间
elapsed_time = end_time - start_time
print(f"Time taken to crack the key: {elapsed_time} seconds")
