import os
import sys
base_dir = os.path.dirname(os.path.abspath(__file__))
libs_path = os.path.join(base_dir, "libs")
sys.path.insert(0, libs_path)

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog
from pypinyin import pinyin, Style
import pyperclip #安装出了问题，导致无法复制，有时间再修
import json
import jieba
from threading import Thread
import pdfplumber
import docx
import re
from docx import Document
import unicodedata
from datetime import datetime
import pyttsx3
from pydub import AudioSegment
from pydub.playback import play
import io
import threading
import time
from playsound import playsound


class ToneStyle:
    def __init__(self, name, pypinyin_style, description=""):
        self.name = name
        self.pypinyin_style = pypinyin_style
        self.description = description

TONE_STYLES = [
    ToneStyle("古韵", Style.TONE, "保留声调符号，如 nǐ"),
    ToneStyle("音韵", Style.TONE2, "用数字表示声调，如 ni3"),
    ToneStyle("无声调", Style.NORMAL, "移除所有声调符号，如 ni")
]

def clean_pinyin(pinyin_str, style):
    """严格处理不同拼音风格"""
    if style.pypinyin_style == Style.NORMAL:
        # 无声调模式：移除所有声调相关字符
        cleaned = []
        for char in pinyin_str:
            if char == ' ':
                cleaned.append(char)
                continue
            normalized = unicodedata.normalize('NFD', char)
            for c in normalized:
                if not unicodedata.combining(c):
                    cleaned.append(c)
        return ''.join(cleaned).lower().replace("ü", "v")
    
    elif style.pypinyin_style == Style.TONE2:
        # 数字声调模式：保留数字但标准化格式
        return re.sub(r'([a-zü]+)([1-4])', r'\1\2 ', pinyin_str.lower()).strip().replace("ü", "v")
    
    else:  # Style.TONE
        # 保留原始声调符号
        return pinyin_str.replace("ü", "v")

def translate_with_punctuation(text: str, tone_style) -> str:
    """
    严格按照要求的新实现：
    1. 重新定义句子（以语义完整性为单位）
    2. 每句内部分词并反转拼音
    3. 反转句子顺序
    4. 添加空格并首字母大写
    """
    print(f"原始文本: {text}")

    # 第一步：分割句子（以语义完整性为单位）
    pattern = re.compile(r'([^。！？!?]*[。！？!?])')  # 匹配完整句子，包括标点符号
    matches = pattern.findall(text)
    sentences = [match.strip() for match in matches if match.strip()]
    print(f"分割的句子: {sentences}")
    
    # 第二步：处理每个句子（分词→拼音→反转）
    processed_sentences = []
    for sentence in sentences:
        print(f"处理句子: {sentence}")
        # 去掉句尾标点符号，单独保存
        content = sentence[:-1]
        delimiter = sentence[-1]
        
        words = list(jieba.cut(content))
        print(f"分词结果: {words}")
        reversed_words = []
        for word in words:
            # 中文转拼音
            pys = pinyin(word, style=tone_style.pypinyin_style)
            py_str = ''.join([p[0] for p in pys])
            print(f"拼音: {py_str}")
            # 清洗拼音
            cleaned = clean_pinyin(py_str, tone_style)
            print(f"清洗后的拼音: {cleaned}")
            # 反转拼音
            reversed_word = cleaned[::-1]
            print(f"反转后的拼音: {reversed_word}")
            reversed_words.append(reversed_word)
        # 反转句子内部的词语顺序
        reversed_sentence = ' '.join(reversed_words[::-1])
        print(f"处理后的句子（反转词语顺序）: {reversed_sentence}")
        # 添加标点符号
        processed_sentences.append(reversed_sentence + delimiter)
    
    print(f"所有处理后的句子: {processed_sentences}")
    
    # 第三步：反转句子顺序
    processed_sentences = processed_sentences[::-1]
    print(f"反转后的句子顺序: {processed_sentences}")
    
    # 第四步：首字母大写
    result = ' '.join(processed_sentences).strip()
    if result:
        result_chars = list(result)
        capitalize_next = True  # 标记是否需要大写
        for i, c in enumerate(result_chars):
            if c.isalpha() and capitalize_next:
                result_chars[i] = c.upper()
                capitalize_next = False
            elif c in ['。', '.', '！', '？']:  # 遇到句号等标点符号时，标记下一个字母需要大写
                capitalize_next = True
        result = ''.join(result_chars)
    
    print(f"最终结果: {result}")
    return result

def translate_paragraphs(text: str, tone_style) -> str:
    """
    处理多段文字的作文，每段独立处理。
    """
    print(f"原始文本: {text}")

    # 按段落分割
    paragraphs = text.split('\n')
    print(f"分割的段落: {paragraphs}")

    # 处理每段文字
    translated_paragraphs = []
    for paragraph in paragraphs:
        if paragraph.strip():  # 跳过空段落
            translated_paragraph = translate_with_punctuation(paragraph.strip(), tone_style)
            translated_paragraphs.append(translated_paragraph)

    # 拼接段落，保留换行符
    result = '\n'.join(translated_paragraphs)
    print(f"最终结果: {result}")
    return result

# 测试代码1
#result1 = translate_with_punctuation("你好,世界。今天是个好日子,阳光明媚。我们一起去公园散步,享受美好时光。", TONE_STYLES[2])
#print(f"翻译结果: {result1}")

# 测试代码2
#essay = """第一段：你好,世界。今天是个好日子,阳光明媚。

#第二段：我们一起去公园散步,享受美好时光。生活如此美好,值得珍惜。"""
# result = translate_paragraphs(essay, TONE_STYLES[2])
# print(f"翻译结果:\n{result}")
