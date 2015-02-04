from flask import Flask
from flask import request
import sqlite3
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def todo():
    import pdb; pdb.set_trace()
    if request.method == 'POST':
        insert = 'INSERT INTO todo VALUES(' + request.form['category'] + ','\
                + request.form['priority'] + ',' + request.form['description'] + ')'
        c.execute(insert)
    
    response = '''<form method="POST" action='/'>
        Category: <input type="text" name="category"/></br>
        Priority: <input type="text" name="priority"/></br>
        Description: <input type="text" name="description"/></br>
        <input type="submit"/>
        </form>
        ''' 
    for row in c.execute("Select * from todo"):
        pass
    return response

if __name__ == '__main__':
    conn = sqlite3.connect('sample.db')
    c = conn.cursor()
    app.run()
