
import re
from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.secret_key = 'your_key_here'

messages = [""]

def find_suspicious_words(query:str):
    suspects = ["SELECT", "DROP", "INSERT", "DELETE", "FROM", "'" "\""]
    for suss in suspects:
        if query.__contains__(suss):
            print("Possible SQL injection")
            return True
    else: return False
        

def only_digits(query:str):
    if not re.match("\d[^a-z]", query):
            print("Non-numeric characters included in numeric only input")
            return True
    else: return False


def limited_length(query:str, length_limit: int = 20):
     if len(query) > length_limit:
          print("Oversized query - possible SQL injection attempt")
          return True
     else: return False

@app.route('/')
def index():
     return render_template('index.html', messages = messages)

# ...

@app.route('/sanitise/', methods=('GET', 'POST'))
def sanitise():
    safe = True
    if request.method == 'POST':
        id = request.form['id']
        pwd = request.form['pwd']

        if not id:
            flash('Please enter your user ID')
            safe = False
        elif not pwd:
            flash('Please enter your password')
            safe = False
        else:
            if only_digits(id):
                 flash('Non-numeric characters included in numeric only input')
                 safe = False
            if limited_length(pwd) or limited_length(id):
                 flash('Please limit length of input to 20 characters')
                 safe = False
            if find_suspicious_words(pwd) or find_suspicious_words(id):
                 flash('What are you playing at?')
                 safe = False
        if safe: 
            messages.append("Success no. " + str(len(messages)) + "!")
            return redirect(url_for('login'))
        
    return render_template('sanitise.html')

@app.route('/login')
def login():
     return render_template('login.html')
