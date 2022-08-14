import opentdb
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
        raw_questions = self.conn.get_questions(15)
        i = 0
        for raw_question in raw_questions:
            answers = []
            questions.append({"question": unescape(raw_question["question"])})
            answers = [{unescape(raw_question["correct_answer"]): True}]
            for answer in raw_question["incorrect_answers"]:
                answers.append({unescape(answer): False})
            questions[i]["answers"] = answers
            i = i + 1
        return questions

    # if __name__ == "__main__":
    #    main()


# print(list(Robie2xl().prepare_questions()[5]["answers"][3].keys())[0])
questions = Robie2xl().prepare_questions()
for question in questions:
    print(question["question"])
    for answer in question["answers"]:
        print(list(answer.keys())[0])
