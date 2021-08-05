from flask import Flask, render_template
import requests
import datetime

app = Flask(__name__)

blog_url = "https://api.npoint.io/92e41515e8e7f8466117"
response = requests.get(blog_url)
all_posts = response.json()
current_year = datetime.datetime.now().year


@app.route('/')
def home():
    return render_template("index.html", posts = all_posts, year=current_year)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    post = all_posts[int(num)-1]
    print(post)
    return render_template('post.html', post = post, year=current_year)

if __name__ == "__main__":
    app.run(debug=True)
