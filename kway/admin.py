# -*- coding: utf-8 -*-

from django.contrib import admin
from django.db import models
from django.db.models import Q
from django.forms import Textarea

from kway.models import KText
from kway import settings, utils

try:
    from modeltranslation.admin import TabbedTranslationAdmin as __KTextAdminBaseClass

except ImportError:
    
    __KTextAdminBaseClass = admin.ModelAdmin
    
    
class BlankListFilter(admin.SimpleListFilter):
    
    title = 'blank'
    parameter_name = 'blank'

    def lookups(self, request, model_admin):
        
        lookups_values = ()
        
        for language in settings.KWAY_LANGUAGES:
            
            lookups_values += ((language[0], language[1], ), )
            
        return lookups_values
        
    def queryset(self, request, queryset):
        
        value = self.value()
        
        if value:
            
            value_key = utils.get_localized_value_field_name(self.value())
            
            value_isnull = {}
            value_isnull[ value_key + '__isnull' ] = True
            
            value_isempty = {}
            value_isempty[ value_key + '__exact' ] = ''
            
            return queryset.filter(Q( **value_isnull ) | Q( **value_isempty ))
        
        else:
            return queryset
        
        
class KTextAdmin(__KTextAdminBaseClass):
    
    actions = None
    
    value_fields = ()
    
    for language in settings.KWAY_LANGUAGES:
        value_fields += (utils.get_localized_value_field_name(language[0]), )
        
    list_display = ('key', ) + value_fields
    
    if settings.KWAY_ADMIN_LIST_EDITABLE:
        list_editable = value_fields
    
    list_filter = (BlankListFilter, )
    list_per_page = settings.KWAY_ADMIN_LIST_PER_PAGE
    
    readonly_fields = ('key', )
    
    def get_readonly_fields(self, request, obj = None):
        return () if request.user.is_superuser else self.readonly_fields
    
    search_fields = ('key', ) + value_fields
    
    fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('key', ) + value_fields
        }),
    )
    
    save_on_top = True
    
    def has_add_permission(self, request, obj = None):
        return request.user.is_superuser
        
    def has_delete_permission(self, request, obj = None):
        return request.user.is_superuser
        
    formfield_overrides = {
        models.TextField:{ 'widget':Textarea( attrs = { 'rows':3, 'cols':25 } ) },
    }
    
admin.site.register(KText, KTextAdmin)

