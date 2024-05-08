from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title="Home Page", description="Welcome to my Flask app!")

if __name__ == '__main__':
    app.run(debug=True)

