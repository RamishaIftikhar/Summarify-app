from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from summarize import summarize_text

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()
    input_text = data.get("text", "")
    if not input_text:
        return jsonify({"error": "No text provided."}), 400

    summary = summarize_text(input_text)
    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(debug=True)
