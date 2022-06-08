from flask import Flask, render_template, request
#from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

#debug = DebugToolbarExtension(app)

@app.get('/')
def homepage():
    prompts = request.args.get(silly_story.prompts)
    #input_words = sample(#words list, number?)

    return render_template('questions.html', noun = prompts)
