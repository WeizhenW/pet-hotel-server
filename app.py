#main python server file

from flask import Flask
from flask import jsonify

app = Flask(__name__)

#import module to connect to db
import psycopg2
import psycopg2.extras

# create the connect via psycopg2 module
conn = psycopg2.connect(host="localhost", database="pet_hotel")
cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

@app.route('/api/owners')
def home_route():
    cur.execute('SELECT owner.id, owner.name, COUNT(pet.id) FROM owner JOIN pet on pet.owner_id = owner.id GROUP BY owner.id;')
    owners = cur.fetchall()
    return jsonify(owners)