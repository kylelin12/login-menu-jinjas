from flask import Flask, render_template, request, session, redirect
from utils import login_checker

login_app = Flask(__name__)
# For the session to be encrypted, you must set a secret key
login_app.secret_key = 'T0T@11YS3CUR3P@SSW0RD'

@login_app.route('/')
def login():
    # If you're logged in, go to the logged in page
    if 'logged_in' in session:
        return render_template('login_ok.html', username = session['logged_in'])
    # Else go to the login form page
    else:
        return render_template('login_form.html')

# Misleading name kinda, this route is accessed when the login button is pressed.
@login_app.route('/loggedin', methods=["POST", "GET"])
def loggedin():
    # Stores a 'cookie' that says that the user is logged in
    session['logged_in'] = login_checker.username_store()
    return login_checker.loggedin()

# Route that is accessed when the logout button is pressed.
@login_app.route('/logout', methods=["POST", "GET"])
def logout():
    # Pops the 'cookie' that says the user is logged in
    # Logs the user out
    session.pop('logged_in', None)
    # Redirects the user to the root/homepage route
    return redirect("./")

if __name__ == '__main__':
    login_app.debug = True
    login_app.run()