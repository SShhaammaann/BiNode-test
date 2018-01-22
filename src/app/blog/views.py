from flask import Flask, render_template
from app.blog import blog

@blog.route("/")
@blog.route('/<username>')
def userNameView(username):
    return render_template('../templates/blog.html', username=username)

