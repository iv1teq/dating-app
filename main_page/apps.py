import flask


main_page = flask.Blueprint(
            name = "main_page",
            import_name = __name__,
            static_folder = "static",
            template_folder = "templates",
            static_url_path = "/main_page/static"
        )

registration_page = flask.Blueprint(
            name = "registration_page",
            import_name = __name__,
            static_folder = "static",
            template_folder = "templates",
            static_url_path = "/main_page/static"
        )

