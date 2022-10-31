input = ("Welcome, User_12!!")

s=[input[i] for i in range (len(input)) if (input[i].isalpha) == True]
s="".join(s)
#s = ''.join(filter(str.isalpha, input))
print(s)	# WelcomeUser12

