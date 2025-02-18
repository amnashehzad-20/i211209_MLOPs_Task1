from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Deploying Flask App at Vercel"

