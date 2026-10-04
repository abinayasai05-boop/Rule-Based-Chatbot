from flask import Flask, render_template, request, jsonify
from chatbot import get_response
from text_analyzer import analyze_text

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    message = data.get("message", "").strip()

    if not message:
        return jsonify({
            "response": "Please enter a message.",
            "analysis": {}
        })

    response, intent, confidence = get_response(message)
    analysis = analyze_text(message)

    analysis["intent"] = intent
    analysis["confidence"] = confidence

    return jsonify({
        "response": response,
        "analysis": analysis
    })


if __name__ == "__main__":
    app.run(debug=True)