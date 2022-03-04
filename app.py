from flask import Flask, request, render_template
from stories import story1

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/story-form')
def story_form():
    return render_template('story_form.html', prompts=story1.prompts)

@app.route('/story-show')
def story_show():
    args = request.args
    full_story = story1.generate(args)
    return render_template('story_show.html', full_story=full_story)