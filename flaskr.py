# -*- coding: utf-8 -*-
from flask import Flask, request, session, redirect, url_for, abort, \
     render_template, flash, Markup
import pandas as pd
import os

# Instantiate and configure our little app :)
app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] ='super-secret-key'
app.config['USERNAME'] = 'admin'
app.config['PASSWORD'] = 'default'
app.config['DATABASE'] = 'mydatabase.csv'
# Possible io methods: csv, excel, hdf, sql, json, 
# msgpack, html, gbq, stata, clipboard, pickle

# Create the dataframe for blog entries, aka posts
if not os.path.isfile(app.config['DATABASE']):
    df = pd.DataFrame()
    df['title'], df['text'] = [], []
    df.to_csv(app.config['DATABASE'], index=False)
    

@app.route('/')
def show_entries():
    df_entries = pd.read_csv(app.config['DATABASE'])
    entries = df_entries.to_dict(orient='records')
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    df_entry = pd.DataFrame([[Markup(request.form['title']), Markup(request.form['text'])]], 
        columns=['title', 'text'])
    df_entry.to_csv(app.config['DATABASE'], mode='a', header=False, index=False)
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    app.run()
