from flask import Flask, render_template, redirect, request, session
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Connection string for PostgreSQL
conn_str = 'postgresql://postgres:Fwc3StngKebReDyv@org-revuc-2024-inst-revuc.data-1.use1.tembo.io:5432/postgres'

try:
    # Create a new database session
    conn = psycopg2.connect(conn_str)
except Exception as e:
    print(f"Unable to connect to the database: {e}")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        cursor.close()
        
        if user and check_password_hash(user[2], password):
            session['username'] = username
            return redirect('/dashboard')
        else:
            return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        
        if not username or not password:
            return render_template('login.html', error='Missing Username or Password')
        
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        existing_user = cursor.fetchone()
        
        if existing_user:
            return render_template('login.html', error='Username Already Exists!')
        else:
            cursor.execute("""
                INSERT INTO users (username, password)
                VALUES (%s, %s)
            """, (username, password))
            conn.commit()
            cursor.close()
            session['username'] = username
            return redirect('/dashboard')
    
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
