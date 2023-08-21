import datetime

#All important commands
def removeacc(target):
    with open("login.txt", "r") as rmr:
        lines = rmr.readlines()
        with open("login.txt", "w") as rmv:
            for line in lines:
                if line.find(target) == -1:
                    rmv.write(line)

def addacc(role):
    print("\nAdd new account\n")
    username = input("Username:")
    password = input("Password:")
    with open("login.txt", "a") as add:
        newacc = username + "," + password + "," + role + "\n"
        add.write(newacc)

def admin():
    print('Wlecome')
    print('What would you like to do ?\n1.View\n2.Edit\n3.Update self profile')
    funcadm = int(input('Please choose the function desired via the numbers given: '))
    if funcadm == 1:
        print('What item would you like to read ?\n1.Tutor\n2.Receptionist\n3.Tutor Monthly Income\n4.Back to Main Menu')
        funcadmv = int(input('Please enter the number of the item: '))
        if funcadmv == 1:
            while True:
                with open('TtrLvlSject.txt', 'r') as vwttrlvlsject:
                    vwtline = vwttrlvlsject.readlines()
                    vwtr = input('Please enter the name of the tutor to be viewed :')
                    for line in vwtline:
                            if vwtr in line:
                                print(line)
                                vwttrlvlsject.close()
                cvt = input('Would you like to continue viewing\nYes or No :')
                if cvt.lower() == 'no':
                    admin()
        elif funcadmv == 2:
            while True:
                with open('Receptionist.txt', 'r') as vwrcpt:
                    vwrline = vwrcpt.readlines()
                    vwrp = input('Please enter the name of the receptionist you want to view :')
                    for line in vwrline:
                        if vwrp in line:
                            print(line)
                            vwrcpt.close()
                cvr = input('Would you like to continue\nYes or No :')
                if cvr.lower() == 'no':
                    admin()
        elif funcadmv == 3:
            while True:
                with open('TtrLvlSject.txt', 'r') as ttrinc:
                    tinco = ttrinc.readlines()
                    vtinc = input('Please enter the name of the tutor\'s income you wish to see :')
                    for line in tinco:
                        tico = line.strip().split(',')
                        if vtinc in tico:
                            print(vtinc, '\'s monthly income : RM', int(tico[4])*5000)
                cvti = input('Would you like to continue :\nYes or No :')
                if cvti.lower() == 'no':
                    admin()
        elif funcadmv == 4:
            admin()
    elif funcadm == 2:
        print('Would you like to edit:\n1.Register\n2.Delete\n3.Back to Main Menu')
        funcadme = int(input('Please enter the funtion you would like to proceed with: '))
        if funcadme == 1:
            print('Would you like to register:\n1.Tutor\n2.Receptionist\n3.Back to Main Menu')
            funcadm3 = int(input('Please enter the number of your choice: '))
            if funcadm3 == 1:
                while True:
                    with open('TtrLvlSject.txt', 'a') as tifo:
                        tname = input('Please register your name: ')
                        tphnum = int(input('Please register your phone number: '))
                        tmail = input('Please register your email: ')
                        sject = input('Please register your subject: ')
                        sjlvl = int(input("Please enter the subject's level: "))
                        tfo = tname+','+str(tphnum) + ','+tmail + ',' + sject + ',' + str(sjlvl) + '\n'
                        tifo.write(tfo)
                        tifo.close()
                        print('New Tutor added')
                        cat = input('Would you like to continue ?\nYes or No :')
                        if cat.lower() == 'no':
                            admin()
            elif funcadm3 == 2:
                while True:
                    with open('Receptionist.txt', 'a') as rifo:
                        rname = input('Please register your name: ')
                        rphnum = int(input('Please register your phone number: '))
                        rmail = input('Please register your email: ')
                        rfo = rname+','+str(rphnum) + ','+rmail+'\n'
                        rifo.write(rfo)
                        rifo.close()
                        print('New Receptionist added')
                        car = input('Would you like to continue ?\nYes or No :')
                        if car.lower() == 'no':
                            admin()
            elif funcadm3 == 3:
                admin()
        elif funcadme == 2:
            print('Which category would you like to delete an item in :\n1.Tutor\n2.Receptionist\n3.Back to Main Menu')
            funcadmd = int(input('Please enter the number of the option :'))
            if funcadmd == 1:
                while True:
                    dttr = input('Please enter the name of the tutor to be deleted')
                    with open('TtrLvlSject.txt', 'r') as radttrlvlsject:
                        rtline = radttrlvlsject.readlines()
                        with open('TtrLvlSject.txt', 'w') as dltttr:
                            for line in rtline:
                                if dttr in line:
                                    pass
                                else:
                                    dltttr.write(line)
                            print(dttr, 'Deleted')
                    cdltttr = input('Would you like to continue deleting tutor :\nYes or No :')
                    if cdltttr.lower() == 'no':
                        admin()
            if funcadmd == 2:
                while True:
                    dtrecp = input('Please enter the name of the receptionist to be deleted')
                    with open('Receptionist.txt', 'r') as radrecp:
                        rrline = radrecp.readlines()
                        with open('Receptionist.txt', 'w') as dltrec:
                            for line in rrline:
                                if dtrecp in line:
                                    pass
                                else:
                                    dltrec.write(line)
                            print(dtrecp, 'Deleted')
                    cdltrec = input('Would you like to continue deleting receptionist ?\nYes or No :')
                    if cdltrec.lower() == 'no':
                        admin()
            elif funcadmd == 3:
                admin()
        elif funcadme ==3:
            admin()
    elif funcadm == 3:
        while True:
            with open ('adm.txt','r') as admchce:
                rdadmline = admchce.readlines()
            updtadm = input('Please enter the name of the admin\'s profile to be updated :')
            with open('adm.txt','w') as altadmpf:
                for line in rdadmline:
                    if updtadm in line:
                        nadmnm = input('Please enter your name :')
                        nadmgdr = input('Please enter your gender :')
                        nadmdob = input('Please enter your date of birth with the following format(01 January 2000) :')
                        nadmem = input('Please enter your email :')
                        nadmphnum = input('Please enter your phone number')
                        nadmadrs = input('Please enter your address :')
                        nwadm = f"{nadmnm},{nadmgdr},{nadmdob},{nadmem},{nadmphnum},{nadmadrs}"
                        altadmpf.write(nwadm+'\n')
                    else:
                        altadmpf.write(line)
            calterpf = input('Would you like to continue making changes in admin profile ?\nYes or no')
            if calterpf.lower() == 'no':
                admin()

    admin()



#("Ali", "ali345")
#("Egg", "egg345")
def receptionist():
    print("Welcome to receptionist panel ! ", "\n1.Register and enroll student",
          "\n2.Update student subject enrollment", "\n3.Accept payment from student", "\n4.Delete student",
          "\n5.Update profile", "\n6.Back to login")
    o = input("Please enter the operation you want :")
    if o == "1":
        op1()
    elif o == "2":
        op2()
    elif o == "3":
        op3()
    elif o == "4":
        op4()
    elif o == "5":
        op5()
    elif o == "6":
        print("Back to login")


def op1():
    print("Insert student information")
    with open("rstudent.txt", "a") as r:
        stu_in = input("Enter student name :") + ";" + input("Enter student IC :") + ";" + input(
            "Enter student email address :") + ";" + input("Enter student contact number :") + ";" + input(
            "Enter student address :") + ";" + input("Enter student level :") + ";" + input(
            "Enter student subject 1 (type none1 if no subject):") + ";" + input(
            "Enter student subject 2 (type none2 if no subject):") + ";" + input(
            "Enter student subject 3 (type none3 if no subject):") + ";" + input("Enter month of enrollment :") + "\n"
        r.write(stu_in)
    r.close()
    print("Registered successful.")
    c = input("Back to receptionist panel ?(yes/no):")
    if c == "yes":
        receptionist()
    else:
        print("End of program.")


def op2():
    op = input("Enter name :")
    with open("rstudent.txt", "r") as r:
        for line in r:
            if op in line:
                item = line.strip().split(";")
                print("Subject are :", item[6], item[7], item[8])
                search_text = input("Which subject you want to change :")
                replace_text = input("Enter the subject :")
                with open("rstudent.txt", "r") as file:
                    data = file.read()
                    data = data.replace(search_text, replace_text)
                # Opening our text file in read only mode using the open() function
                # Writing the replaced data in our text file
                with open("rstudent.txt", "w") as f:
                    f.write(data)
                    print("replace text(", search_text, ",", replace_text, ")")
    c = input("Back to receptionist panel ?(yes/no):")
    if c == "yes":
        receptionist()
    else:
        print("End of program.")


def op3():
    op = input("Enter name :")
    with open("payment.txt", "r") as r:
        for line in r:
            if op in line:
                item = line.strip().split(",")
                print("*****Payment receipt*****", "\nStudent name :", item[0], "\nAmount :", item[1], "\nDate :",
                      item[2])


def op4():
    op = input("Enter student name :")
    try:
        with open("recpprof.txt", "r") as r:
            lines = r.readlines()
            with open("recpprof.txt", "w") as r1:
                for line in lines:
                    # strip() is used to remove '\n' present at the end of each line
                    if line.find(op) == -1:
                        r1.write(line)
        print(op, "deleted successful.")
    except op not in "recpprof.txt":
        print("Oops, something error!")

    c = input("Back to receptionist panel ?(yes/no):")
    if c == "yes":
        receptionist()
    else:
        print("End of program.")



def op5():
    op = input("Enter name :")
    with open("recpprof.txt", "r") as r:
        for line in r:
            if op in line:
                item = line.strip().split(",")
                print("Name :", item[0],"\nGender :", item[1],"\nDate of birth :", item[2],"\nEmail :", item[3],"\nIc number :", item[4])
                search_text = input("Enter the part which you want to change :")
                replace_text = input("Replace with :")
                with open("recpprof.txt", "r") as file:
                    data = file.read()
                    data = data.replace(search_text, replace_text)
                # Opening our text file in read only mode using the open() function
                # Writing the replaced data in our text file
                with open("recpprof.txt", "w") as f:
                    f.write(data)
                    print("replace text(", search_text, ",", replace_text, ")")


    c = input("Back to receptionist panel ?(yes/no):")
    if c == "yes":
        receptionist()
    else:
        print("End of program.")





#tutor("Lee", "lee345"),
    #tutor("Leong", "leong345")
def tutor():
    print("Welcome,", name)
    print("1. Add class information\n2. Update or delete class information\n3. View list of student according to subject\n4. Update profile")
    codex = int(input("Please choose option by using number:"))
    #record subject for tutor
    with open("tutorprof.txt", "r") as read:
        lines = read.readlines()
        for line in lines:
            if name in line:
                item = line.strip().split(",")
                sub = item[-1]


    # Dictionary
    tutorconversion = {
        "Chinese": "classschedule.txt",
        "English": "english_class.txt",
        "Malay": "malay_class.txt"
    }

    if codex == 1:
        with open("tutorprof.txt", "r") as read:
            lines = read.readlines()
            for line in lines:
                if name in line:
                    item = line.strip().split(",")
                    while True:
                        #allow teacher to add class information
                        print("\n\nPlease enter following information")
                        with open("classschedule.txt", "a") as admin_prof:
                            new_sub = input("Subject_name:") + "," + input("Charge:") + "," + input(
                                "Class_schedule(day and time):") + "\n"
                            admin_prof.write(new_sub)
                        admin_prof.close()

                        #continue?
                        cont = input("Do you wish to continue modify?(yes/no)")
                        if cont == "no":
                            break
    if codex == 2:
        while True:

            # show schedule
            print("Schedule:")
            with open("classschedule.txt", 'r') as fr:
                # reading line by line
                lines = fr.readlines()
                for line in lines:
                    item = line.strip().split(",")
                    if sub in line:
                        print(item[-1])

            #replace  time
            timi = input("Please enter day and time you want to change:")
            new_timi = input("Please enter new day and time:")
            with open("classschedule.txt", "r") as file:
                data = file.read()
                data = data.replace(timi, new_timi)
            # Opening our text file in read only mode using the open() function
            # Writing the replaced data in our text file
            with open("classschedule.txt", "w") as f:
                f.write(data)
                print("Replaced time successfully!")


            cont = input("Do you wish to continue modify?(yes/no)")
            if cont == "no":
                break

    if codex == 3:
        #show all student in his or her subject
        print(sub)
        print("Students:")
        with open("rstudent.txt","r") as rstudent:
            for line in rstudent:
                if sub in line:
                    item = line.strip().split(";")
                    print(item[0])
        print("\n")

    if codex == 4:




        #print table
        print("\n\n")
        with open("tutorprof.txt", "r") as mir:
            lines = mir.readlines()
            for line in lines:
                if line.find(name) == 0:
                    item = line.strip().split(",")
                    print("Name:", item[0], "\nGender:", item[1], "\nDate of birth:", item[2], "\nEmail:", item[3],
                          "\nContact number:", item[4] , "\nSubject:", item[5])

                    # choice make
                    chc = input("Do you really want to make change?(yes/no)")
                    if chc == "no":
                        break
                    if chc == "yes":
                        with open("tutorprof.txt", "w") as miw:
                            for line in lines:
                                if line.find(name) == -1:
                                    miw.write(line)
                            miw.close()
                        # append
                        with open("tutorprof.txt", "a") as mia:
                            new_prof = "\n" + input("Name:") + "," + input("Gender:") + "," + input(
                                "Date of Birth:") + "," + input("Email address:") + "," + input("Phone number:") + "," + input("Subject:")
                            mia.write(new_prof)
                        mia.close()

                        cont = input("Do you wish to continue modify?(yes/no)")
                        if cont == "no":
                            break


    tutor()


# Amir,amir345,student
# Aik,aik345,student
def student():
    while True:
        print("Welcome, ", name)
        codex = int(input("1. View schedule\n2. Send change subject enrollment request\n3. Delete change subject enrollment request\n4. View payment due\n5. Update profile\nPlease enter the option you want by using number:"))

        if codex == 1:
            # print table function
            def print_schedule(subject):
                with open("classschedule.txt", "r") as read:
                    lines = read.readlines()
                    for line in lines:
                        item = line.strip().split(",")
                        if subject in line:
                            print(item[0], ", ", item[2])

            # find owener's subject
            with open("rstudent.txt", "r") as student:
                for line in student:
                    if name in line:
                        if "Chinese" in line:
                            print_schedule("Chinese")
                        if "English" in line:
                            print_schedule("English")
                        if "Malay" in line:
                            print_schedule("Malay")


            input("Press any key to continue....")

            print("\n")



        if codex == 2:
            with open("request.txt", "a") as rq:
                request = name + ",pending\n"
                rq.write(request)
            rq.close()
            print("\nRequest sent\n")


        if codex == 3:
            try:

                with open("request.txt", 'r') as fr:
                    lines = fr.readlines()

                    with open("request.txt", 'w') as fw:
                        for line in lines:

                            # if no match found, it will return -1
                            if line.find(name) == -1:
                                fw.write(line)
                print("\n", name, "request deleted.")
            except:
                print("Some error has occurred!")
            fr.close()
            fw.close()
            print("\n")


        if codex == 4:
            #function to detect what subject enrolled
            def detect(name):
                list = []
                with open("rstudent.txt","r") as read:
                    for line in read:
                        if name in line:
                            if "Chinese" in line:
                                list.append("Chinese")

                            elif "English" in line:
                                list.append("English")

                            elif "Malay" in line:
                                list.append("Malay")
                return list

            #function to add up all fee
            def calculate(list):
                fee = int(0)
                for sub in list:
                    with open("classschedule.txt", 'r') as fr:
                        lines = fr.readlines()
                        for line in lines:

                            # if no match found, it will return -1
                            if line.find(sub) == 0:
                                item = line.strip().split(",")
                                fee = fee + int(item[1])
                return fee

            with open("rstudent.txt","r") as pay:
                for line in pay:
                    if name in line:
                        item = line.strip().split(";")
                        print(item[0], ": ", item[-2])
                        status = item[-2]

            #show all paid status
            with open("rstudent.txt","r") as read:
                for line in read:
                    if name in line:
                        item = line.strip().split(";")
                        print(item[0] , ": " , item[-1])
                        status = item[-2]
                        amountdue = int(item[-1])
            read.close()

            if status == "paid":
                print("No payment due")

            elif status == "unpaid":
                if amountdue == 0:
                    amountdue = calculate(detect(name))
                    #print amount due
                    print("Amount due:", amountdue)
                    amount = int(input("Please enter the amount you want to pay:"))
                    amountdue = amountdue - amount
                    with open("rstudent.txt", "r") as read:
                        lines = read.readlines()
                        for line in lines:
                            if name in line:
                                data = line
                                data = "\n" + data.replace("0",str(amountdue))
                    with open("rstudent.txt", "w") as rstu:
                        for line in lines:
                            if name in line:
                                pass
                            else:
                                rstu.write(line)
                        rstu.write(data)


                elif amountdue > 0 and status == "unpaid":
                    amount = int(input("Please enter the amount you want to pay:"))
                    amountdue = amountdue - amount
                    if amountdue == 0:

                        with open("rstudent.txt", "r") as read:
                            lines = read.readlines()
                            for line in lines:
                                if name in line:
                                    data = line
                                    data = "\n" + data.replace("unpaid", "paid")
                        with open("rstudent.txt", "w") as rstu:
                            for line in lines:
                                if name in line:
                                    pass
                                else:
                                    rstu.write(line)
                            rstu.write(data)




            #continue payment?
            # choice = input("Do you wish to pay now?(yes/no)")
            # if choice.lower() == "yes":






            # # loop to detect
            # fee = int(0)
            # for item in ["Chinese", "Malay", "English"]:
            #     fee = fee + int(calculate(item))
            # #show amount due
            # print(f"\nAmount due:{fee}\n")
            #
            # #payment
            # from datetime import date
            # choice = input("Do you want to pay now?(yes/no)")
            # if choice == "yes":
            #     amount = int(input("Please enter the amount you want to pay:"))
            #     fee = fee - amount
            #     with open("payment.txt", "a") as py:
            #         payment = name + "," + str(amount) + "," + str(date.today()) + "\n"
            #     print(f"\nAmount due:{fee}\n")

            print("\n")

        if codex == 5:
            # print table
            print("\n\n")
            with open("studentprof.txt", "r") as mir:
                lines = mir.readlines()
                for line in lines:
                    if line.find(name) == 0:
                        item = line.strip().split("-")
                        print("Name:", item[0], "\nIC/Passport number:", item[1], "\nEmail:", item[2],
                              "\nPhone number:", item[3],
                              "\nAddress:", item[4])

                        # choice make
                        chc = input("Do you really want to make change?(yes/no)")
                        if chc == "no":
                            break
                        if chc == "yes":
                            with open("studentprof.txt", "w") as miw:
                                for line in lines:
                                    if line.find(name) == -1:
                                        miw.write(line)
                                miw.close()
                            # append
                            with open("studentprof.txt", "a") as mia:
                                new_prof = "\n" + input("Name:") + "," + input("IC/Passport number:") + "," + input(
                                    "Email:") + "," + input("Phone number:") + "," + input("Address:")
                                mia.write(new_prof)
                            mia.close()

                            cont = input("Do you wish to continue modify?(yes/no)")
                            if cont == "no":
                                break
                mir.close()
            print("\n")


# attempt loop and login
count = 3
while count > 0:
    name = input("Please enter your name:")
    pw = input("Please enter password:")
    with open("login.txt", "r") as lg:
        lines = lg.readlines()
        for line in lines:
            nm, passw, role = line.strip().split(",")
            if name == nm and pw == passw and role == "admin":
                lg.close()
                admin()
                count = 4
            elif name == nm and pw == passw and role == "receptionist":
                lg.close()
                receptionist()
                count = 4
            elif name == nm and pw == passw and role == "tutor":
                lg.close()
                tutor()
                count = 4
            elif name == nm and pw == passw and role == "student":
                lg.close()
                student()
                count = 4
    count = count - 1
    print("Current attempts left:", count)

if count == 0:
    print("Please rerun this program to get more attempts :)")








