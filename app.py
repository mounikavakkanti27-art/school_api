from flask import Flask, request, jsonify
from flask_cors import CORS
from db import get_connection

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "School API is running"

@app.route('/students', methods=['POST'])
def add_student():
    try:
        data = request.get_json() #get request body as json 

        conn = get_connection() #helps to form connection to the database
        cur = conn.cursor() #helps to execute sql queries and fetch results from the database

        cur.execute("""
            INSERT INTO "studentDB".students 
            (first_name, last_name, address, city, monitored_by)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING student_id
        """, (
            data['first_name'],
            data['last_name'],
            data['address'],
            data['city'],
            data['monitored_by']
        )) #execute the sql query to insert a new student record into the students table. The RETURNING clause is used to get the generated student_id of the newly inserted record.    

        student_id = cur.fetchone()[0] #fetchone() retrieves the next row of a query result set, returning a single sequence, or None when no more data is available. [0] is used to access the first element of the returned sequence, which is the student_id.
        
        conn.commit() #commit the transaction to save the changes to the database. This is necessary after executing an INSERT, UPDATE, or DELETE statement to ensure that the changes are persisted in the database.

        cur.close() #close the cursor to free up resources. This is important to prevent memory leaks and ensure that database connections are properly managed.
        conn.close()#close the database connection to free up resources. This is important to prevent memory leaks and ensure that database connections are properly managed.

        return jsonify({
            "student_id": student_id,
            **data
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/students', methods=['GET'])
def get_students():
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute('SELECT * FROM "studentDB".students')
        rows = cur.fetchall()

        cur.close()
        conn.close()

        result = []
        for r in rows:
            result.append({
                "student_id": r[0],
                "first_name": r[1],
                "last_name": r[2],
                "address": r[3],
                "city": r[4],
                "monitored_by": r[5]
            })

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5001)