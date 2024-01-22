from flask import Flask, request, render_template
import random


app = Flask(__name__)

random_number = 0
random_foundation = 0

def checkAnswer(answer):
    global random_number, random_foundation
    return random_number%random_foundation==int(answer)

@app.route("/")
def index():
    global random_number, random_foundation
    random_number = random.randint(1, 1000)
    random_foundation = random.randint(1, 20)
    return render_template('quiz.html', 
                            random_number=random_number, random_foundation=random_foundation)

@app.route("/check", methods=['POST'])
def check():
    answer = request.form['answer']
    if(len(answer)==0):
        return
    textAnswer = "неправильный"
    if(checkAnswer(answer)):
        textAnswer = "правильный"
    return render_template('answer.html', answer = answer, 
                           forward_message = textAnswer)


if __name__== "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)