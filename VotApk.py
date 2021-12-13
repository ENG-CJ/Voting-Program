import Voting



Voting.header()
def voting():
    vot1 = 0
    vot2 = 0
    vot3 = 0
    vot4 = 0
    nation=input('Enter Your Native: ')
    if nation=="somali" or nation=="Somali":
        age=int(input('Enter Your Age: '))
        if age>=18:
            print()
            print('Candidates')
            Voting.candidates()
            vote=input('Vote: ')

        #     Conditions
            if vote=="1":
                vot1+=1
                print('You Votted Mohamed Farmajo')
                print('Voters:',vot1)
            elif vote=="2":
                print('You Votted Hassan Kheyre')
                vot2+=1
                print('Voters:',vot2)

            elif vote=="3":
                print('You Votted Hassan Shiekh')
                vot3+=1
                print('Voters:',vot3)

            elif vote=="4":
                print('You Votted Shiekh Sharif')
                vot4+=1
                print('Voters:',vot4)
            else:
                print('Invalid Selection')

            print()
            print('RESULT'
                  )
            print('Mohamed Farmaajo Got voters:',vot1)
            print('Hassan Ali KHEYRE Got Voters:',vot2)
            print('Shiekh Hassan Voters:',vot3)
            print('Sheikh Sharif Voters:',vot4)



        else:
            print('Your Age Too Low')
    else:
        Voting.validate()

voting()