from flask import Flask, url_for, render_template
from markupsafe import escape
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']= True

on = False

@app.route('/')
def index():
    return render_template('index.html', on = on)

@app.route('/test/<string:var>')
def test_world(var):
    return 'test, World! %s' % escape(var)

@app.route('/template/<name>')
def test_template(name):
    return render_template('name_template.html', name=name)

@app.route('/on')
def on():
    global on
    on = True
    print("on:", on)
    return index()

@app.route('/off')
def off():
    global on
    on = False
    print("on:", on)
    return index()

@app.route('/toggle')
def toggle():
    global on
    on = not on
    print("on:", on)
    return index()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
