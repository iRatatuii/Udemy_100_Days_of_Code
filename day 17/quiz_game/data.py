import requests

url = "https://opentdb.com/api.php?amount=13&type=boolean"

question_data = {
    "response_code": 0,
    "results": [
        {
            "type": "boolean",
            "difficulty": "medium",
            "category": "Entertainment: Video Games",
            "question": "In the Resident Evil series, Leon S. Kennedy is a member of STARS.",
            "correct_answer": "False",
            "incorrect_answers": ["True"],
        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science &amp; Nature",
            "question": "An exothermic reaction is a chemical reaction that releases energy by radiating electricity.",
            "correct_answer": "False",
            "incorrect_answers": ["True"],
        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science: Computers",
            "question": "RAM stands for Random Access Memory.",
            "correct_answer": "True",
            "incorrect_answers": ["False"],
        },
    ],
}

r = requests.get(url=url)
if r.status_code == 200:
    question_data = r.json()
