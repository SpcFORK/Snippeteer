from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from threading import Thread
import sqlite3
from datetime import datetime

app = Flask(__name__)
DATABASE = 'snippets.db'


# Database initialization
def initialize_database():
  conn = sqlite3.connect(DATABASE)
  c = conn.cursor()
  c.execute('''CREATE TABLE IF NOT EXISTS snippets
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  code TEXT NOT NULL,
                  language TEXT NOT NULL,
                  created_at TEXT NOT NULL,
                  likes INTEGER NOT NULL DEFAULT 0)''')
  conn.commit()
  conn.close()


# Upload a code snippet
@app.route('/snippets', methods=['POST'])
def create_snippet():
  code = request.json['code']
  language = request.json['language']
  created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  conn = sqlite3.connect(DATABASE)
  c = conn.cursor()
  c.execute(
    "INSERT INTO snippets (code, language, created_at) VALUES (?, ?, ?)",
    (code, language, created_at))
  conn.commit()
  conn.close()
  return jsonify({'message': 'Snippet created successfully'}), 201


# View all snippets
@app.route('/snippets', methods=['GET'])
def get_all_snippets():
  conn = sqlite3.connect(DATABASE)
  c = conn.cursor()
  c.execute("SELECT * FROM snippets")
  snippets = [{
    'id': row[0],
    'code': row[1],
    'language': row[2],
    'created_at': row[3],
    'likes': row[4]
  } for row in c.fetchall()]
  conn.close()
  return jsonify(snippets), 200


# Upvote a snippet
@app.route('/snippets/<int:snippet_id>/like', methods=['PUT'])
def like_snippet(snippet_id):
  conn = sqlite3.connect(DATABASE)
  c = conn.cursor()
  c.execute("UPDATE snippets SET likes = likes + 1 WHERE id = ?",
            (snippet_id, ))
  conn.commit()
  conn.close()
  return jsonify({'message': 'Snippet liked successfully'}), 200


# Filter snippets by language or creation date or likes
@app.route('/snippets/filter', methods=['GET'])
def filter_snippets():
  language = request.args.get('language')
  created_at = request.args.get('created_at')
  likes = request.args.get('likes')
  conn = sqlite3.connect(DATABASE)
  c = conn.cursor()
  query = "SELECT * FROM snippets WHERE 1=1"
  params = []
  if language:
    query += " AND language = ?"
    params.append(language)
  if created_at:
    query += " AND created_at >= ?"
    params.append(created_at)
  if likes:
    query += " AND likes >= ?"
    params.append(likes)
  c.execute(query, tuple(params))
  snippets = [{
    'id': row[0],
    'code': row[1],
    'language': row[2],
    'created_at': row[3],
    'likes': row[4]
  } for row in c.fetchall()]
  conn.close()
  return jsonify(snippets), 200


@app.route('/')
def home():
  return f"<h1>😎I'm Awake Already!🔥</h1>"


def run():
  # app.run(host='0.0.0.0',port=8080)
  pass


def keep_alive():
  # t = Thread(target=run)
  # t.start()
  pass


if __name__ == '__main__':
  keep_alive()

  # Don't put anything below unless needed...

  initialize_database()
  # app.run()
  
  app.run(host='0.0.0.0', port=8080)
