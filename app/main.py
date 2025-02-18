from flask import Flask
from serverless_wsgi import handle_request  # WSGI adapter

app = Flask(__name__)

@app.route('/')
def home():
    return "Deploying Flask App at Vercel"

def handler(event, context):
    return handle_request(app, event, context)