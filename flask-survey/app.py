from flask import Flask, render_template, request, redirect, session, flash
from surveys import satisfaction_survey as survey
from flask_debugtoolbar import DebugToolbarExtension

ANSWERS_KEY = "answers"

app = Flask(__name__)
app.config['SECRET_KEY']="dfsgsEGseg"

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


@app.route('/')
def home_page():
    return render_template('instructions.html', survey=survey)

@app.route('/start', methods=["POST"])
def start_survey():
    """Clean session to store new user answers"""
    session[ANSWERS_KEY] = []
    return redirect('/questions/0')

@app.route('/answer', methods=["POST"])
def save_answers():
    """Save the user answer to session"""
    #get an answer
    answer=request.form["answer"]
    #make session into a variable
    answers=session[ANSWERS_KEY]
    #reference session variable to append an answer
    answers.append(answer)

    #saves the answers into the public scope session[] for the sake of keeping
    # a count of which question theyr on.

    session[ANSWERS_KEY] = answers

    if(len(answers) == len(survey.questions)):
        return redirect('/confirmation')
    else:
        return redirect(f'/questions/{len(answers)}')



@app.route('/questions/<int:qid>')
def ask_question(qid):
    """Ask the current question in the survey using session as reference for already answered questions"""

    answers=session.get(ANSWERS_KEY)

    if (answers is None):
        # if there are yet no answers saved in session
        return redirect("/")

    if (len(answers) == len(survey.questions)):
        # if there is an asnwer for each question in the survey
        return redirect("/complete")

    if (len(answers) != qid):
        # if attempting to answer questions out of order
        flash(f"Invalid question id: {qid}.")
        return redirect(f"/questions/{len(answers)}")

    question = survey.questions[qid]
    return render_template('question.html', qid=qid, question=question, survey=survey)


@app.route('/confirmation')
def confirmation():
    """Let user know they have completed survey"""
    return render_template('confirmation.html)
