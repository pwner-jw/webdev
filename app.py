from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

# Route for the greetings page
@app.route('/')
def greetings():
    return render_template('greetings.html')

# Route for the moral story page
@app.route('/story')
def story():
    return render_template('story.html')

# Route for the feedback form page
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        comment = request.form['comment']
        save_feedback(name, comment)
        return redirect('/')
    return render_template('feedback.html')

# Function to save feedback to feedback.csv
def save_feedback(name, comment):
    with open('feedback.csv', 'a', newline='') as csvfile:
        fieldnames = ['Name', 'Comment']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'Name': name, 'Comment': comment})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
