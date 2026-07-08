"""File IO utilities for reading documents and preparing text for translation."""
import os
import re
import json
import docx
import pdfplumber
import jieba
from docx import Document
from .translate import (
    translate_with_punctuation,
    reverse_pinyin_translation,
    split_long_text,
    read_pdf as translate_read_pdf,
    read_word as translate_read_word,
    CUSTOM_TRANSLATION_DICT,
)


def read_pdf(file_path):
    """读取 PDF 文件内容"""
    return translate_read_pdf(file_path)


def read_word(file_path):
    """读取 Word 文件内容"""
    return translate_read_word(file_path)


def load_custom_dict(file_path="custom_dict.json"):
    """加载自定义翻译字典并更新 jieba 词典"""
    try:
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                custom_dict = json.load(f)
                for word in custom_dict.keys():
                    jieba.add_word(word)
                return custom_dict
        return {}
    except Exception as e:
        print(f"加载自定义字典失败: {str(e)}")
        return {}


def process_file(file_path: str, tone_style):
    """Read a file and return a list of translated segments (strings)."""
    if file_path.endswith('.pdf'):
        content = read_pdf(file_path)
    elif file_path.endswith('.docx'):
        content = read_word(file_path)
    else:
        # Fallback to reading text file with best-effort encoding detection
        try:
            import chardet
            with open(file_path, 'rb') as f:
                raw_data = f.read()
                detected = chardet.detect(raw_data)
                encoding = detected['encoding'] if detected['encoding'] else 'utf-8'
        except Exception:
            encoding = 'utf-8'
        with open(file_path, 'r', encoding=encoding, errors='replace') as f:
            content = f.read().split('\n')

    translated = []
    for para in content:
        if para.strip():
            segments = split_long_text(para)
            for segment in segments:
                translated.append(reverse_pinyin_translation(segment, tone_style))
    return translated
