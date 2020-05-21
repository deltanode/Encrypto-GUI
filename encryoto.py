import tkinter as tk
from tkinter import messagebox

# Encryption/Decryption

cdtxt="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWX/*-+.,./;':<>?{}[]+_)(&^%$#@!~`"
len= len(cdtxt)

def encrypt(string,key=2):
    res = ""
    for i in string:
        pos=cdtxt.find(i)
        new_pos= (pos+key)%len
        res=res+cdtxt[new_pos]
        # print(pos,new_pos)
    return res

def decrypt(string,key=2):
    res = ""
    for i in string:
        pos=cdtxt.find(i)
        new_pos= (pos-key)%len
        res=res+cdtxt[new_pos]
        # print(pos,new_pos)
    return res

key=2
einp="EncryptPassword@123"
dinp="GpetOrvRcuuyqtf~345"

# print(inp)
print(encrypt(einp))
# dinp=encrypt(einp,key)
# print(decrypt(dinp,key))

def esubmit():
    e_value=encrypt(tb_inp.get(),int(tb_key.get()))
    # messagebox.showinfo("This is title","Encryption of: "+tb_inp.get()+ "is "+e_value)
    txt_out.delete(1.0,tk.END)
    txt_out.insert(tk.INSERT,e_value)
    # txt.set(e_value)

def dsubmit():
    d_value=decrypt(tb_inp.get(),int(tb_key.get()))
    # messagebox.showinfo("This is title","Encryption of: "+tb_inp.get()+ "is "+e_value)
    # tb_key.insert(0,e_value)
    # txt.set(d_value)
    txt_out.delete(1.0, tk.END)
    txt_out.insert(tk.INSERT, d_value)
#Creating GUI

root=tk.Tk()
root.title("Encrypto-PY")
root.geometry("460x390")

photo = tk.PhotoImage(file = "icon.png")
root.iconphoto(False,photo )

# txt="Enter text for Encription/Decription"
fontstyle=("Helvetica",10,"bold")

#Text Input ----------------------------------------------------

lb_inp=tk.Label(root,text="Text to Encrypt/Decrypt:",font=fontstyle)
lb_inp.grid(row=0,column=0,columnspan=2,sticky=tk.W,padx=5, pady=5)

tb_inp=tk.Entry(root,bd=1,width=40,font=("Helvetica",15,"bold"))                       #Textbox - Input
tb_inp.grid(row=1,columnspan=2,sticky=tk.W,padx=5, pady=5)

#Key Input ----------------------------------------------------

lb_key=tk.Label(root,text="Enter Secret Key (Remember this for Decryption)",font=fontstyle)     #Label - Key
lb_key.grid(row=2,columnspan=2,sticky=tk.W,padx=5, pady=5)

tb_key=tk.Entry(root,justify=tk.LEFT,font=("Helvetica",15,"bold"),width=40)                       #Textbox - Key
tb_key.insert(0,2)
tb_key.grid(row=3,columnspan=2,sticky=tk.W,padx=5, pady=5)

#Encrypt/Decrypt Button ----------------------------------------------------

btn_encrypt = tk.Button(root,text="Encrypt",command=esubmit,fg="white",bg="#f57971",width=29)   #Button - Encrypt
btn_encrypt.grid(row=5,column=0,sticky=tk.W,padx=5, pady=5)

btn_decrypt = tk.Button(root,text="Decrypt",command=dsubmit,fg="white",bg="green",width=29)     #Button - Decrypt
btn_decrypt.grid(row=5,column=1,sticky=tk.W,padx=5, pady=5)

# btn_reset = tk.Button(root,text="RESET",command="")                        #Button - Reset
# btn_reset.grid(row=6,column=0,columnspan=2,sticky=tk.W,padx=5, pady=5)

#Output Section ----------------------------------------------------

lb_out=tk.Label(root,text="Output : ",font=fontstyle)                         #Label - Input
lb_out.grid(row=7,column=0,columnspan=2,sticky=tk.W,padx=5, pady=5)

# txt=tk.StringVar(root, value='default text')
# txt.set("Hi")
# lb_out=tk.Label(root,textvariable=txt,bd=40,bg="LightGrey",justify=tk.LEFT)

txt_out=tk.Text(root,bg="white",height=10,width=55)                          #Label - Output
txt_out.grid(row=8,columnspan=2,sticky=tk.W,padx=5, pady=5)

root.mainloop()
