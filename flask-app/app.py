from flask import Flask, render_template, request
import os
import shutil

total, used, free = shutil.disk_usage("/")

total = (total // (2**30))
used  = (used // (2**30))
free = (free // (2**30))

from werkzeug.utils import redirect

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        title = request.form.get('title').lower()
        content = request.form.get("content")

        if os.path.exists(f'{os.getcwd()}/feedback/{title}.txt'):
            return redirect('/exists')
        else:
            with open(os.getcwd()+'/feedback/'+title+'.txt', mode='w') as f:
                f.write(content)

    return render_template('index.html', e=False)

@app.route('/exists')
def already():
    return render_template('index.html', e=True)

@app.route('/feedback/<file>')
def feedback(file):
    with open(os.getcwd()+'/feedback/'+file) as f:
            c = f.read()
    return c

@app.route('/disk')
def save():
    return f'{total}Gb = {used}Gb + {free}Gb'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')