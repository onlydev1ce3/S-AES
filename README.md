# S-AES

![image](https://github.com/onlydev1ce3/S-AES/assets/145557897/003f4627-cd22-475d-bf36-1bc38b439cc6)


TASK 1:基本功能 S-AES.py

加密：

![image](https://github.com/onlydev1ce3/S-AES/assets/145557897/0fd81e0f-26c6-4ea6-a9e1-24a8756cdf24)

![image](https://github.com/onlydev1ce3/S-AES/assets/145557897/81756de8-e31c-46f7-9d0a-c6493d113728)

解密：

![image](https://github.com/onlydev1ce3/S-AES/assets/145557897/a7f918fa-b62a-413e-915a-a2b719816b8f)

![image](https://github.com/onlydev1ce3/S-AES/assets/145557897/1b3803d6-56e5-46d0-b163-c46c5364e3fa)

TASK 2：交叉测试 ✔

TASK 3: 扩展功能 ASCII加密解密  AES(ASCLL).py


![image](https://github.com/onlydev1ce3/S-AES/assets/145557897/5cff587b-d76b-4825-80c6-c52ecd41602b)


![image](https://github.com/onlydev1ce3/S-AES/assets/145557897/5512751d-d30c-44bb-8b61-c7755b4c786e)


![image](https://github.com/onlydev1ce3/S-AES/assets/145557897/a1dfe5f8-d9e6-437f-afc7-5ff08233b73d)

TASK 4:多重加密
4-1 双重加密将S-AES算法通过双重加密进行扩展，分组长度仍然是16 bits，但密钥长度为32 bits。 AES4-1.py

![image](https://github.com/onlydev1ce3/S-AES/assets/145557897/3e392d10-311f-47c6-8c59-189f93713850)


![image](https://github.com/onlydev1ce3/S-AES/assets/145557897/0a12b7f6-2131-45b9-a2fb-19e5141be884)

4-2 中间相遇攻击假设你找到了使用相同密钥的明、密文对(一个或多个)，请尝试使用中间相遇攻击的方法找到正确的密钥Key(K1+K2)。   AES4-2.py


![image](https://github.com/onlydev1ce3/S-AES/assets/145557897/a166feee-20b5-4374-a44c-ea5d18c08bf8)


4-3 三重加密将S-AES算法通过三重加密进行扩展，下面两种模式选择一种完成：(1)按照32 bits密钥Key(K1+K2)的模式进行三重加密解。 AES4-3.py

![image](https://github.com/onlydev1ce3/S-AES/assets/145557897/d27e3614-cdd1-4018-9644-c473ed6d02c5)

![image](https://github.com/onlydev1ce3/S-AES/assets/145557897/a19b59fb-ebe0-417e-b62c-b8b911809d5b)

TASK 5:工作模式. 
基于S-AES算法，使用密码分组链(CBC)模式对较长的明文消息进行加密。注意初始向量(16 bits) 的生成，并需要加解密双方共享。在CBC模式下进行加密，并尝试对密文分组进行替换或修改，然后进行解密，请对比篡改密文前后的解密结果。    
AES5-1.py
AES5-2.py

![image](https://github.com/onlydev1ce3/S-AES/assets/145557897/6e314ba4-9229-4b1c-bc3f-c2c5a4578c11)

![image](https://github.com/onlydev1ce3/S-AES/assets/145557897/9484a957-f928-486b-b0e4-24be34b7b2d7)




