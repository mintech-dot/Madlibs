def android():

   a= 1
   
qst ='''>>> Fill in the blanks with the appropriate words :
>>> Android is a mobile operating <word1> based on a modified
version of the <word2> kernel and other open source <word3>, designed
primarily for touchscreen <word4> devices such as smartphones and tablets.'''

print (qst)

word1 = input(">>>word1 :")
word2 = input("   word2 :")
word3 = input("   word3 :")
word4 = input("   word4 :")

print (f'''>>> Android is a mobile operating {word1} based on a modified
version of the {word2} kernel and other open source {word3}, designed
primarily for touchscreen {word4} devices such as smartphones and tablets. ''')

if word1== "system" and word2 == "Linux" and word3 == "software" and word4 == "mobile" :
    print (" congratas , you won ! ")
else :
    print (">>> sorry , it is not the best answer !")


android()
