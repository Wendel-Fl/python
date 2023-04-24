msg='welcome to Python 101: Strings'
#    0123456789  
# print(msg)

words = msg.split()

text = msg[18]+' '+words[0]+' '+msg[25:29]+' '+msg[8:10]+' '+msg[13]+msg[12]+msg[2]+msg[1]+msg[25]

# 1 Welcome Ring To Tyler
print(text.title())

back = text.split()
back.reverse()
newMsg = ' '.join(back)
print(newMsg.title())

# or

print(text[::-1].title())