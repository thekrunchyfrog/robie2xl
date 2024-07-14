import os
from game_setup import *
from read_me import *


class Robie2xl:
    def main():
        pass

    # if __name__ == "__main__":
    #    main()


game = GameSetup()
readit = ReadMe()
questions = game.get_questions()

for question in questions:
    print(question["question"])
    readit.readme(question["question"])
    game.read_answers(question)
    guess = input("What is your guess: ")
    x = game.check_answer(question, guess)
    os.popen("echo {0} | ./robo".format(x)).read()

readit(game.final_score())
