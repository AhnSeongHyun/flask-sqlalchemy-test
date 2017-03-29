from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:xxxx@xxxxx/test'
# using Flask-SQLAlchemy
db = SQLAlchemy(app)




@app.route("/")
def hello():
    from user import User
    try:
        usr = User(username='test', email='test@gmail.com')
        db.session.add(usr)
        db.session.commit()
    except:
        import traceback
        print traceback.format_exc()

    return db.session.query(User.username).first()

if __name__ == "__main__":
    db.create_all()
    app.run()