from flask import Flask, render_template, redirect, request, session
import psycopg2

app = Flask(__name__)
app.secret_key = '65cc6c216e0429368f170452'

# PostgreSQL connection string
conn_str = 'postgresql://postgres:Fwc3StngKebReDyv@org-revuc-2024-inst-revuc.data-1.use1.tembo.io:5432/postgres'
try:
    # Connect to PostgreSQL
    conn = psycopg2.connect(conn_str)
    print("Connected to the PostgreSQL database")
except Exception as e:
    print("Failed to connect to PostgreSQL")

@app.route("/")
@app.route("/home")
def home():
    # gui_instance.run(use_reloader=True)
    return render_template("home.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    return render_template("dashboard.html")

@app.route("/getdata", methods=["GET", "POST"])
def getdata():
    return render_template("getdata.html")

@app.route("/submit-data", methods=["GET", "POST"])
def submitdata():
    user_data = {}
    session['username'] = "admin"
    if 'username' in session:
        username = session['username']
        if request.method == 'POST':
            age = request.form['age']
            gender = request.form['gender']
            weight = request.form['weight']
            height = request.form['height']
            occupation = request.form['occupation']
            sleep_duration = request.form['sleep_duration']
            blood_pressure = request.form['blood_pressure']
            heart_rate = request.form['heart_rate']
            daily_steps = request.form['daily_steps']
            
            if age and gender and weight and height and occupation and sleep_duration and blood_pressure and heart_rate and daily_steps:
                 # Create a cursor object
                    try:
                        
                        cur = conn.cursor()

                        # Define your SQL statement for updating data
                        sql = """UPDATE users
                                SET age = %s, gender = %s, weight = %s, occupation = %s,
                                    sleep_duration = %s, blood_pressure = %s,
                                    heart_rate = %s, daily_steps = %s
                                WHERE username = %s;"""

                        # Define the values you want to update
                        values = (age, gender, weight, occupation, sleep_duration, blood_pressure,
                                heart_rate, daily_steps, username)

                        # Execute the SQL statement with the values
                        cur.execute(sql, values)

                        # Commit the transaction
                        conn.commit()

                        # Close the cursor and connection
                        cur.close()
                        conn.close()
                    except Exception as e:
                        print(f"Error: {e}")
                    user_data = {
                        "age": age, 
                        "gender": gender,
                        "weight": weight,
                        "height": height,
                        "occupation": occupation,
                        "sleep_duration": sleep_duration,
                        "blood_pressure": blood_pressure,
                        "heart_rate": heart_rate,
                        "daily_steps": daily_steps
                    }

                    return render_template("dashboard.html", user_data=user_data)
    return render_template("dashboard.html", user_data=user_data)

if __name__ == "__main__":
    app.run(debug=True, port = 5000)


def create_foreign_keys():
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(conn_str)
        print("Connected to the PostgreSQL database")

        # Create foreign data wrapper and foreign tables
        cursor = conn.cursor()
        cursor.execute("""
            CREATE FOREIGN DATA WRAPPER clerk_wrapper
            HANDLER clerk_fdw_handler
            VALIDATOR clerk_fdw_validator;
            
            CREATE SERVER my_clerk_server
            FOREIGN DATA WRAPPER clerk_wrapper
            OPTIONS (api_key '<clerk secret Key>');
            
            CREATE FOREIGN TABLE clerk_users (
                user_id TEXT,
                first_name TEXT,
                last_name TEXT,
                email TEXT,
                gender TEXT,
                created_at BIGINT,
                updated_at BIGINT,
                last_sign_in_at BIGINT,
                phone_numbers BIGINT,
                username TEXT
            )
            SERVER my_clerk_server
            OPTIONS (object 'users');
            
            CREATE FOREIGN TABLE clerk_organizations (
                organization_id TEXT,
                name TEXT,
                slug TEXT,
                created_at BIGINT,
                updated_at BIGINT,
                created_by TEXT
            )
            SERVER my_clerk_server
            OPTIONS (object 'organizations');
            
            CREATE FOREIGN TABLE clerk_organization_memberships (
                user_id TEXT,
                organization_id TEXT,
                role TEXT
            )
            SERVER my_clerk_server
            OPTIONS (object 'organization_memberships');
        """)
        conn.commit()
        print("Foreign keys created successfully")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

def print_foreign_table_data(table_name):
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(conn_str)
        print(f"Connected to the PostgreSQL database - Printing data from '{table_name}'")

        # Fetch and print data from foreign table
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        print(rows)
        for row in rows:
            print(row)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()