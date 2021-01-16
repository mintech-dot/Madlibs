import os 
print(
    '''
>>> choose one of this titles :
        1_ computer
        2_ programming language
        3_ metasploit
        4_ android 
        5_ kaliLinux
    '''
)
a = str(input(">>>"))

f = open("computer.py" , "r")
if a == "1": 
    os.system("python3 computer.py")
elif a == "2": 
    os.system("python3 programmingLanguage.py")
elif a == "3":
    os.system("python3 metasploit.py")
elif a == "4":
    os.system("python3 android.py")
elif a == "5":
    os.system("python3 kaliLinux.py")
    
b = str(input('''>>> do you want to try the other titles [y/n] :'''
    ))
if b == "y" :
    os.system("python3 madlibs1.py")
elif b =="n" :
    print("thank you for playing my game ^^ ")
