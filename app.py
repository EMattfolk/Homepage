from flask import Flask, render_template

app = Flask(__name__, static_url_path="/static")

def page(name: str):
    with open(f"pages/{name}.html") as f:
        return render_template("base.html", content=f.read())

@app.route("/")
def root():
    return page("about")
