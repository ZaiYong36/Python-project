name = "*****"
pw = "******"
count = 3

while count > 0 :
    name = input("Please enter your name:")
    pw = input("Please enter password:")
    if name == "admin" and pw == "123456":
        break
    elif name == "student" and pw == "123456":
        break
    elif name == "tutor" and pw == "123456":
        break
    elif name == "receptionist" and pw == "123456":
        break
    elif name != "admin" or name != "student" or name != "tutor" or name != "receptionist":
        print("Try again :)")
    count = count - 1

if name == "admin":
    print("""Name: admin \n welcome to admin panel""")
if name == "student":
    print("Name: zai \n Welcome to our new tutor app")
if name == "tutor":
    print("Name: zai \n Welcome to tutor our dear students.")
if name == "receptionist":
    print("Name: zai \n Welcome to our new receptionist panel.")