# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def do_add():
    """Add params"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(add(a, b))

@app.route("/sub")
def do_sub():
    """Subtract params"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(sub(a, b))

@app.route("/mult")
def do_mult():
    """Multiply params"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(mult(a, b))

@app.route("/div")
def do_div():
    """Divide params"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)

    return str(result)

operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<oper>")
def do_math(oper):
    """Math Operation"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(operators[oper](a, b))

