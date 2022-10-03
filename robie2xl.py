import opentdb
import random

from html import unescape


class Robie2xl:
    def __init__(self):
        self.conn = opentdb.Opentdb()

    def main():
        pass

    def list_categories(self):
        categories = self.conn.get_catagories()

        for category in categories:
            print(str(category["id"]) + " " + category["name"])

    def prepare_questions(self):
        questions = []
        raw_questions = self.conn.get_questions(11)
        i = 0
        for raw_question in raw_questions:
            answers = []
            questions.append({"question": unescape(raw_question["question"])})
            answers = [{unescape(raw_question["correct_answer"]): True}]
            for answer in raw_question["incorrect_answers"]:
                answers.append({unescape(answer): False})
            questions[i]["answers"] = self.prepare_answers(answers)
            i = i + 1
        return questions

    def prepare_answers(self, answers):
        prepped_answers = {}
        for x in ("a", "b", "c", "d"):
            item1 = random.choice(answers)
            prepped_answers[x] = item1
            answers.remove(item1)
        return prepped_answers

    def read_answers(answers):
        for key in question["answers"]:
            for key2 in question["answers"][key]:
                print(key + ": " + key2)

    # if __name__ == "__main__":
    #    main()


# print(list(Robie2xl().prepare_questions()[5]["answers"][3].keys())[0])
questions = Robie2xl().prepare_questions()

score = 0

for question in questions:
    print(question["question"])
    Robie2xl.read_answers(question["answers"])
    guess = input("What is your guess: ")
    is_it = list(question["answers"][guess].values())[0]

    print(question["answers"])
    if is_it is True:
        score += 1
        print("Correct! Score is now: " + str(score))
    else:
        print("Wrong! Your score is still: " + str(score))

print("Your final score is: " + str(score) + "out of 10.")
