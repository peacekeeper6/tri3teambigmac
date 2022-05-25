import markdown
from flask import render_template
from flask_login import current_user

from __init__ import app

from usercrud.app_crud import app_crud
from timelinecrud.app_timeline import app_timeline
from announcementcrud.app_announcement import app_announcement
# from cruddy.app_crud_api import app_crud_api
from usercrud.query import user_by_id
from announcementcrud.app_announcement import ann_all_alc

app.register_blueprint(app_crud)
app.register_blueprint(app_timeline)
app.register_blueprint(app_announcement)
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

@app.route('/GetInvolved')
def GetInvolved():
    return render_template("Gallery/GetInvolved.html")

@app.errorhandler(404)
def error(e):
    return render_template("404.html"), 404

@app.route('/displayannouncement')
def displayannouncement():
    # # defaults are empty, in case user data not found
    # user = ""
    # list_announcement = []
    # print("in announcement")
    # # grab user database object based on current login
    # uo = user_by_id(current_user.userID)
    #
    # # if user object is found
    # if uo is not None:
    #     user = uo.read()  # extract user record (Dictionary)
    #     if uo.announcement is None:
    #         print("about to die")
    #     for content in uo.announcement:  # loop through each user note
    #         print(content)
    #         content = content.read()  # extract note record (Dictionary)
    #         content['content'] = markdown.markdown(content['content'])  # convert markdown to html
    #         list_announcement.append(content)  # prepare note list for render_template
    #     if list_announcement is not None:
    #         list_announcement.reverse()
    # # render user and note data in reverse chronological order(display latest notes rec on top)
    # print(list_announcement)
    list_announcement = ann_all_alc()
    print(list_announcement)
    if list_announcement is not None:
        list_announcement.reverse()
    return render_template('displayannouncement.html', ann=list_announcement)

@app.route('/oceaninformation')
def oceaninformation():
    return render_template("oceaninformation.html")

@app.route('/oceanquiz')
def oceanquiz():
    return render_template("oceanquiz.html")

@app.route('/meettheteam')
def meettheteam():
    return render_template("meettheteam.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
