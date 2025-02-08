
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini AI API Key
genai.configure(api_key="AIzaSyCIpd-JnEZWgTtjMseFTw08Wj5lNEdo17Q")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_question = request.form["question"]

    try:
        # Initialize the Gemini AI model
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_question)

        # Ensure proper formatting (Convert markdown to HTML)
        bot_reply = response.text if hasattr(response, "text") else "I'm sorry, I couldn't generate a response."
        bot_reply = bot_reply.replace("*", "").replace("\n", "<br>")  # Remove * and keep line breaks

    except Exception as e:
        bot_reply = f"<span style='color: red;'>Error: {str(e)}</span>"

    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
