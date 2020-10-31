from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_i3yc&@i5$y+k-^(cr-jk8%%p1-m#-hg79lyh!x6_-d86t$l_!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mainapp',
    'django_cleanup',
    'sorl.thumbnail',
    'ckeditor',
    'ckeditor_uploader',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangoex.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangoex.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]


MEDIA_ROOT = "media/"
MEDIA_URL = '/media/'


EMAIL_HOST = 'smtp.mail.ru'
EMAIL_PORT = 2525
EMAIL_HOST_USER = "sonikry.99@mail.ru"
EMAIL_HOST_PASSWORD = "1999.Sonikry"
EMAIL_USE_TLS = True



CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_FILENAME_GENERATOR = 'utils.get_filename'

CKEDITOR_CONFIGS = {
    'default1': {
        'toolbar': 'full',
    },
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            # ['Source', '-', 'Preview', 'Table', 'Textarea', 'Templates', '-', 'Undo', 'Redo', 'Image', 'Image2'],
            # ['Source', '-', 'Bold', 'Italic'],
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'image2', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
{'extraPlugins': ','.join([
            'uploadimage',
            'image2',
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath'
            ]),},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            # {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize'],},
        ],
    },








    'default555': {
        # 'skin': 'Kama',
        'skin': 'moono',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'image2', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',
                'image2',
                'imageuploader'

            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage', # the upload image feature
            # your extra plugins here
            'div',
            'image2',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath',
        ]),
    }
}













# customColorPalette = [
#         {
#             'color': 'hsl(4, 90%, 58%)',
#             'label': 'Red'
#         },
#         {
#             'color': 'hsl(340, 82%, 52%)',
#             'label': 'Pink'
#         },
#         {
#             'color': 'hsl(291, 64%, 42%)',
#             'label': 'Purple'
#         },
#         {
#             'color': 'hsl(262, 52%, 47%)',
#             'label': 'Deep Purple'
#         },
#         {
#             'color': 'hsl(231, 48%, 48%)',
#             'label': 'Indigo'
#         },
#         {
#             'color': 'hsl(207, 90%, 54%)',
#             'label': 'Blue'
#         },
#     ]
#
#
#
#
#
# CKEDITOR_5_CONFIGS = {
#     'default': {
#         'toolbar': ['heading', '|', 'bold', 'italic', 'link',
#                     'bulletedList', 'numberedList', 'blockQuote', 'imageUpload', ],
#
#     },
#     'extends': {
#         'blockToolbar': [
#             'paragraph', 'heading1', 'heading2', 'heading3',
#             '|',
#             'bulletedList', 'numberedList',
#             '|',
#             'blockQuote', 'imageUpload'
#         ],
#         'toolbar': ['heading', '|', 'outdent', 'indent', '|', 'bold', 'italic', 'link', 'underline', 'strikethrough',
#         'code', 'subscript', 'superscript', 'highlight', '|',
#                     'bulletedList', 'numberedList', 'todoList', '|',  'blockQuote', 'imageUpload', '|',
#                     'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'mediaEmbed', 'removeFormat',
#                     'insertTable',],
#         'image': {
#             'toolbar': ['imageTextAlternative', 'imageTitle', '|', 'imageStyle:alignLeft', 'imageStyle:full',
#                         'imageStyle:alignRight', 'imageStyle:alignCenter', 'imageStyle:side',  '|'],
#             'styles': [
#                 'full',
#                 'side',
#                 'alignLeft',
#                 'alignRight',
#                 'alignCenter',
#             ]
#
#         },
#         'table': {
#             'contentToolbar': [ 'tableColumn', 'tableRow', 'mergeTableCells',
#             'tableProperties', 'tableCellProperties' ],
#             'tableProperties': {
#                 'borderColors': customColorPalette,
#                 'backgroundColors': customColorPalette
#             },
#             'tableCellProperties': {
#                 'borderColors': customColorPalette,
#                 'backgroundColors': customColorPalette
#             }
#         },
#         'heading' : {
#             'options': [
#                 { 'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph' },
#                 { 'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1' },
#                 { 'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2' },
#                 { 'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3' }
#             ]
#         }
#     },
#     # 'mypreset': {
#     #     "removePlugins": "stylesheetparser",
#     #     'allowedContent': True,
#     #     'toolbar_Full': [
#     #     ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat' ],
#     #     ['Image', 'Flash', 'Table', 'HorizontalRule'],
#     #     ['TextColor', 'BGColor'],
#     #     ['Smiley','sourcearea', 'SpecialChar'],
#     #     [ 'Link', 'Unlink', 'Anchor' ],
#     #     [ 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl', 'Language' ],
#     #     [ 'Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates' ],
#     #     [ 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo' ],
#     #     [ 'Find', 'Replace', '-', 'SelectAll', '-', 'Scayt' ],
#     #     [ 'Maximize', 'ShowBlocks' ]
#     #     ]
#     # },
#     'default2': {
#         'toolbar': ['Source', 'Bold', 'Italic', 'Underline', 'BulletedList', 'Link', 'Unlink', 'JustifyLeft',
#                     'JustifyCenter', 'JustifyRight', 'JustifyBlock', 'Font', 'FontSize', 'TextColor', 'About',
#                     'NewPage', 'Preview', 'Templates', 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', 'Undo',
#                     'Redo', 'Strike', 'Image', 'Table', 'HorizontalRule', 'BGColor', 'Liststyle', 'NumberedList',
#                     'BulletedList','Outdent','Indent','Blockquote'
#             # 'Source', '-', 'ExportPdf', 'Print'
#         ],
#     },
# }