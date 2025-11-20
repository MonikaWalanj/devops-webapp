from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Devops Project! I am Monika testing ci and cd code on github with docker i am esing in dev directory"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
