#main python server file

from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)

#import module to connect to db
import psycopg2
import psycopg2.extras

# create the connect via psycopg2 module
conn = psycopg2.connect(host="localhost", database="pet_hotel")
cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

# get and post routes for owners
@app.route('/api/owners', methods=['GET', 'POST', 'DELETE'])
def owner_route():
    if request.method == 'GET':
        cur.execute('SELECT owner.id, owner.name, COUNT(pet.id) FROM owner LEFT JOIN pet on pet.owner_id = owner.id GROUP BY owner.id;')
        owners = cur.fetchall()
        return jsonify(owners)
    elif request.method == 'POST':
        print(request.get_json()['name'])
        cur.execute("INSERT INTO owner (name) VALUES (%s)",(request.get_json()['name'],))
        conn.commit()
        return 'ok'
# delete owner route
@app.route('/api/owners/<owner_id>', methods=['DELETE'])
def delete_owner(owner_id):
    print(owner_id)
    cur.execute("DELETE FROM owner WHERE id = %s",(owner_id,))
    conn.commit()
    return 'ok'

#get and post route to api/pets
@app.route('/api/pets', methods=['GET', 'POST'])
def pet_route():
    if request.method == 'GET':
        cur.execute('SELECT "pet".*, "owner"."name" as "owner_name" FROM "pet" JOIN "owner" ON "owner"."id" = "pet"."owner_id" ORDER BY "pet"."id";')
        pets = cur.fetchall()
        return jsonify(pets)
    elif request.method == 'POST':
        print(request.get_json())
        cur.execute("INSERT INTO pet (name, breed, color, age, owner_id) VALUES (%s, %s, %s, %s, %s)", (request.get_json()['name'],request.get_json()['breed'],request.get_json()['color'],request.get_json()['age'],request.get_json()['owner'],))
        conn.commit()
        return 'ok'
