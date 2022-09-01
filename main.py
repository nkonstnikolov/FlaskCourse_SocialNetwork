from config import create_app
from db import db
from models.user import UserModel


app = create_app()


@app.after_request
def close_request(response):
    db.session.commit()
    return response

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)