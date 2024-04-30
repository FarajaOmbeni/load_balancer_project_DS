from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def home():
    return "Homepage"

@app.route('/home')
def getname():
    return f"Hello from server: {socket.gethostname()}"

if __name__ == '__main__':
    app.run(debug=True)