from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story
from stories import excited_story

STORY = excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/')
def index():
    """Return homepage"""

    html = render_template(
        'questions.html',
        prompts=STORY.prompts)

    return html

@app.get('/results')
def show_results():
    """Return resulting STORY for user-provided answers"""

    prompts = STORY.prompts
    template = STORY.template

    # create dictionary of {prompts: answers} from inputs
    answers = {}
    for prompt in prompts:
        answers[prompt] = request.args[prompt]

    result = STORY.generate(answers)

    html = render_template(
        'results.html',
        result_story=result)

    return html