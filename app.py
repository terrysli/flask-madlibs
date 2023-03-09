from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story
from stories import excited_story

STORY = silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/')
def index():
    """Return homepage with form to collect answers to prompts"""

    return render_template(
        'questions.html',
        prompts=STORY.prompts)

@app.get('/results')
def show_results():
    """Return resulting story for user-provided answers"""

    prompts = STORY.prompts

    # generate string of resulting story
    result = STORY.generate(request.args)

    return render_template(
        'results.html',
        result=result)