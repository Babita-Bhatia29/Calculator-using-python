a=int(input("enter the number of iteration"))
print("press1 for addition \n press2 for subtraction \n press3 for multiplication \n press 4 for divsion \n press 5 for exponential\n press 6 for floor divsion")
for i in range(a):
    x=int(input("press"))
    if x==1:
        b=eval(input("1st no"))
        c=eval(input("2nd no"))
        y=b+c
        print(y)
    elif x==2:
        b=eval(input("1st no"))
        c=eval(input("2nd no"))
        y=b-c
        print(y)
    elif x==3:
        b=eval(input("1st no"))
        c=eval(input("2nd no"))
        y=b*c
        print(y)     
    elif x==4:
        b=eval(input("1st no"))
        c=eval(input("2nd no"))
        y=b/c
        print(y) 
    elif x==5:
        b=eval(input("1st no"))
        c=eval(input("2nd no"))
        y=b**c
        print(y)
    elif x==6:
        b=eval(input("1st no"))
        c=eval(input("2nd no"))
        y=b//c
        print(y)
    elif x>6:
        print("kyu bhai or kam nhi h")     
    else:
        print("bhai galat jagha aa gye aap")    
                                       