AUTHOR = "Transport Data Commons Initiative"
SITENAME = "Transport Data Commons"
SITEURL = ""

PATH = "content"

TIMEZONE = "Europe/Rome"

DEFAULT_LANG = "en"

THEME = "pelican-bootstrap3"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

# For pelican-bootstrap3
PLUGINS = ["i18n_subsites"]
PLUGIN_PATHS = ["pelican-plugins"]
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
