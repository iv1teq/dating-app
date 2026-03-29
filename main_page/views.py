import flask


def render_main_page():
    return flask.render_template("main_page.html")

def render_registration_page():
    return flask.render_template("registration_page.html")