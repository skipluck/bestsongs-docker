# BestSongs
from flask import Flask
from flaskext.mysql import MySQL
import os
 
mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = os.environ['MYSQL_USER']
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ['MYSQL_PASSWORD']
app.config['MYSQL_DATABASE_DB'] = os.environ['MYSQL_DATABASE']
app.config['MYSQL_DATABASE_HOST'] = os.environ['MYSQL_HOST']
mysql.init_app(app)

@app.route('/')
def hello():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT song, artist FROM songs ORDER BY RAND() LIMIT 1")
    data = cursor.fetchone()
    if data is None:
     return '<html><head><title>Error</title><body><h1>Database not available!</h1></body></html>'
    else:
     return '<html><head><title>Best Songs of the Rock Era</title><body><h1>Best Songs of the Rock Era</h1><h2>{}</h2>-- {}</body></html>'.format(data[0], data[1])
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)