from flask import Flask, render_template

app = Flask(__name__)

# Dummy data to show dynamic rendering on membership page
membership_plans = [
    {
        'name': 'Basic',
        'price': '$999 / month',
        'features': ['Access to gym equipment', 'Locker', '1 group class / week']
    },
    {
        'name': 'Pro',
        'price': '1,799$ / month',
        'features': ['All Basic features', 'Unlimited group classes', '1 personal training / month']
    },
    {
        'name': 'Premium',
        'price': '3,999$ / month',
        'features': ['All Pro features', 'Unlimited PT', 'Nutrition plan', 'Spa access']
    }
]

@app.route('/')
def home():
    highlights = [
        'State-of-the-art equipment',
        'Certified trainers',
        'Flexible timings',
        'Personalized training plans'
    ]
    return render_template('home.html', highlights=highlights)

@app.route('/about')
def about():
    team = [
        {'name': 'Ahsan Khan', 'role': 'Head Trainer'},
        {'name': 'Sara Malik', 'role': 'Nutritionist'},
        {'name': 'Bilal Ahmed', 'role': 'Physio'}
    ]
    mission = "To create a welcoming fitness community that helps members reach goals safely and sustainably."
    return render_template('about.html', mission=mission, team=team)

@app.route('/membership')
def membership():
    services = [
        'Cardio Zone', 
        'Weight Training', 
        'Group Classes', 
        'Nutrition Advice', 
        'Sauna & Spa'
    ]
    return render_template('membership.html', plans=membership_plans, services=services)

if __name__ == '__main__':
    app.run(debug=True)
