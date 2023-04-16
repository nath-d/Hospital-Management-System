cardName = []
cardAge = []
cardSex = []
cardNum = []

neuroName = []
neuroAge = []
neuroSex = []
neuroNum = []

orthoName = []
orthoAge = []
orthoSex = []
orthoNum = []


def cardio():
    global counterCard
    global cardName
    global cardAge
    global cardSex
    global cardNum

    while True:
        inputs()
        cardName.append(name)
        cardAge.append(age)
        cardSex.append(sex)
        cardNum.append(num)
        if check == '0':
            break

    menu_2()
    print("")


def neuro():
    global counterNeuro
    global neuroName
    global neuroAge
    global neuroSex
    global neuroNum

    while True:
        inputs()
        neuroName.append(name)
        neuroAge.append(age)
        neuroSex.append(sex)
        neuroNum.append(num)
        if check == '0':
            break

    menu_2()
    print("")


def ortho():
    global counterOrtho
    global orthoName
    global orthoAge
    global orthoSex
    global orthoNum

    orthoName = []
    orthoAge = []
    orthoSex = []
    orthoNum = []
    while True:
        inputs()
        orthoName.append(name)
        orthoAge.append(age)
        orthoSex.append(sex)
        orthoNum.append(num)
        if check == '0':
            break

    menu_2()
    print("")


def menu():
    print(" ")
    print("\n\t\t           ......  SELECT CATEGORY  ......\n")
    print("\t\t    *********************************************  \t\t"
          "\n\t\t    *\t\t                    \t\t*"
          "\n\t\t    *\t\t  1. Cardiology     \t\t*"
          "\n\t\t    *\t\t  2. Neurosurgery   \t\t*"
          "\n\t\t    *\t\t  3. Orthopaedic    \t\t*"
          "\n\t\t    *\t\t  4. Menu           \t\t*"
          "\n\t\t    *\t\t                    \t\t*"
          "\n\t\t    *********************************************  \t\t")


def menu_2():
    print(" ")
    print("\t\t    ***************************************************** \t\t"
          "\n\t\t    *\t\t                                 \t*"
          "\n\t\t    *\t\t1. Input Records                 \t*"
          "\n\t\t    *\t\t2. Display Records by Category   \t*"
          "\n\t\t    *\t\t3. Display All Records           \t*"
          "\n\t\t    *\t\t                                 \t*"
          "\n\t\t    *****************************************************  \t\t")

    menuInp = input("Enter choice: ")
    print(" ")

    if menuInp == '1':
        menu()
        catInp = input("\nSelect Category:  ")
        if catInp == '1':
            cardio()
        elif catInp == '2':
            neuro()
        elif catInp == '3':
            ortho()
        elif catInp == '4':
            menu_2()
        else:
            print("Wrong Input...")
    elif menuInp == '2':
        menu()
        ctr = int(input("Enter choice: "))
        if ctr == 1:
            print("Serial", "\t\t", "Name", "\t\t", "Age", "\t\t", "Sex", "\t\t", "Number", "\n")
            i = 0
            while i < len(cardName):
                print(i + 1, "\t\t", cardName[i], "\t\t", cardAge[i], "\t\t", cardSex[i], "\t\t", cardNum[i])
                i += 1
            menu_2()

        elif ctr == 2:
            print("Serial", "\t\t", "Name", "\t\t", "Age", "\t\t", "Sex", "\t\t", "Number", "\n")
            i = 0
            while i < len(neuroName):
                print(i + 1, "\t\t", neuroName[i], "\t\t", neuroAge[i], "\t\t", neuroSex[i], "\t\t", neuroNum[i])
                i += 1
            menu_2()
        elif ctr == 3:
            print("Serial", "\t\t", "Name", "\t\t", "Age", "\t\t", "Sex", "\t\t", "Number", "\n")
            i = 0
            while i < len(orthoName):
                print(i + 1, "\t\t", orthoName[i], "\t\t", orthoAge[i], "\t\t", orthoSex[i], "\t\t", orthoNum[i])
                i += 1
            menu_2()
        elif ctr == 4:
            menu_2()
        else:
            print("Wrong Input...")
    elif menuInp == '3':
        globalInput()

        menu_2()
    elif menuInp == '4':
        exit()
    else:
        print("Wrong input...")


def inputs():
    global name
    global age
    global sex
    global num
    global check

    name = input("> Enter Name: ")
    age = input("> Enter Age: ")
    sex = input("> Enter Sex: ")
    num = input("> Enter number: ")
    print("\n")
    check = input("--Press any button to Continue\n"
                  "--Press 0 to exit: ")


def globalInput():
    print(" Category ", "   Name", "\t\t", "Age", "\t\t", "Sex", "\t\t", "Number", "\n")
    i = 0
    while i < len(cardName):
        print("Cardiology:  ", cardName[i], "\t\t", cardAge[i], "\t\t", cardSex[i], "\t\t", cardNum[i])
        i += 1
    i = 0
    while i < len(neuroName):
        print("Neurology:   ", neuroName[i], "\t\t", neuroAge[i], "\t\t", neuroSex[i], "\t\t", neuroNum[i])
        i += 1
    i = 0
    while i < len(orthoName):
        print("Orthopaedic:  ", orthoName[i], "\t\t", orthoAge[i], "\t\t", orthoSex[i], "\t\t", orthoNum[i])
        i += 1


menu_2()
