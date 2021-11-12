en = input("enter your email :: ")  # ryanrenolds18@gmail.com
k = list(en.partition("@"))


print("name :" + str(k[0]))
print("domain :" + str(k[2]))
