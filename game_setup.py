import opentdb
import random
from html import unescape
from read_me import *


class GameSetup:
    score = 0

    def __init__(self):
        self.conn = opentdb.Opentdb()

    def get_categories(self):
        return self.conn.get_catagories()

    def get_questions(self):
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

    def read_answers(self, question):
        for key in question["answers"]:
            for key2 in question["answers"][key]:
                print(key + ": " + key2)
                ReadMe().readme(key + ": " + key2)

    def get_correct_answer(self, question):
        for answer in ("a", "b", "c", "d"):
            if list(question["answers"][answer].values())[0] is True:
                return answer

    def check_answer(self, question, guess):
        is_it = list(question["answers"][guess].values())[0]
        correct_answer = self.get_correct_answer(question)

        if is_it is True:
            self.score += 1
            return "Correct! Score is now: " + str(self.score)
        else:
            return (
                "Wrong! Correct answer was: "
                + correct_answer
                + ": "
                + list(question["answers"][correct_answer].keys())[0]
                + ". Your score is still: "
                + str(self.score)
            )

    def final_score(self):
        return "Your final score is: " + str(self.score) + " out of 10."
