from datetime import date

#All important commands
def removeacc(target):
    with open("login.txt", "r") as rmr:
        lines = rmr.readlines()
        with open("login.txt", "w") as rmv:
            for line in lines:
                item = line.strip().split(",")
                if target != item[0]:
                    rmv.write(line)

def addacc(username, password, role):
    with open("login.txt", "a") as add:
        newacc = username + "," + password + "," + role + "\n"
        add.write(newacc)

#check variable can be integer or not
def check_int(variable,ques):
    try:
        variable = int(input(ques))
        return variable
    except:
        print("\n------------------------\nError input.\n------------------------")

def welcome(name):
    print('---------------------------------------\nWelcome,', name, "\n---------------------------------------")

#login credential:
#Bob,bob123
#Jane,Jane345
def admin(name):
    while True:
        welcome(name)
        print('What would you like to do ?\n1.View\n2.Edit\n3.Update self profile\n4.Log out')
        funcadm = ""
        funcadm = check_int(funcadm,'Please choose the function desired via the numbers given: ')

        if funcadm == 1:
            while True:
                print('-----------------------------------\nWhat item would you like to read ?\n1.Tutor\n2.Receptionist\n3.Tutor Monthly Income\n4.Back to Main Menu')
                funcadmv = ""
                funcadmv = check_int(funcadmv, 'Please enter the number of the item: ')

                if funcadmv == 1:
                    while True:
                        with open('tutorprof.txt', 'r') as vwttrlvlsject:
                            vwtline = vwttrlvlsject.readlines()
                            for line in vwtline:
                                try:
                                    item = line.strip().split(",")
                                    tutor_info = "Name :"  + item[0] + '\nGender : ' +  item[1]  + '\nDate of Birth :' + item[2] + '\nEmail :' + item[3] + '\nPhone Number :' + item[4] + '\nSubject :' + item[5] + '\nLevel :' + item[6] + '\n------------------------------'
                                    print(tutor_info)
                                except:
                                    pass
                        cvt = input('Would you like to continue viewing\nYes or No :')
                        if cvt.lower() == 'no':
                            break
                    admin(name)

                elif funcadmv == 2:
                    while True:
                        with open('recpprof.txt', 'r') as vwrcpt:
                            vwrline = vwrcpt.readlines()
                            for line in vwrline:
                                try:
                                    vritem = line.strip().split(",")
                                    print(f"Name :{vritem[0]}\nGender :{vritem[1]}\nDate of Birth :{vritem[2]}\nEmail :{vritem[3]}\nPhone Number :{vritem[4]}\n------------------------------")
                                except:
                                    pass
                        cvr = input('Would you like to continue\nYes or No :')
                        if cvr.lower() == 'no':
                            break
                    admin(name)

                elif funcadmv == 3:
                    print("---------------------------------------------")
                    while True:
                        with open('tutorprof.txt', 'r') as ttrinc:
                            tinco = ttrinc.readlines()
                            for line in tinco:
                                try:
                                    tico = line.strip().split(',')
                                    print(tico[0], '\'s monthly income : RM', int(tico[6])*1000, "\n---------------------------------------------")
                                except:
                                    pass
                        cvti = input('Would you like to continue :\nYes or No :')
                        if cvti.lower() == 'no':
                            break
                    admin(name)
                elif funcadmv == 4:
                    break
        elif funcadm == 2:
            print('---------------------------------\nWould you like to edit:\n1.Register\n2.Delete\n3.Back to Main Menu')
            funcadme = ""
            funcadme = check_int(funcadme, 'Please enter the number of the item: ')

            #register
            if funcadme == 1:
                print('---------------------------------------------\nWould you like to register:\n1.Tutor\n2.Receptionist\n3.Back to Main Menu')
                funcadm3 = ""
                funcadm3 = check_int(funcadm3, 'Please enter the number of your choice: ')

                if funcadm3 == 1:
                    while True:
                        with open('tutorprof.txt', 'a') as tifo:
                            tname = input('Please register his/her name: ')
                            passw = input('Please enter password for account:')
                            #Data validations
                            while True:
                                try:
                                    tphnum = int(input('Please register your phone number: '))
                                    break
                                except:
                                    print("Incorrect data input.")
                            while True:
                                try:
                                    sjlvl = int(input("Please enter the subject's level: "))
                                    break
                                except:
                                    print("Incorrect data input.")

                            tmail = input('Please register your email: ')
                            sject = input('Please register your subject: ').lower()
                            tfo = tname+','+str(tphnum) + ','+tmail + ',' + sject + ',' + str(sjlvl) + '\n'
                            tifo.write(tfo)
                            tifo.close()

                            # add account for new tutor
                            addacc(tname,passw,"tutor")

                            print('New Tutor added')
                            cat = input('Would you like to continue ?\nYes or No :')
                            if cat.lower() == 'no':
                                break
                    admin(name)
                elif funcadm3 == 2:
                    while True:
                        with open('recpprof.txt', 'a') as rifo:
                            rname = input('Please register your name: ')
                            passw = input('Please enter password for account:')
                            while True:
                                try:
                                    rphnum = int(input('Please register your phone number: '))
                                    break
                                except:
                                    print("Incorrect data input.")
                            rmail = input('Please register your email: ')
                            rfo = rname+','+str(rphnum) + ','+rmail+'\n'
                            rifo.write(rfo)
                            rifo.close()

                            # add account for new receptionist
                            addacc(rname, passw, "receptionist")

                            print('New Receptionist added')
                            car = input('Would you like to continue ?\nYes or No :')
                            if car.lower() == 'no':
                                admin(name)
                elif funcadm3 == 3:
                    admin(name)

            #delete
            elif funcadme == 2:
                print('Which category would you like to delete an item in :\n1.Tutor\n2.Receptionist\n3.Back to Main Menu')
                funcadmd = int(input('Please enter the number of the option :'))

                if funcadmd == 1:
                    while True:
                        dttr = input('Please enter the name of the tutor to be deleted :')
                        with open('tutorprof.txt', 'r') as radttrlvlsject:
                            rtline = radttrlvlsject.readlines()
                            with open('tutorprof.txt', 'w') as dltttr:
                                for line in rtline:
                                    if dttr in line:
                                        pass
                                    else:
                                        dltttr.write(line)

                                #remove account
                                removeacc(dttr)
                                print(dttr, 'Deleted')
                        cdltttr = input('Would you like to continue deleting tutor :\nYes or No :')
                        if cdltttr.lower() == 'no':
                            admin(name)
                if funcadmd == 2:
                    while True:
                        dtrecp = input('Please enter the name of the receptionist to be deleted :')
                        with open('Receptionist.txt', 'r') as radrecp:
                            rrline = radrecp.readlines()
                            with open('Receptionist.txt', 'w') as dltrec:
                                for line in rrline:
                                    if dtrecp in line:
                                        pass
                                    else:
                                        dltrec.write(line)
                                #remove account
                                removeacc(dtrecp)
                                print(dtrecp, 'Deleted')
                        cdltrec = input('Would you like to continue deleting receptionist ?\nYes or No :')
                        if cdltrec.lower() == 'no':
                            admin(name)
                elif funcadmd == 3:
                    admin(name)
            elif funcadme ==3:
                admin(name)
        elif funcadm == 3:
            while True:
                with open("adminprof.txt", "r") as read:
                    for line in read:
                        if name in line:
                            try:
                                item = line.strip().split(",")
                                print("----------------------------------------------\nName:", item[0], "\nDate of Birth:", item[1], "\nEmail:", item[2],
                                      "\nPhone number:", item[3])
                            except:
                                pass

                # choice make
                chc = input("Do you really want to make change?(yes/no) :")
                if chc == "no":
                    break
                if chc == "yes":
                    with open ('adminprof.txt','r') as admchce:
                        rdadmline = admchce.readlines()
                    with open('adminprof.txt','w') as altadmpf:
                        for line in rdadmline:
                            if name in line:
                                nadmgdr = input('Please enter your gender :')
                                nadmdob = input('Please enter your date of birth with the following format(01 January 2000) :')
                                nadmem = input('Please enter your email :')
                                nadmphnum = input('Please enter your phone number')
                                nwadm = f"{name},{nadmgdr},{nadmdob},{nadmem},{nadmphnum}"
                                altadmpf.write(nwadm+'\n')
                            else:
                                altadmpf.write(line)
                calterpf = input('Would you like to continue making changes in admin profile ?\nYes or no :')
                if calterpf.lower() == 'no':
                    break
            admin(name)
        elif funcadm == 4:
            break
    login()



#("Ali", "ali345")
#("Egg", "egg345")
def receptionist(name):
    welcome(name)
    print("Welcome to receptionist panel!\n-----------------------------------------\nWhat would you like to do?\n1.Register and enroll student",
          "\n2.Update student subject enrollment", "\n3.Accept payment from student", "\n4.Delete student",
          "\n5.Update profile", "\n6.Check request ", "\n7.Back to login")
    o = input("Please enter the operation you want :")
    if o == "1":
        op1(name)
    elif o == "2":
        op2(name)
    elif o == "3":
        op3(name)
    elif o == "4":
        op4(name)
    elif o == "5":
        op5(name)
    elif o == "6":
        op6(name)
    elif o == "7":
        login()
    else:
        receptionist(name)


def op1(name):
    print("Insert student information")
    with open("rstudent.txt", "a") as r:
        username = input("Enter student name :")
        stu_in = username + ";" + input("Enter student IC :") + ";" + input(
            "Enter student email address :") + ";" + input("Enter student contact number :") + ";" + input(
            "Enter student address :") + ";" + input("Enter student level :") + ";" + input(
            "Enter student subject 1 (type None1 if no subject):").capitalize() + ";" + input(
            "Enter student subject 2 (type None2 if no subject):").capitalize() + ";" + input(
            "Enter student subject 3 (type None3 if no subject):").capitalize() + ";" + input("Enter month of enrollment :") + ";unpaid;0\n"
        r.write(stu_in)
    r.close()
    passw = input("Please enter password for account creation:")
    addacc(username,passw,"student")
    print("Registered successful.")
    c = input("Back to receptionist panel ?(yes/no):").lower()
    if c == "yes":
        receptionist(name)
    else:
        op1(name)


def op2(name):
    with open("rstudent.txt", "r") as r:
        for line in r:
            item = line.strip().split(";")
            print(item[0])
    op = input("Please enter name of the student:")
    with open("rstudent.txt", "r") as r:
        for line in r:
            item = line.strip().split(";")
            if op == item[0]:
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
                    print("replace text(", search_text, "to ", replace_text, ")")
    c = input("Back to receptionist panel ?(yes/no):").lower()
    if c == "yes":
        receptionist(name)
    else:
        op2(name)


def op3(name):
    print("-----------------------------------------")
    with open("payment.txt", "r") as r:
        for line in r:
            item = line.strip().split(",")
            print("Payment from", item[0] + ":" + item[1])
    print("-----------------------------------------")
    op = input("Enter name you want to generate receopt:")
    with open("payment.txt", "r") as r:
        for line in r:
            if op in line:
                item = line.strip().split(",")
                print("*****Payment receipt*****", "\nStudent name :", item[0], "\nAmount :", item[1], "\nDate :",
                      item[2])
    #delete payment record option
    delete = input("Do you want to delete this payment record?(yes/no)").lower()
    if delete == "yes":
        try:
            with open("payment.txt", "r") as r:
                lines = r.readlines()

                with open("payment.txt", "w") as r1:
                    for line in lines:
                        # strip() is used to remove '\n' present at the end of each line
                        if line.find(op) == -1:
                            r1.write(line)
                    print(op, "deleted successful.")
        except:
            print("Oops, something error!")

    #back to receptionist
    c = input("Back to receptionist panel ?(yes/no):").lower()
    if c == "yes":
        receptionist(name)
    else:
        op3(name)


def op4(name):
    with open("rstudent.txt", "r") as r:
        for line in r:
            item = line.strip().split(";")
            print(item[0])
    op = input("Enter student name that you want to delete:")
    try:
        with open("rstudent.txt", "r") as r:
            lines = r.readlines()

            with open("rstudent.txt", "w") as r1:
                for line in lines:
                    item = line.strip().split(";")
                    # strip() is used to remove '\n' present at the end of each line
                    if op != item[0]:
                        r1.write(line)

            print(op, "deleted successful.")
    except:
        print("Oops, something error!")
    # remove student account
    removeacc(op)

    c = input("Back to receptionist panel ?(yes/no):").lower()
    if c == "yes":
        receptionist(name)
    else:
        op4(name)



def op5(name):
    op = name
    with open("recpprof.txt", "r") as r:
        for line in r:
            if op in line:
                item = line.strip().split(",")
                print("Name :", item[0],"\nGender :", item[1],"\nDate of birth :", item[2],"\nEmail :", item[3],"\nIc number :", item[4])
                search_text = input("Enter the part which you want to change(enter the data in the field):")
                replace_text = input("Replace with :")
                with open("recpprof.txt", "r") as file:
                    data = file.read()
                    data = data.replace(search_text, replace_text)
                # Opening our text file in read only mode using the open() function
                # Writing the replaced data in our text file
                with open("recpprof.txt", "w") as f:
                    f.write(data)
                    print("Replaced text from ", search_text, "to", replace_text)

    c = input("Back to receptionist panel ?(yes/no):").lower()
    if c == "yes":
        receptionist(name)
    else:
        op5(name)

def op6(name):
    with open("request.txt", "r")as r:
        for line in r:
            try:
                item = line.strip().split(";")
                print("Request from", item[0], ":", item[1])
            except:
                pass
    op = input("which student you want to delete :")
    try:
        with open("request.txt", "r") as r:
            lines = r.readlines()
            with open("request.txt", "w") as r1:
                for line in lines:
                    item = line.strip().split(";")
# strip() is used to remove '\n' present at     the end of each line
                    if op != item[0]:
                        r1.write(line)
        print(op, "deleted successful.")

    except:
        print("Oops, something error!")

    c = input("Back to receptionist panel ?(yes/no):").lower()
    if c == "yes":
        receptionist(name)
    else:
        op6(name)






#tutor("Lee", "lee345"),
    #tutor("Leong", "leong345")
def tutor(name):
    welcome(name)
    print("1. Add class information\n2. Update or delete class information\n3. View list of student according to subject\n4. Update profile\n5. Log out")
    codex = ""
    codex = check_int(codex,"Please choose option by using number:")
    #record subject for tutor
    with open("tutorprof.txt", "r") as read:
        lines = read.readlines()
        for line in lines:
            if name in line:
                item = line.strip().split(",")
                sub = item[-2]

    if codex == 1:
        tutorop1(name)
    elif codex == 2:
        tutorop2(sub)

    elif codex == 3:
        tutorop3(sub)

    elif codex == 4:
        tutorop4(name)

    elif codex == 5:
        login()

    tutor(name)

def tutorop1(name):
    with open("tutorprof.txt", "r") as read:
        lines = read.readlines()
        for line in lines:
            if name in line:
                item = line.strip().split(",")
                while True:
                    # allow teacher to add class information
                    print("\n\nPlease enter following information")
                    with open("classschedule.txt", "a") as admin_prof:
                        new_sub = input("Subject_name:").capitalize() + "," + input("Charge:") + "," + input(
                            "Please enter class_schedule in this format(wed 6.00pm-7.00pm):").lower() + "," + input(
                            "Subject level:") + "\n"
                        admin_prof.write(new_sub)
                    admin_prof.close()

                    # continue?
                    cont = input("Do you wish to continue modify?(yes/no)")
                    if cont == "no":
                        break

def tutorop2(sub):
    code = ""
    code = check_int(code,"----------------------------------------\n1.Update class information\n2.Delete class information\nPlease choose the operation by using number:")
    if code == 1:
        while True:

            # show schedule
            print("Schedule and level:")
            with open("classschedule.txt", 'r') as fr:
                # reading line by line
                lines = fr.readlines()
                for line in lines:
                    item = line.strip().split(",")
                    if sub in line:
                        print(item[-2] + "," + item[-1])

            # replace  time
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

    if code == 2:
        while True:
            # show schedule
            print("Schedule and level:")
            with open("classschedule.txt", 'r') as fr:
                # reading line by line
                lines = fr.readlines()
                for line in lines:
                    item = line.strip().split(",")
                    if sub in line:
                        print(item[-2] + "," + item[-1])

            # delete  time
            timi = input("Please enter the schedule you want to delete:")
            with open("classschedule.txt", "r") as file:
                lines = file.readlines()

                with open("classschedule.txt", "w") as f:
                    for line in lines:
                        if timi not in line:
                            f.write(line)
                print("Deleted schedule successfully!")

            cont = input("Do you wish to continue delete?(yes/no)")
            if cont == "no":
                break

def tutorop3(sub):
    # show all student in his or her subject
    print("Students:")
    with open("rstudent.txt", "r") as rstudent:
        for line in rstudent:
            if sub in line:
                item = line.strip().split(";")
                print(item[0])

def tutorop4(name):
    # print table
    print("\n\n")
    with open("tutorprof.txt", "r") as mir:
        lines = mir.readlines()
        for line in lines:
            if line.find(name) == 0:
                item = line.strip().split(",")
                print("Profile:\nName:", item[0], "\nGender:", item[1], "\nDate of birth:", item[2], "\nEmail:",
                      item[3],
                      "\nContact number:", item[4], "\nSubject:", item[5], "\nLevel:", item[6])

                # choice make
                chc = input("Do you really want to make change?(yes/no)")
                if chc == "no":
                    break
                if chc == "yes":
                    with open("tutorprof.txt", "w") as miw:
                        for line in lines:
                            if line.find(name) == -1:
                                miw.write(line)
                            elif name in line:
                                new_prof = input("Name:") + "," + input("Gender:") + "," + input(
                                    "Date of Birth:") + "," + input("Email address:") + "," + input(
                                    "Phone number:") + "," + input("Subject:") + "," + input("Level:") + "\n"
                                miw.write(new_prof)
                        miw.close()

                    cont = input("Do you wish to continue modify?(yes/no)")
                    if cont == "no":
                        break

# Muhammad Amir Yong,amir345
# Tan Aik Bah,aik345
def student(name):
    welcome(name)
    codex = ""
    codex = check_int(codex,"1. View schedule\n2. Send change subject enrollment request\n3. Delete change subject enrollment request\n4. View payment due\n5. Update profile\n6. Log out\nPlease enter the option you want by using number:")
    with open("rstudent.txt", "r") as rstu:
        for line in rstu:
            item = line.strip().split(";")
            if name == item[0]:
                level = item[5]

    if codex == 1:
        studentop1(name,level)

    elif codex == 2:
        studentop2(name)

    elif codex == 3:
        studentop3(name)

    elif codex == 4:
        studentop4(name)

    elif codex == 5:
        studentop5(name)

    elif codex == 6:
        login()

    student(name)

def studentop1(name,level):
    print("Schedule:")

    # print table function
    def print_schedule(subject, level):
        with open("classschedule.txt", "r") as read:
            lines = read.readlines()
            for line in lines:
                item = line.strip().split(",")
                if subject in line:
                    if level == item[-1]:
                        print(item[0], ", ", item[2], "Level: " + item[-1])

    # find owener's subject
    with open("rstudent.txt", "r") as student:
        for line in student:
            if name in line:
                list = line.strip().split(";")
                if "Chinese" in line:
                    print_schedule("Chinese", level)
                elif "English" in line:
                    print_schedule("English", level)
                elif "Malay" in line:
                    print_schedule("Malay", level)

    input("Press any key to continue....")

    print("\n")

def studentop2(name):
    with open("request.txt", "a") as rq:
        requestsub = input("Please tell the receptionist that you want to change which subject to which subject:")
        request = name + ";" + requestsub + "\n"
        rq.write(request)
    rq.close()
    print("\nRequest sent\n")

def studentop3(name):
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

def studentop4(name):
    # function to detect what subject enrolled
    def detect(name):
        list = []
        with open("rstudent.txt", "r") as read:
            for line in read:
                if name in line:
                    if "Chinese" in line:
                        list.append("Chinese")

                    if "English" in line:
                        list.append("English")

                    if "Malay" in line:
                        list.append("Malay")
        return list

    # function to add up all fee
    def calculate(list):
        with open("rstudent.txt", "r") as rstu:
            for line in rstu:
                item = line.strip().split(";")
                if name == item[0]:
                    level = item[5]
        fee = int(0)
        for sub in list:
            with open("classschedule.txt", 'r') as fr:
                lines = fr.readlines()
                for line in lines:
                    item = line.strip().split(",")
                    # if no match found, it will return -1
                    if sub in line and level == item[-1] :
                        fee = fee + int(item[1])
        return fee

    # show all paid status
    with open("rstudent.txt", "r") as read:
        for line in read:
            if name in line:
                item = line.strip().split(";")
                print("---------------------------------------\n" + item[0] + ": ", item[-2])
                status = item[-2]
                amountdue = int(item[-1])

    if status == "paid":
        print("-----------------------------------\nNo payment due\n-----------------------------------")

    elif status == "unpaid" and amountdue == 0:
        amountdue = calculate(detect(name))
        # print amount due
        print("Amount due:", amountdue)
        amount = int(input("Please enter the amount you want to pay:"))
        if amount <= amountdue:
            amountdue = amountdue - amount
            # update payment status or amount due in rstudent
            with open("rstudent.txt", "r") as read:
                lines = read.readlines()
                for line in lines:
                    if name in line:
                        data = line
                        data = data.replace("0", str(amountdue))
            with open("rstudent.txt", "w") as rstu:
                for line in lines:
                    if name in line:
                        rstu.write(data)
                    else:
                        rstu.write(line)

            # send a payment record to receptionist
            with open("payment.txt", "a") as pay:
                payrecord = name + "," + str(amount) + "," + str(date.today()) + "\n"
                pay.write(payrecord)

        else:
            print("---------------------------------------\nPlease don't overpay.")

        # change status to paid if amountdue is 0
        if amountdue == 0:
            with open("rstudent.txt", "r") as read:
                lines = read.readlines()
                for line in lines:
                    if name in line:
                        data = line
                        data = data.replace("unpaid", "paid")
            with open("rstudent.txt", "w") as rstu:
                for line in lines:
                    if name in line:
                        rstu.write(data)
                    else:
                        rstu.write(line)

    elif amountdue > 0 and status == "unpaid":
        # print amount due
        print("Amount due:", amountdue)
        amount = int(input("Please enter the amount you want to pay:"))

        if amount <= amountdue:
            amountdue = amountdue - amount

            # update amount due in rstudent
            with open("rstudent.txt", "r") as read:
                lines = read.readlines()
                for line in lines:
                    if name in line:
                        item = line.strip().split(";")
                        data = line
                        data = data.replace(item[-1], str(amountdue))
            with open("rstudent.txt", "w") as rstu:
                for line in lines:
                    if name in line:
                        rstu.write(data)
                    else:
                        rstu.write(line)

            if amountdue == 0:
                # update payment status in rstudent
                with open("rstudent.txt", "r") as read:
                    lines = read.readlines()
                    for line in lines:
                        if name in line:
                            data = line
                            data = data.replace("unpaid", "paid")
                with open("rstudent.txt", "w") as rstu:
                    for line in lines:
                        if name in line:
                            rstu.write(data)
                        else:
                            rstu.write(line)

            # send a payment record to receptionist
            with open("payment.txt", "a") as pay:
                payrecord = name + "," + str(amount) + "," + str(date.today()) + "\n"
                pay.write(payrecord)
        else:
            print("---------------------------------------\nPlease don't overpay.")

def studentop5(name):
    # functions to replace item
    def item_replace(ori, modi):

        with open("rstudent.txt", "r") as file:
            data = file.read()
            data = data.replace(ori, modi)
        # Opening our text file in read only mode using the open() function
        # Writing the replaced data in our text file
        with open("rstudent.txt", "w") as f:
            f.write(data)
            print("Replace text(", ori, "to ", modi, ")")

    # print table
    print("\n\n")
    with open("rstudent.txt", "r") as mir:
        lines = mir.readlines()
        for line in lines:
            try:
                item = line.strip().split(";")
            except:
                pass

            if name == item[0]:

                print("Profile:\nName:", item[0], "\nIC/Passport number:", item[1], "\nEmail:", item[2],
                      "\nPhone number:", item[3],
                      "\nAddress:", item[4])

                # choice make
                chc = input("Do you really want to make change?(yes/no)")
                if chc == "no":
                    break
                if chc == "yes":
                    while True:
                        ori = input("Please enter the data you want to change:")
                        modi = input("Please enter data you want to change to:")

                        item_replace(ori, modi)

                        cont = input("Do you wish to continue modify?(yes/no)").lower()
                        if cont == "no":
                            break
                    break

def login():
    count = 3
    while count > 0:
        print("-----------------------------------\n            Login page        \n-----------------------------------")
        name = input("Please enter your name:")
        pw = input("Please enter password:")
        with open("login.txt", "r") as lg:
            for line in lg:
                nm, passw, role = line.strip().split(",")
                if name == nm and pw == passw and role == "admin":
                    admin(name)

                elif name == nm and pw == passw and role == "receptionist":
                    receptionist(name)

                elif name == nm and pw == passw and role == "tutor":
                    tutor(name)

                elif name == nm and pw == passw and role == "student":
                    student(name)

        count -= 1
        print("Current attempts left:", count)
    print("Please rerun this program to get more attempts :)")
    exit()
login()





