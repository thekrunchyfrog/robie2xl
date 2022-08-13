import requests


class Opentdb:
    _base_url = "https://opentdb.com/"
    _cat_url = _base_url + "api_category.php"
    _token_url = _base_url + "api_token.php?command=request"
    _questions_url = _base_url + "api.php?"

    def __init__(self):
        r = requests.get(self._token_url)
        self.token = r.json()["token"]

    def get_catagories(self):
        r = requests.get(self._cat_url)
        return r.json()["trivia_categories"]

    def get_questions(self, category, amount=10, difficulty="medium", qtype="multiple"):
        questions_url = "{}&category={}&amount={}&difficulty={}&type={}&token={}"
        r = requests.get(
            questions_url.format(
                self._questions_url, category, amount, difficulty, qtype, self.token
            )
        )
        return r.json()["results"]
