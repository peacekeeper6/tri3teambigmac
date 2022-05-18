from flask import render_template
from __init__ import app

from usercrud.app_crud import app_crud
from timelinecrud.app_timeline import app_timeline
# from cruddy.app_crud_api import app_crud_api


app.register_blueprint(app_crud)
app.register_blueprint(app_timeline)
# app.register_blueprint(app_crud_api)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("layouts/index.html")


@app.route('/signin')
def signin():
    return render_template("sign-in.html")

@app.route('/signup')
def signup():
    return render_template("sign-up.html")

@app.route('/calendar')
def calendar():
    return render_template("calendar.html")

@app.errorhandler(404)
def error(e):
    return render_template("404.html"), 404

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
