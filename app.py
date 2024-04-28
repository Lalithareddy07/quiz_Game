from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {"question": "What planet do we live on?", "answer": "Earth"},
    {"question": "What is the color of the sky on a clear day?", "answer": "Blue"},
    {"question": "What gas do plants breathe in that humans and animals breathe out?", "answer": "Carbon dioxide"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "What is the capital of France?", "answer": "Paris"}
]
index = 0
score = 0

@app.route("/", methods=["GET", "POST"])
def quiz():
    global index, score
    if request.method == "POST":
        user_answer = request.form['answer']
        if user_answer.lower() == questions[index]['answer'].lower():
            score += 1
        index += 1
    
    if index >= len(questions):
        result = f"Your final score is: {score}/{len(questions)}"
        index, score = 0, 0  # Reset for next player
        return render_template("result.html", result=result)
    else:
        return render_template("index.html", question=questions[index]["question"])

if __name__ == "__main__":
    app.run(debug=True)
