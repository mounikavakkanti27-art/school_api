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
        data = request.get_json()

        conn = get_connection()
        cur = conn.cursor()

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
        ))

        student_id = cur.fetchone()[0]
        conn.commit()

        cur.close()
        conn.close()

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