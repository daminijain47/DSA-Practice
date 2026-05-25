no=int(input("Enter mobile number: "))

if no.isdigit():
    if len(no)==10:
        print("Number is valid ")

        if no.startswith(("6", "7", "8", "9")):
            print("Number valid in India ")
        else:
            print("Number not valid in India ")
    
    else: 
        print("Number is not valid ")
    
else:
    print("Not in digit")
# check number is number not a char
# (6.7.8.9) 6 or 7 or 8 or 
# .is digit , 
#1 insertion order preseve and duplicate values allowed then go for list 
#set mai ulta hai iska 
no = input("Enter mobile number: ")

if no.isdigit():

    if len(no) == 10:
        print("Number is valid")

        if no.startswith(("6", "7", "8", "9")):
            print("Number valid in India")

        else:
            print("Number not valid in India")

    else:
        print("Number is not valid")

else:
    print("Not in digit")