from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/')
def homepage():
    prompts = silly_story.prompts
    #input_words = sample(#words list, number?)

    return render_template('questions.html', prompts=prompts)


@app.post('/story')
def results():
    results = request.form
    result_story = silly_story.generate(results)

    return render_template("story.html", story_text=result_story)
    # return f'<h1>"{prompts}"</h1> '

