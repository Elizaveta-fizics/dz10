import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    cand = "<pre>"
    for candidate in candidates:
        cand += f"Имя кандидата - {candidate['name']}\nПозиция кандидата - {candidate['position']}\nНавыки через запятую - {candidate['skills']}\n\n"

    return cand + "</pre>"

@app.route('/candidate/<int:id>')
def id_candidate(id):
    cand = "<pre>"
    for candidate in candidates:
        if candidate["id"] == id:
            cand += f"<img src='{candidate['picture']}'><img>\nИмя кандидата - {candidate['name']}\nПозиция кандидата - {candidate['position']}\nНавыки через запятую - {candidate['skills']}\n\n"
            return cand + "</pre>"


@app.route('/skill/<skill>')
def skill_candidate(skill):
    list_candidate = []
    cand = "<pre>"
    for candidate in candidates:
        list_candidate = candidate["skills"].split(", ")
        if skill in list_candidate:
            cand += f"Имя кандидата - {candidate['name']}\nПозиция кандидата - {candidate['position']}\nНавыки через запятую - {candidate['skills']}"
            return cand + "</pre>"




with open("candidates.json", encoding='utf-8') as file:
    candidates = json.load(file)

if __name__ == '__main__':
    app.run(debug=True)