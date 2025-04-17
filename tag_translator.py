import json
import os
import re


class TagTranslator:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            'required': {
                "text": ("STRING", {"forceInput": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = 'process'
    CATEGORY = 'aleiluo tools'
    
    def process(self, text):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        json_file_path = os.path.join(script_dir, 'danbooru-cn.json')
        
        with open(json_file_path, 'r', encoding='utf-8') as f:
            tag_dict = json.load(f)

        tags = [tag.strip() for tag in re.split(r'[,\n]+', text) if tag.strip()]
        translated_tags = []
        
        for tag in tags:
            # 将下划线替换为空格
            tag = tag.replace('_', ' ')
            
            # 去除括号中的转义符
            tag = tag.replace(r'\(', '(').replace(r'\)', ')')
            
            # 查找字典中是否有该 key
            translated_value = tag_dict.get(tag)
            
            if translated_value:
                # 如果字典中找到了对应的中文值，加入到翻译列表
                translated_tags.append(translated_value)
            else:
                # 如果没有找到对应的中文值，保留原标签
                translated_tags.append(tag)
        
        # 使用 ', ' 拼接翻译后的标签
        translated_text = ', '.join(translated_tags)
        
        return (translated_text,)