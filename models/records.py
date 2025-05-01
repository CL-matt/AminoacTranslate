import json
import jieba
import os

def load_custom_dict(file_path="custom_dict.json"):
    """加载自定义翻译字典并更新 jieba 词典"""
    try:
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                custom_dict = json.load(f)
                for word in custom_dict.keys():
                    jieba.add_word(word)
                return custom_dict
        else:
            return {}
    except Exception as e:
        print(f"加载自定义字典失败: {str(e)}")
        return {}

CUSTOM_TRANSLATION_DICT = load_custom_dict()