from flask import Flask, url_for, render_template, redirect, request
from markupsafe import escape
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']= True

on = False

@app.route('/', methods=['GET', 'POST'])
def index():
    global on
    if request.method == 'POST':
        if request.form['btn'] == 'on':
            on = True
        elif request.form['btn'] == 'off':
            on = False
        elif request.form['btn'] == 'toggle':
            on = not on
    return render_template('index.html', on = on)

@app.route('/test/<string:var>')
def test_world(var):
    return 'test, World! %s' % escape(var)

@app.route('/template/<name>')
def test_template(name):
    return render_template('name_template.html', name=name)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
