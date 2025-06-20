# Phishing Attack Simulator

A full-stack cybersecurity training web application that simulates real-world phishing attacks in a completely safe, ethical, and local environment.

This project helps users understand the full phishing attack chain — from receiving a spoofed email to entering credentials on a fake login page — while logging user actions and visualizing behavior for educational purposes.

**Watch the demo video**: [https://youtu.be/QcUGuFrTsMU](https://youtu.be/QcUGuFrTsMU)
---

## Features

### Frontend
- **Landing Page**: Professional home page with a clear mission, disclaimers, and GitHub link.
- **Simulated Phishing Email Page**: Realistic email from “SecureBanking” urging users to click a verification link.
- **Fake Login Page**: Mimics a real banking login page; captures any credentials entered.
- **Credential Capture Page**: Logs fake credentials and explains the purpose of the simulation.

### Backend Functionality
- **Click Tracking**: Records user clicks on phishing links, including timestamps and target info.
- **Credential Logging**: Stores submitted fake credentials in a local SQLite database.
- **Admin Dashboard**: Visualizes phishing success rates with a data table and click behavior chart (Chart.js).

---

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Backend**: Python (Flask)
- **Database**: SQLite
- **Visualization**: Chart.js

---

## Real-World Case Study

### Objective
To test the effectiveness of the phishing simulator, I conducted a live phishing simulation with 4 participants. The goal was to observe user responses to a realistic phishing email and evaluate the educational value of the tool.

### Method
Participants received a spoofed email from "SecureBanking" asking them to verify their account. The simulator tracked:
- Email link clicks
- Credential submissions
- Timestamps for all interactions

Participants were then shown a warning page and debriefed about the simulation.

### Results

| Participant | Clicked Link | Entered Credentials | Reaction Time |
|-------------|--------------|---------------------|----------------|
| Ojas        | ❌ No         | ❌ No                | —              |
| Manan       | ✅ Yes        | ❌ No                | 2 minutes      |
| Anuj        | ✅ Yes        | ❌ No                | 1 minute       |
| Ayush       | ✅ Yes        | ✅ Yes              | 5 minutes      |

- **75%** of participants clicked the link.
- **25%** submitted fake credentials.
- Only **1** user identified the phishing attempt and avoided it entirely.

### Participant Feedback
- “It looked really real — I didn’t even question the link.”
- “The layout made me trust it. But I got suspicious when the login form didn’t redirect properly.”
- “The warning page after submitting credentials really drove it home.”

### Takeaways
- Most users are susceptible to clicking phishing links — even when they’re tech-savvy.
- Educational feedback directly after the attempt was key to reinforcing learning.

---

## 📥 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/phishing-attack-simulator.git
   cd phishing-attack-simulator
`'''

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**

   ```bash
   python app.py
   ```

5. **Visit**

   ```
   http://localhost:5000
   ```

> You can also expose the app publicly using `ngrok` (free) for demo purposes.

---


## ⚠️ Ethical Use Disclaimer

This simulator is intended **strictly for educational and ethical use only**.
It does **not** send real emails or interact with any real user data.
Do not deploy this in production or use it to simulate attacks without full consent.

---


## Contributions

Want to suggest a feature or improve the UI? PRs welcome!
Please include a short description and screenshot if relevant.
