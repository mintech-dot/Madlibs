def kalilinux():

   a= 1

qst ='''>>> Fill in the blanks with the appropriate words :
>>> Kali Linux is a Debian-based Linux <word1> aimed at advanced
<word2> Testing and Security Auditing. Kali contains several hundred
tools which are geared towards various information security tasks, such
as Penetration Testing, <word3> , Computer Forensics and <word4>.'''

print (qst)

word1 = input(">>>word1 :")
word2 = input("   word2 :")
word3 = input("   word3 :")
word4 = input("   word4 :")

print (f'''>>> A computer is a {word1} that can be instructed to carry out sequences 
of {word2} or logical operations automatically via computer programming.
Modern computers have the ability to follow generalized sets of operations,
called {word3}. These programs enable computers to perform an extremely wide
range of {word4}. ''')

if word1== "distribution" and word2 == "Penetration" and word3 == "Security research" and word4 == "Reverse Engineering" :
    print (" congratas , you won ! ")
else :
    print (">>> sorry , it is not the best answer !")


kalilinux()
