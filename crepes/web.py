import flask

app = flask.Flask(__name__, static_url_path='/')

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/order/<item>')
def order(item):
    return flask.render_template('order.html', code=66)

app.run(port=3636, debug=True)