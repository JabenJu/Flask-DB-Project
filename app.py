from flask import Flask,render_template,request,redirect,url_for
import psycopg2

app = Flask(__name__)

active_user = []

def get_db_connection():
   conn = psycopg2.connect(
   host = 'localhost',
   database = 'flask_db',
   user = 'postgres',
   password = 'jaben1215'
   )

   return conn

@app.route("/register")
def register(error =None):   
    return render_template("register.html", error=error)

@app.route("/register", methods=["POST"])
def registers():

    conn = get_db_connection()
    curr = conn.cursor()

    curr.execute("SELECT username, password FROM users")
    users_list = curr.fetchall()

    if request.method == 'POST':
        in_name = request.form['name']
        in_user = request.form['username']
        in_pass = request.form['password']
        in_mail = request.form['email']
        if [in_user, in_pass] not in users_list:
            curr.execute("INSERT INTO users (name, username, password, email) VALUES (%s, %s, %s, %s)", [in_name, in_user, in_pass, in_mail])
            conn.commit()
            
            curr.close()
            conn.close()
            return redirect(url_for('login'))
        else:
            curr.close()
            conn.close()
            return redirect(url_for('register',error='existingaccount'))

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/", methods=["POST", "GET"])
def logins():

    conn = get_db_connection()
    curr = conn.cursor()

    curr.execute("SELECT username, password FROM users")
    users_list = curr.fetchall()

    if request.method == 'POST':
        in_user = request.form['username']
        in_pass = request.form['password']

        if (in_user, in_pass) in users_list:
            curr.execute("SELECT name FROM users WHERE username = %s AND password = %s", [in_user, in_pass])
            name = curr.fetchone()
            curr.execute("SELECT email FROM users WHERE username = %s AND password = %s", [in_user, in_pass])
            email = curr.fetchone()

            active_user = [name, in_user, in_pass, email]

            curr.close()
            conn.close()
            return redirect(url_for('shop', active_user=active_user))
        else:
            return redirect(url_for('login',error='faillogin'))

@app.route("/shop/active_user")
def shop(active_user):
    return render_template("shop.html", active_user=active_user)

@app.route("/shop/active_user", methods=["POST", "GET"])
def purchase(active_user):

    conn = get_db_connection()
    curr = conn.cursor()

    active_user = active_user

    if request.method == 'POST':
        if request.form.get('bike1'):
            curr.execute("SELECT * FROM bikes WHERE bicycle_name = 'bike1'")
            bike = curr.fetchone()
            entry = [active_user[0], active_user[1], active_user[2], active_user[3], bike[0], bike[1]]
            curr.execute("INSERT INTO orders (name, username, password, email, bicycle_name, bicycle_price) VALUES (%s, %s, %s, %s, %s, %s)", (entry[0], entry[1], entry[2], entry[3], entry[4], entry[5]))
            conn.commit()

            curr.close()
            conn.close()
            return redirect(url_for('login',error='thanks'))
        if request.form.get('bike2'):
            curr.execute("SELECT * FROM bikes WHERE bicycle_name = 'bike2'")
            bike = curr.fetchone()
            entry = [active_user[0], active_user[1], active_user[2], active_user[3], bike[0], bike[1]]
            curr.execute("INSERT INTO orders (name, username, password, email, bicycle_name, bicycle_price) VALUES (%s, %s, %s, %s, %s, %s)", (entry[0], entry[1], entry[2], entry[3], entry[4], entry[5]))
            conn.commit()

            curr.close()
            conn.close()
            return redirect(url_for('login',error='thanks'))
        if request.form.get('bike3'):
            curr.execute("SELECT * FROM bikes WHERE bicycle_name = 'bike3'")
            bike = curr.fetchone()
            entry = [active_user[0], active_user[1], active_user[2], active_user[3], bike[0], bike[1]]
            curr.execute("INSERT INTO orders (name, username, password, email, bicycle_name, bicycle_price) VALUES (%s, %s, %s, %s, %s, %s)", (entry[0], entry[1], entry[2], entry[3], entry[4], entry[5]))
            conn.commit()

            curr.close()
            conn.close()
            return redirect(url_for('login',error='thanks'))
        if request.form.get('bike4'):
            curr.execute("SELECT * FROM bikes WHERE bicycle_name = 'bike4'")
            bike = curr.fetchone()
            entry = [active_user[0], active_user[1], active_user[2], active_user[3], bike[0], bike[1]]
            curr.execute("INSERT INTO orders (name, username, password, email, bicycle_name, bicycle_price) VALUES (%s, %s, %s, %s, %s, %s)", (entry[0], entry[1], entry[2], entry[3], entry[4], entry[5]))
            conn.commit()

            curr.close()
            conn.close()
            return redirect(url_for('login',error='thanks'))
        if request.form.get('bike5'):
            curr.execute("SELECT * FROM bikes WHERE bicycle_name = 'bike5'")
            bike = curr.fetchone()
            entry = [active_user[0], active_user[1], active_user[2], active_user[3], bike[0], bike[1]]
            curr.execute("INSERT INTO orders (name, username, password, email, bicycle_name, bicycle_price) VALUES (%s, %s, %s, %s, %s, %s)", (entry[0], entry[1], entry[2], entry[3], entry[4], entry[5]))
            conn.commit()

            curr.close()
            conn.close()
            return redirect(url_for('login',error='thanks'))
        if request.form.get('bike6'):
            curr.execute("SELECT * FROM bikes WHERE bicycle_name = 'bike6'")
            bike = curr.fetchone()
            entry = [active_user[0], active_user[1], active_user[2], active_user[3], bike[0], bike[1]]
            curr.execute("INSERT INTO orders (name, username, password, email, bicycle_name, bicycle_price) VALUES (%s, %s, %s, %s, %s, %s)", (entry[0], entry[1], entry[2], entry[3], entry[4], entry[5]))
            conn.commit()

            curr.close()
            conn.close()
            return redirect(url_for('login',error='thanks'))
        if request.form.get('bike7'):
            curr.execute("SELECT * FROM bikes WHERE bicycle_name = 'bike7'")
            bike = curr.fetchone()
            entry = [active_user[0], active_user[1], active_user[2], active_user[3], bike[0], bike[1]]
            curr.execute("INSERT INTO orders (name, username, password, email, bicycle_name, bicycle_price) VALUES (%s, %s, %s, %s, %s, %s)", (entry[0], entry[1], entry[2], entry[3], entry[4], entry[5]))
            conn.commit()

            curr.close()
            conn.close()
            return redirect(url_for('login',error='thanks'))
        if request.form.get('bike8'):
            curr.execute("SELECT * FROM bikes WHERE bicycle_name = 'bike8'")
            bike = curr.fetchone()
            entry = [active_user[0], active_user[1], active_user[2], active_user[3], bike[0], bike[1]]
            curr.execute("INSERT INTO orders (name, username, password, email, bicycle_name, bicycle_price) VALUES (%s, %s, %s, %s, %s, %s)", (entry[0], entry[1], entry[2], entry[3], entry[4], entry[5]))
            conn.commit()

            curr.close()
            conn.close()
            return redirect(url_for('login',error='thanks'))
        if request.form.get('bike9'):
            curr.execute("SELECT * FROM bikes WHERE bicycle_name = 'bike9'")
            bike = curr.fetchone()
            entry = [active_user[0], active_user[1], active_user[2], active_user[3], bike[0], bike[1]]
            curr.execute("INSERT INTO orders (name, username, password, email, bicycle_name, bicycle_price) VALUES (%s, %s, %s, %s, %s, %s)", (entry[0], entry[1], entry[2], entry[3], entry[4], entry[5]))
            conn.commit()

            curr.close()
            conn.close()
            return redirect(url_for('login',error='thanks'))
        if request.form.get('bike10'):
            curr.execute("SELECT * FROM bikes WHERE bicycle_name = 'bike10'")
            bike = curr.fetchone()
            entry = [active_user[0], active_user[1], active_user[2], active_user[3], bike[0], bike[1]]
            curr.execute("INSERT INTO orders (name, username, password, email, bicycle_name, bicycle_price) VALUES (%s, %s, %s, %s, %s, %s)", (entry[0], entry[1], entry[2], entry[3], entry[4], entry[5]))
            conn.commit()

            curr.close()
            conn.close()
            return redirect(url_for('login',error='thanks'))

if __name__ == '__main__':
   app.run(debug=True)