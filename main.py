import random

def main():
    print("========================")
    print("====GUESS THE NUMBER====")
    print("========================")

    low_num = 1
    high_num = 100
    print(f"Select a number between {low_num} and {high_num}")

    attempt = 0
    secret_guess = random.randint(1, 100)
    is_running = True

    while is_running:
        answer = input("Masukan Tebakanmu:")
        
        if not answer.isdigit():
            print(f"Please input the valid number between ({low_num},{high_num})")
            continue
            
        answer = int(answer)
        attempt += 1

        if answer < secret_guess:
            print("Too Low, Try Again")
            continue

        if answer > secret_guess:
            print("Too High, Try Again")
            continue

        print(f"Correct, the number is {secret_guess}")
        print("Attempt: ", attempt)
        is_running = False




if __name__ =="__main__":
    main()


