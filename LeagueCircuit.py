from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sign-up')
def sign_up():
    return render_template("signup.html")


if __name__ == '__main__':
    app.run(debug=True)
