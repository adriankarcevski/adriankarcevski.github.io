#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Adrian Karcevski'
SITENAME = "Adrian Karcevski"
SITEURL = ''
TIMEZONE = 'America/New_York'

PATH = 'content'
STATIC_PATHS = ['images', 'files']
USER_LOGO_URL = '/images/logo.png'
GITHUB_URL = 'https://github.com/adriankarcevski/'

DEFAULT_LANG = 'en'

THEME = '/home/t/pelican-themes/pelican-themes/medius'
DEFAULT_CATEGORY = 'misc'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# # Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/adriankarcevski'),
          ('Linkedin', 'https://www.linkedin.com/in/adrian-karcevski-061a31109'),)



DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MEDIUS_CATEGORIES = {
    'Projects': {
        'description': 'list of posts related to projects',
        'logo': '/images/engine.jpg',
        'thumbnail': '/images/f1-red.png',
    },

    'Python': {
        'description': 'things done with <3 in Python',
        'logo': '/images/py3.jpg',
        'thumbnail': '/images/snake.png',
    },

    'Linux': {
        'description': 'things done using magic in Linux',
        'logo': '/images/drone.jpg',
        'thumbnail': '/images/term.png'
    }
}


MEDIUS_AUTHORS = {
    'Adrian Karcevski': {
        'description':"""
            I read a lot about technical topics related to IT.
        """,
        'cover': '/images/profile.png',
        'image': '/images/ninja.png',
        'links': (('github', 'https://github.com/adriankarcevski'),)
    }
}