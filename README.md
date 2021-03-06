# django-kway
django-kway is an alternative to django gettext catalog with admin integration.

#####How it works:
django-kway stores key-values in the database and caches them, so your database will not receive any query when the values will be retrieved. When a value is updated using the admin interface also its cached value will updated.

New entries are automatically created when the passed key is not present yet in the cache/database.

Values are stored using ``model.TextField``, so there is not any ``max_length`` required.


##Features

- i18n support *(supporting also multiple plural forms)*: 
  - ``kgettext("")`` function as alternative to **gettext**
  - ``{% ktrans "" %}`` template tag as alternative to **trans** template tag
- Admin integration
- Lazy [``modeltranslation``](https://github.com/deschler/django-modeltranslation) integration *(modeltranslation will be used only if already installed)*
- Caching
- Extra-settings

##Requirements
- Python 2.6, Python 2.7
- Django 1.5 through Django 1.8

##Installation

1. Run ``pip install django-kway`` or [download django-kway](http://pypi.python.org/pypi/django-kway) and add the **kway** package to your project
2. Add ``'kway'`` to ``settings.INSTALLED_APPS``
3. If you are using **South** run ``python manage.py schemamigration kway --initial`` and ``python manage.py migrate kway`` otherwise run ``python manage.py migrate``
4. If your project is multi-language run ``python manage.py makemigrations kway`` then ``python manage.py migrate kway``
5. Restart your application server

##Configuration (optional)

All these settings are optional, if not defined in ``settings.py`` the default values (listed below) will be used.

```python
#indicates if kway values can be changed directly from the admin list view
KWAY_ADMIN_LIST_EDITABLE = True

#indicates if how many kway rows will be displayed in the admin list view
KWAY_ADMIN_LIST_PER_PAGE = 100

#indicates if kway admin actions will be displayed or not
KWAY_ADMIN_SHOW_ACTIONS = False

#indicates if kway admin list_filter will be displayed or not
KWAY_ADMIN_SHOW_LIST_FILTER = True

#kway cache name, if the specified cache backend does not exist the default one will be used
KWAY_CACHE_NAME = 'kway'

#kway cache key prefix
KWAY_CACHE_KEY_PREFIX = 'kway'

#kway cache timeout (in seconds) 
#cached values are automatically updated on admin save
KWAY_CACHE_TIMEOUT = (60 * 60 * 24) #1 day

#kway languages list
#you can specify the languages list as in settings.LANGUAGES
KWAY_LANGUAGES = settings.LANGUAGES

#if True and settings.DEBUG returns "[[ key ]]" instead of an empty string
KWAY_USE_KEY_AS_DEBUG_VALUE = True

#if True and a default value is not specified the key will be stored also as value
#(only if the key has not been created yet)
KWAY_USE_KEY_AS_DEFAULT_VALUE = False

#if True and value is not set returns the key
KWAY_USE_KEY_AS_VALUE = False
```

##Usage

####Python

```python
from kway import kgettext as _

#basic
_('mykey')

#pass a default value to store if the key does not exist yet
_('mykey', default='myvalue')

#pass arguments to a value that needs to be formatted
#let's suppose that mykey value is 'Hello, my name is %(firstname)s %(lastname)s'
_('mykey', firstname='Fabio', lastname='Caccamo')

#basic plural form usage, if count matches a plural-form then key plural will be used
_('mykey', 'mykey_plural', count=3)

#advanced plural form usage, some languages support multiple plural forms, 
#if count matches a plural-form 'n' then key plural will be used by replacing %s with 'n'
_('mykey', 'mykey_plural_%s', count=3)

#in this case it's also possible to use a single key
#if the count is singular, the plural-form 'n' received will be '0'
_('mykey_%s', count=3)
```

####Template

```python
{% load kway_tags %}

#basic
{% ktrans "mykey" %}

#pass a default value to store if the key does not exist yet
{% ktrans "mykey" default="myvalue" %}

#pass arguments to a value that needs to be formatted
#let's suppose that mykey value is 'Hello, my name is %(firstname)s %(lastname)s'
{% ktrans "mykey" firstname="Fabio" lastname="Caccamo" %}

#basic plural form usage, if count matches a plural-form then key plural will be used
{% ktrans "mykey" "mykey_plural" count=3 %}

#advanced plural form usage, some languages support multiple plural forms, 
#if count matches a plural-form 'n' then key plural will be used by replacing %s with 'n'
{% ktrans "mykey" "mykey_plural_%s" count=3 %}

#in this case it's also possible to use a single key
#if the count is singular, the plural-form 'n' received will be '0'
{% ktrans "mykey_%s" count=3 %}
```

##TODO
- Import/Export CSV
- Google Translate suggestions

##License
Released under [MIT License](LICENSE).
