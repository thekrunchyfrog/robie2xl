from game_setup import *


class Robie2xl:
    def main():
        pass

    # if __name__ == "__main__":
    #    main()


game = GameSetup()
questions = game.get_questions()

score = 0

for question in questions:
    print(question["question"])
    game.read_answers(question)

    guess = input("What is your guess: ")

    game.check_answer(question, guess)


print("Your final score is: " + str(game.score) + " out of 10.")
