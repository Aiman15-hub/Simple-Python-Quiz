
q={
   'html=':'hyper text markup language',
   '3+4=':'7',
   '1+9=':'10',
   'who is the leader of BTS=':'rm'
   }

def welcome():
    print("Welcome to quiz")
    score=0
    for qi,ans in q.items():
        print(qi)
        userinp=input("Enter the Answer:").lower()
        if userinp==ans:
            print("correct!")
            score+=1
            print("you scored:",score)
        else:
            print("incorrect!")
welcome()  

    
        

