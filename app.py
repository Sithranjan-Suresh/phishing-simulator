from flask import Flask, render_template, request
from datetime import datetime
import sqlite3

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

if __name__ == '__main__':
    app.run(debug=True)
