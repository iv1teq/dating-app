from .settings import app
from main_page import *

main_page.add_url_rule(
    rule="/",
    view_func = render_main_page
)

registration_page.add_url_rule(
    rule="/registration",
    view_func = render_registration_page
)

login_page.add_url_rule(
    rule = "/login",
    view_func = render_login_page
)

