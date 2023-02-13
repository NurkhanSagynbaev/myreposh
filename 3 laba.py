import string

txt = str(input("TXT: "))
isup = 0
islo = 0
for i in txt:
    if i.isupper():
        isup+=1
    if i.islower():
        islo+=1

if isup>islo:
    print(txt.upper())
else :
    print(txt.lower())

booling = 1
while(booling):
    s1 = str(input("1 san: "))
    s2 = str(input("2 san: "))
    if(s1.isdigit() and s2.isdigit()):
        print(int(s1) + int(s2))
        print("CONTINUE?")
        
        slovo = str(input())
        if slovo == "NO":
            booling = 0
    else:
        print("Sandy kayta jaz!!!")
