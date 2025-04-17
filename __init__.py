from .clear_file import clear_file
from .tag_translator import TagTranslator

NODE_CLASS_MAPPINGS = { 
    'TagTranslator': TagTranslator,
    'ClearFile': clear_file,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    'TagTranslator': 'Tag Translator',
    'ClearFile': 'Clear File'
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']