from flask import Flask, render_template
from flask_mysqldb import MySQL  # Change this line

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "vijisanjai3031"
app.config["MYSQL_DB"] = "crud"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql = MySQL(app)  # Change this line

@app.route('/')
def home():
    con = mysql.connection.cursor()  # to connect the database
    sql = "select * from users"
    con.execute(sql)
    res = con.fetchall()

    return render_template('home.html', datas=res)

if __name__ == '__main__':
    app.run(debug=True)
