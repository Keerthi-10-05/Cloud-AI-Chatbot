from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def chatbot():

    user_message = request.json["message"].lower()

    responses = {

"hi":"Hello! How are you?",

"hello":"Hello!",

"how are you":"I'm doing great. Thanks for asking.",

"what is your name":"I'm Cloud AI Chatbot.",

"bye":"Goodbye! Have a nice day.",

"who created you":"I was developed using Python and Flask.",

"what is python":"Python is a popular programming language.",

"what is flask":"Flask is a lightweight Python web framework.",

"what is cloud computing":"Cloud computing delivers services over the internet.",

"what is ai":"Artificial Intelligence enables computers to perform tasks that normally require human intelligence.",

"thank you":"You're welcome!",

"help":"Ask me about Python, Flask, AI or Cloud Computing."

}

    reply = responses.get(
        user_message,
        "Sorry, I don't understand that yet."
    )

    return jsonify({"response": reply})

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

    
