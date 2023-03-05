AUTHOR = "Transport Data Commons Initiative"
SITENAME = "Transport Data Commons"
SITEURL = ""

PATH = "content"
ARTICLE_PATHS = [
    "",
    "event",
]
PAGE_PATHS = [
    "page",
]

TIMEZONE = "Europe/Rome"

DEFAULT_LANG = "en"

THEME = "pelican-bootstrap3"

CC_LICENSE = "CC-BY-NC-ND"
MENUITEMS = [
    ("Discuss", "https://github.com/orgs/transport-data/discussions"),
]


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}/index.html"

# For pelican-bootstrap3
PLUGINS = ["i18n_subsites"]
PLUGIN_PATHS = ["pelican-plugins"]
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
