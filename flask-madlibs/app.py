import re
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories



app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def select_page():
    """Ask to select a story"""
    return render_template('select.html', stories=stories.values())


@app.route('/questions')
def questions_page():
    """Ask Questions Form"""
    story_id = request.args["story_id"]
    story = stories[story_id]

    prompts = story.prompts
    return render_template('questions.html', story_id=story_id, title=story.title, prompts=prompts)

@app.route('/story')
def story_page():
    """Show Written Story with Form Input"""
    story_id = request.args["story_id"]
    story = stories[story_id]

    written_story= story.generate(request.args)
    return  render_template('story.html', title=story.title, written_story=written_story)
