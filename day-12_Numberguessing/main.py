from random import randint

EASY_LEVEL_TURNS = 10 #Global variables
HARD_LEVEL_TURNS = 5

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1,100)
    print(f"Psst , the correct answer is {answer}")

    def check_answer(user_guess,actual_guess,turns):
        if user_guess < actual_guess:
            print("Too low .")
            return turns -1
        elif user_guess > actual_guess:
            print("Too High.")
            return turns - 1
        else:
            print(f"You got it! The answer was {actual_guess}")

    def set_difficulty():
        level = input("Choose a difficulty.Type 'easy' or 'hard' : ").lower()
        if level == 'easy':
          return EASY_LEVEL_TURNS
        else :
           return HARD_LEVEL_TURNS


    turns = set_difficulty()
    print(f"You have {turns} attempts remaining to guess the number")

    guess=0
    while guess != answer:
        guess = int(input("Make a guess :"))
        turns=check_answer(guess,answer,turns)

game()




