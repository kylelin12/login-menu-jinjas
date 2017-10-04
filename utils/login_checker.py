from flask import Flask, render_template, request

# Hardcoaded username/password
m_username = "DWROX"
m_password = "s3cur3p@ssw0rd"

# Function that determines if the login is successful
def loggedin():
    # Takes the inputs and stores the values as variables
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
    else:
        username = request.args['username']
        username = request.args['password']
    # If the username matches the hardcoded username
    if username == m_username:
        # If the password matches the hardcoded password
        if password == m_password:
            # Return the welcome page
            return render_template('login_ok.html', username = username)
        else:
            # Return the bad password page
            return render_template('login_bad.html', why_bad = "Invalid Password")
    else:
        # If the password matches the hardcoded password
        # but the username doesn't match the hardcoded username
        if password == m_password:
            # Return the bad username page
            return render_template('login_bad.html', why_bad = "Username not recognized")
        else:
            # Return the bad username & password page
            return render_template('login_bad.html', why_bad = "Username and password are not recognized")

# Returns the hardcoded username (bad code)
def username_store():
    return m_username