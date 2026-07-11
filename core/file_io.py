"""
文件读写操作模块
"""
import os
import re
import docx
import json
import pdfplumber
from docx import Document
from .translation import translate_with_punctuation

def read_pdf(file_path):
    """读取 PDF 文件内容"""
    content = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                content.extend(text.split('\n'))
    return [line.strip() for line in content if line.strip()]

def read_word(file_path):
    """读取 Word 文件内容"""
    content = []
    doc = docx.Document(file_path)
    for paragraph in doc.paragraphs:
        if paragraph.text.strip():
            content.append(paragraph.text.strip())
    return content

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

def split_long_text(text, max_length=50):
    """将长文本按标点符号或固定长度分段"""
    sentences = re.split(r'(。|！|\!|\.|？|\?)', text)
    segments = []
    current_segment = ""
    for sentence in sentences:
        if len(current_segment) + len(sentence) <= max_length:
            current_segment += sentence
        else:
            segments.append(current_segment)
            current_segment = sentence
    if current_segment:
        segments.append(current_segment)
    if not segments:
        for i in range(0, len(text), max_length):
            segments.append(text[i:i + max_length])
    return segments

def translate_docx(input_path: str, output_path: str, tone_style):
    """翻译 Word 文档"""
    doc = docx.Document(input_path)
    with open(output_path, 'w', encoding='utf-8') as f:
        for para in doc.paragraphs:
            if not para.text.strip():
                f.write("\n")
            else:
                translated = translate_with_punctuation(para.text, tone_style)
                f.write(translated + "\n")