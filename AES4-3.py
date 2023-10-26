from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# 随机生成k1和k2，每个都是16位
k1 = get_random_bytes(16)
k2 = get_random_bytes(16)

# k3为k1和k2拼接而成的32位密钥
k3 = k1 + k2

# 明文数据
data = b'This is a secret message.'

# 明文处理
def add_to_16(text):
    while len(text) % 16 != 0:
        text += b'\0'
    return text

data = add_to_16(data)

# 第一轮加密，使用k1
cipher1 = AES.new(k1, AES.MODE_ECB)
encrypt_data1 = cipher1.encrypt(data)

# 第二轮加密，使用k2
cipher2 = AES.new(k2, AES.MODE_ECB)
encrypt_data2 = cipher2.encrypt(encrypt_data1)

# 第三轮加密，使用k3
cipher3 = AES.new(k3, AES.MODE_ECB)
encrypt_data3 = cipher3.encrypt(encrypt_data2)
# 解密过程
# 第一轮解密，使用k3
decipher3 = AES.new(k3, AES.MODE_ECB)
decrypt_data2 = decipher3.decrypt(encrypt_data3)

# 第二轮解密，使用k2
decipher2 = AES.new(k2, AES.MODE_ECB)
decrypt_data1 = decipher2.decrypt(decrypt_data2)

# 第三轮解密，使用k1
decipher1 = AES.new(k1, AES.MODE_ECB)
decrypt_data = decipher1.decrypt(decrypt_data1)

print("Original Text:", data)
print("Triple-Encrypted Text:", encrypt_data3)
print("Decrypted Text:", decrypt_data)
