en = input("enter your email :: ") #ryanrenolds18@gmail.com

for i in range(len(en)):
    if en[i] == "@":
        
        print("name :"+ en[:i] )
        print("domain :" + en[i+1:])