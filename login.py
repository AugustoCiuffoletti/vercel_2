from flask import Flask,request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Hallo "+request.form['username']+"!"
    else:
        return '''
            <h2>Come ti chiami?</h2>
            <form action="" method="post">
                <input type="text" name="username">
                <input type="submit" value="Invia">
            </form>
        '''
