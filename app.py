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
def owner_route():
    cur.execute('SELECT * FROM owner')
    owners = cur.fetchall()
    return jsonify(owners)

@app.route('/api/pets')
def pet_route():
    cur.execute('SELECT "pet".*, "owner"."name" as "owner_name" FROM "pet" JOIN "owner" ON "owner"."id" = "pet"."owner_id" ORDER BY "pet"."id";')
    pets = cur.fetchall()
    return jsonify(pets)
