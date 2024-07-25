quizes={
    "Q.1 Which is the “most sensitive organ” in our body?":"skin",
    "Q.2 Who wrote “Romeo and Juliet”?":"william shakespeare",
    "Q.3 Who painted the “Mona Lisa”?":"leonardo da vinci",
    "Q.4 What is the smallest “prime number”?":"2",
    "Q.5 What is the “currency of India”?":"rupee",
    "Q.6 What is the “largest desert in the world”?":"antarctica",
    "Q.7 Who was the “first man to step on the moon”?":"neil armstrong",
    "Q.8 What is the “largest bird in the world”?":"ostrich",
    "Q.9 Who is known as the “Father of Computers”?":"charles babbage",
    "Q.10 In which year did “World War II end”?":"1945"

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
            print("Incorrect ! correct Answer is ",quizes[i]);
            print("Your score:",score);
    print("congrats ! your Score is:",score);
opinion=input("Do you want to play Quize ('enter yes or no'):")
if(opinion.lower()=='yes'):
    print("let's play");
    Quiz()
else:
    exit()
