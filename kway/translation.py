# -*- coding: utf-8 -*-

from kway.models import KText

try: 
    
    from modeltranslation.translator import translator, TranslationOptions
    
    
    class KTextTranslationOptions(TranslationOptions):
        
        fields = ('value', )
        
    translator.register(KText, KTextTranslationOptions)
    
    
except ImportError:
    
    pass
    
    