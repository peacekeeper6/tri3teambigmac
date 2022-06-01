import markdown
from flask import render_template
from __init__ import app
from flask_login import current_user
from announcementcrud.app_announcement import ann_all_alc, app_announcement
from calcrud.app_calendar import app_calendar, calendar_all_alc
from usercrud.query import user_by_id

from usercrud.app_crud import app_crud
from timelinecrud.app_timeline import app_timeline
# from cruddy.app_crud_api import app_crud_api


app.register_blueprint(app_crud)
app.register_blueprint(app_timeline)
app.register_blueprint(app_announcement)
app.register_blueprint(app_calendar)
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


@app.route('/GetInvolved')
def GetInvolved():
    return render_template("Gallery/GetInvolved.html")

@app.errorhandler(404)
def error(e):
    return render_template("404.html"), 404

@app.route('/displayannouncement')
def displayannouncement():
    list_announcement = ann_all_alc()
    print(list_announcement)
    if list_announcement is not None:
        list_announcement.reverse()
    return render_template('displayannouncement.html', ann=list_announcement)

@app.route('/oceaninformation')
def oceaninformation():
    return render_template("oceaninformation.html")

@app.route('/oceanquiz/')
def oceanquiz():
    return render_template("oceanquiz/templates/oceanquiz.html")

@app.route('/meettheteam')
def meettheteam():
    return render_template("meettheteam.html")

@app.route('/displaycal')
def displaycal():
    list_calendar = calendar_all_alc()
    print(list_calendar)
    if list_calendar is not None:
        list_calendar.reverse()
    return render_template('displaycal.html', calendar=list_calendar)

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
