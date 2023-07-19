# Compact xors

For this challenge we can use the fact that we know the format of the flag : amateursCTF{...}

So we can xor the string : "amateursCTF{" with the first bytes of the xor by doing so we notice that the key is composed as follow : 

if the index of the byte is even we byte is null so the byte in the message is not changed and if the byte is odd it's equals to the previous byte in the original message. 

See resolve.py for the solution. 