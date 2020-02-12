from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATBASE_URI'] = 'sqlite:///dss.db'  #///gives relateive path - 4/ would be absolute
db = SQLAlchemy(app)



class Forum(db.Model):
    __tablename__ = "forum1"
    entryID = db.Column(db.Integer, primary_key=True)
    name = db.column(db.String(100))
    Entry = db.column(db.String(250))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)


        # returns string when new task is performed?
    def def__repr__(self):
        return '<Task %r>' % self.id




@app.route('/')
def index():
    return render_template("index.html")



           
if __name__ == "__main__":
    app.run(debug=True)


    # path \\Scripts\\activate.bat ??
    #
    #   refs     https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/ 
    #   install modules -- pip install <package>
    #   