import random 

'''
0 for rock
1 for paper
2 for scissor

'''
computer=random.choice([0,1,2])
mein = input("Enter ur choice:")
medic = { "r":0 , "p":1 , "s":2}
reversedict={ 0:"rock", 1:"paper" , 2:"scissor"}

me=medic[mein]

print(f"you chose:{reversedict[me]}\ncomputer have chose:{reversedict[computer]}")

if(computer == me):
    print("its a draw")

else:
    if(computer==0 and me==1):
        print("u won")
    elif(computer==0 and me==2):
        print("u lost")
    elif(computer==1 and me==0):
        print("u lost")
    elif(computer==1 and me==2):
        print("u won")
    elif(computer==2 and me==0):
        print("u won")
    elif(computer==2 and me==1):
        print("u lost")
    else:
        print("something is wrong")


