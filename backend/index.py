from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/nextgen")
def trigger_next_generation():
    return "<p>Next generation triggered!</p>"

@app.route("/nextgen/<int:generation>")
def get_next_generation(generation):
    return f"<p>Next generation: {generation}</p>"

@app.route("/fibonacci/<int:n>")
def calculate_nth_fibonacci(n):
    # calculate nth fibonacci number
    return f"<p>{n}th fibonacci number is {recur_fib(n)}</p>"

def recur_fib(n):
    return n if n <= 1 else (recur_fib(n-1) + recur_fib(n-2))