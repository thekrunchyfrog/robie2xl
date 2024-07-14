import os


class ReadMe:
    def removeUnreadable(self, phrase):
        for thing in ("'", "(", ")", "`", '"'):
            phrase = phrase.replace(thing, "")
        phrase = phrase.replace("&", "and")
        return phrase

    def readme(self, phrase):
        phrase = self.removeUnreadable(phrase)
        os.popen("echo {0} | ./robo".format(phrase)).read()
