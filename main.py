import random 

def main(): 
    print("========================") 
    print("====GUESS THE NUMBER====") 
    print("====Halo, ini kontribusi pertama saya====") 

    # pilih level
    print("pilih level kesulitan:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-500)")

    level = input("Masukan pilihan (1/2/3): ")

    if level == "1":
        low_num, high_num = 1, 50
    elif level == "2":
        low_num, high_num = 1, 100
    elif level == "3":
        low_num, high_num = 1, 500
    else:
        print("input salah, default ke medium (1-100).")
        low_num, high_num = 1, 100

    print(f"Select a number between {low_num} and {high_num}") 

    attempt = 0 
    secret_guess = random.randint(low_num, high_num) 
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
        print("Total Attempt: ", attempt) 
        is_running = False 


if __name__ =="__main__":
    main()

