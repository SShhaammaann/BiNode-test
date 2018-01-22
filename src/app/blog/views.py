from flask import Flask, render_template
from app.blog import blog

# Подключать Blueprint только с префиксом blog

@blog.route("/", defaults={'username':'anonymous'})
@blog.route('/<username>')
def userNameView(username):
    return render_template('../templates/blog.html', username=username)

