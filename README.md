# django-kway
django-kway is an alternative to django gettext catalog with admin integration.

##Features:

- i18n support *(supporting also multiple plural forms)*: 
  - ``kgettext("")`` function as alternative to **gettext**
  - ``{% ktrans "" %}`` template tag as alternative to **trans** template tag
- Admin integration
- Lazy [``modeltranslation``](https://github.com/deschler/django-modeltranslation) integration *(modeltranslation will be used only if already installed)*
- Caching
- Extra-settings

##Installation:

1. Run ``pip install django-kway`` or [download django-kway](http://pypi.python.org/pypi/django-kway) and add the **kway** package to your project
2. Add ``'kway'`` to ``settings.INSTALLED_APPS``
3. Are you using **South**?
 - ``python manage.py schemamigration kway --initial``
 - ``python manage.py migrate kway``

 otherwise:
 - ``python manage.py syncdb``
4. Restart you application server

##Configuration (optional):

All these settings are optional, if not re-defined in ``settings.py`` the default values (listed below) will be used.

```python
#indicate if kway values can be changed directly from the admin list view
KWAY_ADMIN_LIST_EDITABLE = True

#indicate if how many kway rows will be displayed in the admin list view
KWAY_ADMIN_LIST_PER_PAGE = 100

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

##Usage:
TODO

##TODO:
- Import/Export CSV
- Google Translate suggestions