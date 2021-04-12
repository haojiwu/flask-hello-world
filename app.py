from flask import Flask

app = Flask(__name__)

def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

@app.route('/test/<num>')
def hello_world(num):
    l = [None] * 1000000 * num
    fib(int(num))
    return 'Hello, World!'
