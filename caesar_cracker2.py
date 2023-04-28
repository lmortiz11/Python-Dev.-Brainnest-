'''
	This program can hack messages encrypted 
	with the Caesar cipher from the previous project, even 
	if you don’t know the key. There are only 26 
	possible keys for the Caesar cipher, so a computer can easily try all possible decryptions and dis play the results to the user. In cryptography, we call 
	this technique a brute-force attack.
'''
letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

msg = input("Enter the message to decrypt.")

def decrypt(msg, key):
    decrypt_message=''
    message=msg.upper()
    for charac in message:
        if charac not in letters:
            new_charac= charac
        
        else: 
            index= letters.index(charac)- key
            if index <0:
                new_charac=letters[index+26]
            else:
                new_charac = letters[index]
        decrypt_message += new_charac
        
    yield (decrypt_message)
    

# run the decrypt function for all the keys
for key in range(26):
    print(key)
    options = decrypt(msg,key)
    for i in options:
        print(i)

