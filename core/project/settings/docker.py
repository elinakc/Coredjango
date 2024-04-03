if IN_DOCKER:  # type:ignore
    print("Running in dockermode....")

    assert MIDDLEWARE[:1] == [  # type:ignore
        "django.middleware.security.SecurityMiddleware",
    ]
