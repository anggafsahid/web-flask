from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('page_home.html')

@app.route("/about")
def about():
    return """
    <h1>About This Website</h1>
    <p> by anggafsahid </p>
    <code>Source: https://github.com/anggafsahid/web-flask</code>
    """