from flask import Flask, render_template, request
from datetime import datetime, date
import sys
import os
app = Flask(__name__)
menu = {'Home':'/', 'About':'/about', 'Contact':'/contact'}
today = date.today()
age = today.year - 2001 - ((today.month, today.day) < (9, 17))
@app.route('/')
def index():
    return render_template('index.html', menu=menu, my_os=os.uname(),
                           user_agent=request.headers.get('User-Agent'), version=sys.version,
                           time_now=datetime.now().strftime("%H:%M"))

@app.route('/about')
def info():
    return render_template('about.html', menu=menu,age=age, month=today.month, day=today.day)

@app.route('/contact')
def achievement():
    return render_template('contact.html', menu=menu)

if __name__=='__main__':
    app.run(debug=True)