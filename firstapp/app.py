from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
    #return "<p>Hello, World!</p>"

@app.route("/about")
def about():
    return render_template("about.html")
    #return "<p>This, is about page!</p>"
@app.route("/dashboard/<name>")
def dashboard(name):
    return render_template("Dashboard.html", name=name)

if __name__=='__main__':
    app.run(debug=True)
    