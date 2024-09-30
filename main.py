from flask import Flask, render_template, request, jsonify
import sqlite3
import random

app = Flask(__name__)

# Create a SQLite database
conn = sqlite3.connect('text_database.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS texts (id INTEGER PRIMARY KEY, content TEXT)')
conn.commit()
conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    text = request.form.get('text', '')
    if text:
        conn = sqlite3.connect('text_database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO texts (content) VALUES (?)', (text,))
        conn.commit()
        conn.close()
    return 'OK'

@app.route('/random')
def random_text():
    conn = sqlite3.connect('text_database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT content FROM texts ORDER BY RANDOM() LIMIT 1')
    result = cursor.fetchone()
    conn.close()
    return jsonify({'random_text': result[0] if result else None})

if __name__ == '__main__':
    app.run(debug=True)

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
