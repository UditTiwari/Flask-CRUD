from blog import blog
from flask import render_template

@blog.route('/blog')
def blog_page():
    # return "Blog Home page"
    return render_template('index.html')


