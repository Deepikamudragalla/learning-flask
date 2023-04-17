from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
 return render_template("index.html")
@app.route("/deepika")
def index1():
 return "deepika is good"
@app.route("/deepika_the_great")
def index2():
 return "deepika is great"
if __name__ == "__main__":
	app.run(debug=True)

