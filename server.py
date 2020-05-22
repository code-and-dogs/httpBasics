from flask import Flask, request, render_template
import json

app = Flask(__name__)

@app.route('/start', methods=['GET'])
def start():
    #print(request.headers)
    userAgent = str(request.headers['User-Agent'])
    return(render_template('start.html', userAgent = userAgent))

@app.route('/', methods=['GET'])
def index():
    #print(request.headers)
    userAgent = str(request.headers['User-Agent'])
    return(render_template('index.html', userAgent = userAgent))

@app.route('/1', methods=['POST'])
def index1():
    return("HI")

@app.route('/2', methods=['GET'])
def index2():
    return(int("HI"))

@app.route('/3', methods=['GET', 'POST'])
def index3():
    print(request.headers)
    print(request.form)
    reqData = request.form
    return('You just posted.... ' + str(reqData))
    #return(render_template('index3.html', reqData = reqData))

if __name__ == '__main__':
    app.run(debug=True)
