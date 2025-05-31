import random
secret_guess = random.randint(1, 100)

if __name__ =="__main__":
    print("WELCOME ON GUESS THE NUMBER")
    print("select a number between 1 and 100")
 
    answer = input("Masukan Tebakanmu: ")

    if answer.isdigit():
        answer = int(answer)
        print("answer is digit")
        if answer < secret_guess:
            print("Too Low")

        elif answer > secret_guess:
            print("Too High")
        
    print(answer)
