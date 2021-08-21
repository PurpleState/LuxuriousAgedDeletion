import datetime
import random

from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    date = datetime.datetime.now()
    current_year = date.year
    return render_template('index.html', num=random_number, year=current_year)

@app.route('/guess/<name>')
''' based on the name entered by user, this API predicts the gender and age of the user. Its for fun. '''
def guess(name):

    gender_url = f'https://api.genderize.io/?name={name}'
    gender_response  = requests.get(gender_url)
    gender_data = gender_response.json()
    gender  = gender_data["gender"]

    age_url = f'https://api.agify.io/?name={name}'
    age_response  = requests.get(age_url)
    age_data = age_response.json()
    age  = age_data["age"]

    current_year = datetime.datetime.now().year

    return render_template('guess.html', name=name, gender=gender, age=age, year=current_year)


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/92e41515e8e7f8466117"
    response = requests.get(blog_url)
    all_posts = response.json()

    current_year = datetime.datetime.now().year

    return render_template('blog.html', posts = all_posts, year=current_year)

if __name__ == "__main__":
    app.run(debug=True)
