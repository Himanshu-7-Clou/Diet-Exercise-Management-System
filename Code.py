# re = open("RE.txt",'w')
# rd = open("RD.txt",'w')
# he = open("HE.txt",'w')
# hd = open("HD.txt",'w')
# ve = open("VE.txt",'w')
# vd = open("VD.txt",'w')

def mainfunction():
    def getdate():
        import datetime
        return datetime.datetime.now()

    x = str(getdate())
    print("\n")
    print(" 1 -> Retrieve \n 2 -> Lock \n")
    rl = int(input("Do wanna retrieve or Lock: "))
    print("\n")
    print(" 1 -> Rohan \n 2 -> Himanshu \n 3 -> Vox \n" )
    name = int(input("Choose your number as per your name: "))
    print("\n")
    print(" 1 -> Excercise \n    or \n 2 -> Diet")
    print("\n")
    ED = int(input("Enter the number option: "))
    print("\n")

    def retrieve():
        print("Here's your Data!")
        print("\n")
        if name == 1: 
            if ED == 1:
                with open("RE.txt") as f:
                    print(f.read(100000000))
            elif ED ==2: 
                with open("RD.txt") as f:
                    print(f.read(10000000))
            else: 
                print("Invalid Input")

        elif name == 2: 
            if ED == 1:
                with open("HE.txt") as f:
                    print(f.read(10000000))
            elif ED ==2: 
                with open("HD.txt") as f:
                    print(f.read(10000000))
            else: 
                print("Invalid Input")
        elif name == 3: 
            if ED == 1:
                with open("VE.txt") as f:
                    print(f.read(10000000))
            elif ED ==2: 
                with open("VD.txt") as f:
                    print(f.read(10000000))
            else: 
                print("Invalid Input")
        else: 
            print("invalid input")
    def lock():
        if name == 1: 
            if ED == 1:
                ne = int(input("How many Exercises you have done today Rohan: "))
                print("\n")
                print("Please fill the Exercises you have done!")
                with open("RE.txt","a") as re:
                    re.write(x)
                for i in range(1,ne+1):
                    data1_re = str(input("Exercise "+ str(i) + ": "))
                    with open("RE.txt","a") as re:
                        re.write("\n")
                        re.write(data1_re)
                with open("RE.txt","a") as re:
                    re.write("\n")
                    re.write("\n")
            elif ED == 2:
                nd = int((input("How many times you ate today Rohan: ")))
                print("\n")
                print("Please fill the what you have Ate today!")
                with open("RD.txt","a") as rd:
                    rd.write(x)
                for i in range(1, nd+1):
                    data1_rd = str(input("Food " + str(i) + ": "))
                    with open("RD.txt","a") as rd:
                        rd.write("\n")
                        rd.write(data1_rd)
                with open("RD.txt","a") as rd:
                    rd.write("\n")
                    rd.write("\n")
            else:
                print("Invalid Input")

        elif name ==2:
            if ED == 1:
                ne = int(input("How many Exercises you have done today Himanshu : "))
                print("\n")
                print("Please fill the Exercises you have done!")
                with open("HE.txt","a") as he:
                    he.write(x)
                for i in range(1,ne+1):
                    data1_he = str(input("Exercise "+ str(i) + ": "))
                    with open("HE.txt","a") as he:
                        he.write("\n")
                        he.write(data1_he)
                with open("HE.txt","a") as he:
                    he.write("\n")
                    he.write("\n")
            elif ED == 2:
                nd = int((input("How many times you ate today Himanshu: ")))
                print("\n")
                print("Please fill the what you have Ate today!")
                with open("HD.txt","a") as hd:
                    hd.write(x)
                for i in range(1,nd+1):
                    data1_hd = str(input("Food "+ str(i) + ": "))
                    with open("HD.txt","a") as hd:
                        hd.write("\n")
                        hd.write(data1_hd)
                with open("HD.txt","a") as hd:
                    hd.write("\n")
                    hd.write("\n")
                
            else:
                print("Invalid Input")

        elif name == 3: 
            if ED == 1:
                ne = int(input("How many Exercises you have done today Vox: "))
                print("\n")
                print("Please fill the Exercises you have done!")
                with open("VE.txt","a") as ve:
                    ve.write(x)
                for i in range(1,ne+1):
                    data1_ve = str(input("Exercise "+ str(i) + ": "))
                    with open("VE.txt","a") as ve:
                        ve.write("\n")
                        ve.write(data1_ve)
                with open("VE.txt","a") as ve:
                    ve.write("\n")
                    ve.write("\n")
            elif ED == 2:
                nd = int((input("How many times you ate today Vox?: ")))
                print("\n")
                print("Please fill the what you have Ate today!")
                with open("VD.txt","a") as vd:
                    vd.write(x)
                for i in range(1,nd+1):
                    data1_vd = str(input("Food "+ str(i) + ": "))
                    with open("VD.txt","a") as vd:
                        vd.write("\n")
                        vd.write(data1_vd)
                with open("VD.txt","a") as vd:
                    vd.write("\n")
                    vd.write("\n")
            else: 
                print("Invalid input")
        else:
            print("Invalid input!") 

    if rl == 1: 
        retrieve()
    else: 
        lock()


mainfunction()

print('\n')
print("Do you Want to do it again?")
ask = input("y for Yes & n for No: ")

if ask == "y":
    mainfunction()
elif ask == "n":
    print("Thanks")
    exit()
else: 
    print("invalid input!")
