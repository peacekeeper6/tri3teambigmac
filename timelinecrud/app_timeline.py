import markdown
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from usercrud.query import user_by_id
from timelinecrud.model import Timeline
from datetime import datetime
import pytz

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_timeline = Blueprint('timeline', __name__,
                      url_prefix='/timeline',
                      template_folder='templates/timeline/',
                      static_folder='static',
                      static_url_path='static')


@app_timeline.route('/')
@login_required
def timeline():
    # defaults are empty, in case user data not found
    user = ""
    list_timeline = []

    # grab user database object based on current login
    uo = user_by_id(current_user.userID)

    # if user object is found
    if uo is not None:
        user = uo.read()  # extract user record (Dictionary)
        print(uo)
        print(user)
        print(uo.timeline)
        for content in uo.timeline:  # loop through each user note
            print(content)
            content = content.read()  # extract note record (Dictionary)
            content['content'] = markdown.markdown(content['content'])  # convert markdown to html
            list_timeline.append(content)  # prepare note list for render_template
        if list_timeline is not None:
            list_timeline.reverse()
    # render user and note data in reverse chronological order(display latest notes rec on top)
    print(list_timeline)
    return render_template('timeline.html', user=user, timeline=list_timeline)


# Notes create/add
@app_timeline.route('/create/', methods=["POST"])
@login_required
def create():
    """gets data from form and add to Notes table"""
    if request.form:
        # construct a Notes object
        content_object = Timeline(
            request.form.get("content"), datetime.now(pytz.timezone('America/Los_Angeles')).strftime("%H:%M:%S %p %Z, %a %m/%d/%Y"), current_user.userID
        )
        # create a record in the Notes table with the Notes object
        content_object.create()
    return redirect(url_for('timeline.timeline'))
