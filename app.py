from flask import Flask, render_template

app = Flask(__name__, static_url_path="/static")

navigation = [
    ("Home",     "/"),
    ("CV",       "/cv"),
    ("Projects", "/projects"),
];

def page(name: str):
    with open(f"pages/{name}.html") as f:
        content = f.read()

    kwargs = {
        "content": content,
        "navigation": navigation,
        "page": name,
    }

    return render_template("base.html", **kwargs)


@app.route("/")
def home():
    return page("home")


@app.route("/cv")
def cv():
    return page("cv")


@app.route("/projects")
def projects():
    return page("projects")


@app.route("/404.html")
def not_found():
    return page("404")
