from flask import Flask, request, jsonify
import subprocess
import git
import openai

app = Flask(__name__)

# OpenAI API Key (Replace with your key)
OPENAI_API_KEY = "your-openai-api-key"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}],
        api_key=OPENAI_API_KEY
    )
    return jsonify({"response": response["choices"][0]["message"]["content"]})

@app.route("/run_command", methods=["POST"])
def run_command():
    command = request.json.get("command", "")
    try:
        output = subprocess.check_output(command, shell=True, text=True)
        return jsonify({"output": output})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/clone_repo", methods=["POST"])
def clone_repo():
    repo_url = request.json.get("repo_url", "")
    try:
        git.Repo.clone_from(repo_url, "./cloned_repo")
        return jsonify({"message": "Repository cloned successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
