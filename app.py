from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message
from flask import Flask, render_template
from flask import Flask, render_template, request
from flask import redirect, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.Html')  # This tells Flask to look for templates/index.html

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Email config (optional - for contact form email)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_app_password'

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if not name or not email or not message:
        flash("All fields are required!", "error")
        return redirect('/#contact')

    # Send email (optional)
    msg = Message(subject=f"Message from {name}",
                  sender=email,
                  recipients=["your_email@gmail.com"],
                  body=message)
    mail.send(msg)

    flash("Message sent successfully!", "success")
    return redirect('/#contact')

if __name__ == '__main__':
    app.run(debug=True)
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit-comment', methods=['POST'])
def submit_comment():
    comment = request.form['comment']
    print("New Comment Received:", comment)  # This prints the comment to the terminal
    # You could also save it to a database or file here
    return f"Thanks for your comment: {comment}"


@app.route('/submit-comment', methods=['POST'])
def submit_comment():
    comment = request.form['comment']
    print("Comment:", comment)
    # Do something with comment
    return redirect(url_for('home'))