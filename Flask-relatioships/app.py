from flask import Flask
from extensions import db
from api.views import blueprint

app = Flask(__name__)


app.register_blueprint(blueprint=blueprint)
app.config.from_object('config')


db.init_app(app)


if __name__=='__main__':
    app.run(debug=True)