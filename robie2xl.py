from insults import insults
from praise import praise
from game_setup import *
from read_me import *
import random


class Robie2xl:
    def main():
        pass

    # if __name__ == "__main__":
    #    main()


game = GameSetup()
readit = ReadMe()
questions = game.get_questions()

question_number = 0

while question_number < len(questions):
    readit.readme(questions[question_number]["question"])
    game.read_answers(questions[question_number])
    readit.readme("What is your guess?")
    guess = input("What is your guess: ")

    if guess not in ["a", "b", "c", "d"]:
        readit.readme("does not compute")
        continue
    else:
        x = game.check_answer(questions[question_number], guess)

    readit.readme(x[0])

    if x[1] == "right":
        readit.readme(random.choice(praise))
        readit.readme("your score is now " + str(game.score))
    else:
        readit.readme(random.choice(insults))
        readit.readme("your score is still " + str(game.score))

    question_number = question_number + 1

readit(game.final_score())
