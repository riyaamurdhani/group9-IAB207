from app import create_app, db
from flask import Flask
from app.routes.index import register_routes

app = create_app()
register_routes(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
