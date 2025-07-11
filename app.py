from flask import Flask, request, render_template_string
from rag_setup import qa_chain

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>🏏 Cricket Chatbot</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #eef2f3;
            padding: 40px;
        }
        .container {
            background: white;
            max-width: 700px;
            margin: auto;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h2 {
            color: #1976d2;
            text-align: center;
        }
        input[type="text"] {
            width: 100%;
            padding: 12px;
            margin-top: 10px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 6px;
        }
        button {
            background-color: #1976d2;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 6px;
            margin-top: 10px;
            font-size: 16px;
            cursor: pointer;
            width: 100%;
        }
        button:hover {
            background-color: #1565c0;
        }
        .response {
            margin-top: 20px;
            background-color: #e3f2fd;
            padding: 15px;
            border-radius: 8px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>🏏 Cricket Chatbot</h2>
        <form method="post">
            <input type="text" name="question" placeholder="Ask something about cricket..." required>
            <button type="submit">Ask</button>
        </form>
        {% if answer %}
        <div class="response">
            <strong>Answer:</strong> {{ answer }}
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    if request.method == "POST":
        question = request.form["question"]
        answer = qa_chain.run(question)
    return render_template_string(HTML, answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
