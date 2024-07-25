quizes={
    "Which is the most sensitive organ in our body?":"skin"
    }


def Quiz():
    score=0
    for i in quizes:
        print(i)
        answer=input("enter you answer:");
        if(quizes[i]==answer.lower()):
            score+=1
            print("Correct !")
            print("Your score:",score);
        else:
            print("Incorrect !");
            print("Your score:",score);
opinion=input("Do you want to play Quize ('enter yes or no'):")
if(opinion.lower()=='yes'):
    print("let's play");
    Quiz()
else:
    exit()
