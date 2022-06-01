import markdown
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from usercrud.query import user_by_id
from calcrud.model import Calendar


# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_calendar = Blueprint('calendar', __name__,
                         url_prefix='/calcrud',
                         template_folder='templates/',
                         static_folder='static',
                         static_url_path='static')

def calendar_all_alc():
    table = Calendar.query.all()
    json_ready = [peep.read() for peep in table]
    return json_ready

@app_calendar.route('/')
@login_required
def calendar():
    # defaults are empty, in case user data not found
    user = ""
    list_calendar = []

    # grab user database object based on current login
    uo = user_by_id(current_user.userID)

    # if user object is found
    if uo is not None:
        user = uo.read()  # extract user record (Dictionary)
        print(uo)
        print(user)
        print(uo.calendar)
        for content in uo.calendar:  # loop through each user note
            print(content)
            content = content.read()  # extract note record (Dictionary)
            content['content'] = markdown.markdown(content['content'])  # convert markdown to html
            list_calendar.append(content)  # prepare note list for render_template
        if list_calendar is not None:
            list_calendar.reverse()
    # render user and note data in reverse chronological order(display latest notes rec on top)
    print(list_calendar)
    return render_template('calendar.html', user=user, calendar=list_calendar)

# Notes create/add
@app_calendar.route('/create/', methods=["POST"])
@login_required
def create():
    """gets data from form and add to Notes table"""
    if request.form:
        # construct a Notes object
        content_object = Calendar(
            request.form.get("content"), request.form.get("content2"), request.form.get("content3"), request.form.get("content4"), request.form.get("content5"), request.form.get("content6"), request.form.get("content7"), current_user.userID
        )
        # create a record in the Notes table with the Notes object
        content_object.create()
    return redirect(url_for('calendar.calendar'))

