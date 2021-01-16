def programming_language():

   a= 1

qst ='''>>> Fill in the blanks with the appropriate words :
>>> A programming language is a computer language programmers use to <word1>
software <word2> , <word3> , or other sets of instructions for computers to execute.
Although many languages share similarities, each has its own <word4>.'''

print (qst)

word1 = input(">>>word1 :")
word2 = input("   word2 :")
word3 = input("   word3 :")
word4 = input("   word4 :")

print (f'''>>> A programming language is a computer language programmers use to {word1}
software {word2} , {word3} , or other sets of instructions for computers to execute.
Although many languages share similarities, each has its own {word4}. ''')

if word1== "develop" and word2 == "programs" and word3 == "scripts" and word4 == "syntax" :
    print (" congratas , you won ! ")
else :
    print (">>> sorry , it is not the best answer !")


programming_language()
