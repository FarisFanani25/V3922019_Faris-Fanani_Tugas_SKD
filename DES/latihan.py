#!/usr/bin/env python
# coding: utf-8

# In[4]:


from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

def procces_key(key) :
    return key[:8]

text = "Teknik Informatika"
key = procces_key(b'1n1kunC1')

BLOCK_SIZE = 8

des = DES.new(key, DES.MODE_ECB)
padded_text = pad(text.encode(), BLOCK_SIZE)
encrypted_text = des.encrypt(padded_text)
decrypted_text = des.decrypt(encrypted_text)

print("Plain Teks : ", text)
print("Hasil Enkripsi : ", encrypted_text)
print("Hasil Dekripsi : ", decrypted_text.decode())


# In[ ]:




