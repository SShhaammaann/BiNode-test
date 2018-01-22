from flask import Flask, render_template

app = Flask(__name__)

@app.route("/blog/")
@app.route('/blog/<username>')
def getUserName(username):
    return render_template('../templates/blog.html', id=username)

