TEMPLATES = [
    {
        ............,
        'DIRS': [os.path.join(BASE_DIR, "build"),],   // add this
        'APP_DIRS': True,
        'OPTIONS': {-----
        },
    },
]


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "build/static"), // add this
]
