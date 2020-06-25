

import random
def loop():
     words = ["wednesday","people","car","goblin","dragon","toradora","google","terminal","windows"]
     RandomW = random.choice(words)
     cont = 0
     Cont_Run = 0


     NRandomW = len(RandomW)
     print(RandomW)
     User = input("Choose a random letter: ")
     PLetter = int(RandomW.find(User))
     print("letter selected is position number:", PLetter)

     if PLetter == 0:
        print(RandomW[PLetter], end="")
        while cont != NRandomW:
            print("_ ", end="")
            cont += 1
     if PLetter == NRandomW:
        print(RandomW[PLetter], end="")
        while cont != NRandomW:
            print("_ ", end="")
            cont += 1

     while cont < PLetter:
        Cont_Run += 1
        print("_ ", end="")
        cont += 1
        if cont == PLetter:
            print(RandomW[PLetter], "_ ", end="")
            cont += 1
            while cont != NRandomW:
                print("_ ", end="")
                cont += 1


print(loop())
