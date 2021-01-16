import os
def metasploit():

    a = 1

qst ='''>>> Fill in the blanks with the appropriate words :
>>> The Metasploit Project is a computer <word1> project that provides
information about security vulnerabilities and aids in <word2> testing and IDS
signature development.Its best-known sub-project is the <word3> Metasploit 
Framework, a tool for developing and executing <word4> code against a remote
target machine.'''

print (qst)

word1 = input(">>>word1 :")
word2 = input("   word2 :")
word3 = input("   word3 :")
word4 = input("   word4 :")

print (f'''>>> The Metasploit Project is a computer {word1} project that provides
information about security vulnerabilities and aids in {word2} testing and IDS
signature development.Its best-known sub-project is the {word3} Metasploit 
Framework, a tool for developing and executing {word4} code against a remote
target machine. ''')

if word1== "security" and word2 == "penetration" and word3 == "open-source" and word4 == "exploit" :
    print (" congratas , you won ! ")
else :
    print (">>> sorry , it is not the best answer !")


metasploit()
