import tkinter as tk

# Encryption/Decryption

cdtxt="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWX/*-+.,./;':<>?{}[]+_)(&^%$#@!~`"
len= len(cdtxt)

def encrypt(string,key):
    res = ""
    for i in string:
        pos=cdtxt.find(i)
        new_pos= (pos+key)%len
        res=res+cdtxt[new_pos]
        # print(pos,new_pos)
    return res

def decrypt(string,key):
    res = ""
    for i in string:
        pos=cdtxt.find(i)
        new_pos= (pos-key)%len
        res=res+cdtxt[new_pos]
        # print(pos,new_pos)
    return res

key=2
einp="EncryptPassword@123"
dinp="Gpet0rvRcuuyqtf~345"

# print(inp)
print(encrypt(einp,key))
# dinp=encrypt(einp,key)
print(decrypt(dinp,key))

#Creating GUI

root=tk.Tk()

