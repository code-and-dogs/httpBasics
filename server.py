from flask import Flask, request, render_template
import json

app = Flask(__name__)

@app.route('/firstrequest', methods=['GET'])
def firstRequest():
    return(render_template('index.html'))

@app.route('/secondrequest', methods=['GET'])
def secondRequest():
    userAgent = str(request.headers['User-Agent'])
    return(render_template('start.html', userAgent = userAgent))

@app.route('/fourthrequest', methods=['GET'])
def fourthRequest():
    return(int("HI"))

@app.route('/thirdrequest', methods=['GET', 'POST'])
def thirdRequest():
    reqData = request.form
    return('You just posted.... ' + str(reqData))

if __name__ == '__main__':
    app.run(debug=True)
