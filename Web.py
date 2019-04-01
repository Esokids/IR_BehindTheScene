from flask import Flask, render_template, request
from InvertedIndex import main as InvertedIndex

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("input-form.html")


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == "POST":
        word = request.form.get("Search")
        res,count_assignment,count_comparator = InvertedIndex(word)
    return render_template("result.html", result=res, count_ass=count_assignment, count_com=count_comparator )


if __name__ == '__main__':
    app.run(debug=True)
