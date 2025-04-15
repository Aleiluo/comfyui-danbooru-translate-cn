from .tag_translator import TagTranslator

NODE_CLASS_MAPPINGS = { 
    'TagTranslator': TagTranslator,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    'TagTranslator': 'Tag Translator',
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']