'''
The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It 
encrypts letters by shifting them over by a 
certain number of places in the alphabet. We 
call the length of shift the key. For example, if the 
key is 3, then A becomes D, B becomes E, C becomes 
F, and so on. To decrypt the message, you must shift 
the encrypted letters in the opposite direction. This 
program lets the user encrypt and decrypt messages 
according to this algorithm.

When you run the code, the output will look like this:

Do you want to (e)ncrypt or (d)ecrypt?
> e
Please enter the key (0 to 25) to use.
> 4
Enter the message to encrypt.
> Meet me by the rose bushes tonight.
QIIX QI FC XLI VSWI FYWLIW XSRMKLX.


Do you want to (e)ncrypt or (d)ecrypt?
> d
Please enter the key (0 to 26) to use.
> 4
Enter the message to decrypt.
> QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
MEET ME BY THE ROSE BUSHES TONIGHT.

'''

letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(msg, key):
    encrypt_message=''
    message=msg.upper()
    for charac in message:
        if charac not in letters:
            new_charac= charac
        
        else: 
            index= letters.index(charac)+ key
            if index>=26:
                new_charac=letters[index-26]
            else:
                new_charac = letters[index]
        encrypt_message += new_charac
        
    return encrypt_message
        

def decrypt(msg, key):
    decrypt_message=''
    message=msg.upper()
    for charac in message:
        if charac not in letters:
            new_charac= charac
        
        else: 
            index= letters.index(charac)- key
            if index<0:
                new_charac=letters[index+26]
            else:
                new_charac = letters[index]
        decrypt_message += new_charac
        
    return decrypt_message
    

e_d = input("Do you want to (e)ncrypt or (d)ecrypt?")
key = int(input("Please enter the key (0 to 26) to use:"))
msg = input("Enter the message to encrypt:")

if e_d=='e':
    print( encrypt(msg,key))
    
elif e_d=='d':
    print (decrypt(msg,key))
    
else:
    print("invalid value")

    