from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Hugging Face model API (free endpoint, small model)
HF_API_URL = "https://api-inference.huggingface.co/models/gpt2"
HF_HEADERS = {"Authorization": "Bearer YOUR_HF_API_TOKEN"}  # we’ll fix this later

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    user_input = data.get("text", "")

    response = requests.post(HF_API_URL, headers=HF_HEADERS, json={"inputs": user_input})
    output = response.json()

    return jsonify(output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
