from flask import Flask, render_template

app = Flask(__name__)

@blog.route("/")
@blog.route('/<username>')
def userNameView(username):
    return render_template('../templates/blog.html', username=username)

