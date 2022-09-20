from flask import Flask#import flask

app = Flask(__name__)#new instance of path (what does this mean?)
#Instance of path

@app.route('/') #route of the path
def hello_world():
    return 'Hello World'

@app.route('/<name>') #route of the path (what does this mean)
def name(name):
    return 'Hello ' + name #Helloname

if __name__ == '__main__':
    app.run(debug=True)


