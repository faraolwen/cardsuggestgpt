from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        input_text = request.form["input_text"]
        response = process_input(input_text)
    return render_template("index.html", response=response)

def process_input(input_text):
    # ここで入力テキストを処理し、適切な返答を生成します。
    return input_text.upper()

if __name__ == "__main__":
    app.run(debug=True)
