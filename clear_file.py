import os
import shutil


class AnyType(str):
    """A special class that is always equal in not equal comparisons. Credit to pythongosssss"""

    def __ne__(self, __value: object) -> bool:
        return False


any_type = AnyType("*")


class clear_file:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "any": (any_type, {}),
                "path": ("STRING", {}),
                "is_enable": ("BOOLEAN", {"default": True}),
            },
        }

    RETURN_TYPES = (any_type,)
    RETURN_NAMES = ("any",)

    FUNCTION = "clear"

    OUTPUT_NODE = True

    CATEGORY = "aleiluo tools"

    def clear(self, any, path,is_enable):
        if not is_enable:
            return (None,)
        out = any
        # 如果path存在，删除这个文件或文件夹
        if os.path.exists(path):
            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                shutil.rmtree(path)
        return (out,)
