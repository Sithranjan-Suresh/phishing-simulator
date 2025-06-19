from flask import Flask, render_template, request

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
    print(f"[TRACKED] User clicked on phishing link targeting: {target}")
    return "<h2>✅ Click tracked! This is a simulation. No action taken.</h2>"

if __name__ == '__main__':
    app.run(debug=True)
