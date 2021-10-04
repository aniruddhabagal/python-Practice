name = input("Enter a Namenn")


if(len(name)<3):
    print("name must be atleast 3 chars long")

elif(len(name)>50):
    print("Name can be max of 50 chars")
else:
    print("name looks good")
