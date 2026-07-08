"""
用于阿弥诺斯语的翻译器
"""

__author__ = "温茶"
__copyright__ = "Copyright (C) 2025, ranrylios"
__license__ = None
__version__ = "Alpha 2.2"
__email__ = "@gmail.com"

"""
核心依赖模块

包含程序运行所需的所有第三方库和标准库导入

各导入模块功能说明：
1. GUI开发相关：
   - tkinter: Python标准GUI库，用于创建窗口应用程序
   - ttk: 提供主题化控件（增强版UI组件）
   - messagebox: 显示消息对话框
   - scrolledtext: 带滚动条的文本区域
   - filedialog: 文件选择对话框

2. 核心功能库：
   - pypinyin: 汉字转拼音核心库
     - pinyin: 汉字转拼音函数
     - Style: 拼音风格枚举（声调/数字/无调）
   - pyttsx3: 语音核心库
     - pydub: 音频处理库
     - playsound: 播放音频文件
     - AudioSegment: 音频段处理类

3. 系统交互：
   - pyperclip: 剪贴板读写操作
   - json: 历史记录数据序列化/反序列化
   - os: 文件系统路径操作

4. 多线程处理：
   - threading.Thread: 实现文件处理后台线程，防止界面冻结

5. 文件处理：
   - pdfplumber: PDF文件内容提取
   - docx: Word文件内容提取

6. 字符处理：
   - unicodedata: Unicode字符规范化处理

7. 时间处理：
   - datetime: 记录翻译操作时间戳
"""
import os
import sys
base_dir = os.path.dirname(os.path.abspath(__file__))
libs_path = os.path.join(base_dir, "libs")
sys.path.insert(0, libs_path)
# Ensure project root is importable (so `core` and `gui` packages resolve)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog
from pypinyin import pinyin, Style
import pyperclip #安装出了问题，导致无法复制，有时间再修
import json
import jieba
from threading import Thread
from pydub import AudioSegment
from core.translate import (
    TONE_STYLES,
    detect_and_translate,
    reverse_pinyin_translation,
    split_long_text,
    read_pdf,
    read_word,
    CUSTOM_TRANSLATION_DICT,
    translate_docx,
    translate_with_punctuation,
)
from core.history import HistoryRecord, save_history, load_history
from core.file_io import process_file

# 配色方案
COLOR_SCHEME = {
    "background": "#F0F3F5",
    "primary": "#2E86C1",
    "secondary": "#5DADE2",
    "text": "#2C3E50",
    "success": "#28B463",
    "warning": "#F1C40F"
}

# 项目路径与历史/临时音频文件位置（统一使用项目根目录下的 output）
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HISTORY_DIR = os.path.join(PROJECT_ROOT, "output")
os.makedirs(HISTORY_DIR, exist_ok=True)
HISTORY_FILE = os.path.join(HISTORY_DIR, "translation_history.json")
TEMP_AUDIO = os.path.join(HISTORY_DIR, "temp_audio.wav")
# 其它全局配置
MAX_HISTORY = 20
FILE_TYPES = [
    ('PDF 文档', '*.pdf'),
    ('Word 文档', '*.docx'),
    ('文本文档', '*.txt'),
    ('所有文件', '*.*')
]
HISTORY_COLUMNS = ("时间", "输入摘要", "输出摘要", "模式")
import pdfplumber
import docx
from docx import Document
import unicodedata
from datetime import datetime
import pyttsx3
from pydub import AudioSegment
from pydub.playback import play
import io
import threading
import time
import wave
import re

# translation functions are implemented in core.translate and imported above

# ---------- 与 docx 结合的示例流程 -------------
# translation helpers are provided by core.translate

def process_file_translation(tone_style):
    """文件翻译处理"""
    try:
        file_path = filedialog.askopenfilename(filetypes=FILE_TYPES)
        if not file_path:
            return

        progress_window = tk.Toplevel()
        progress_label = ttk.Label(progress_window, text="正在处理文件...")
        progress_label.pack(padx=20, pady=20)
        progress_window.grab_set()

        # 读取并翻译文件内容 (核心逻辑委托给 core.file_io.process_file)
        translated = process_file(file_path, tone_style)

        # 保存结果
        save_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[('文本文档', '*.txt')]
        )
        if not save_path:  # 用户取消保存操作
            return

        with open(save_path, 'w', encoding='utf-8') as f:
            f.write('\n\n'.join(translated))
        messagebox.showinfo("完成", f"文件已保存至：\n{save_path}")

    except Exception as e:
        messagebox.showerror("错误", f"文件处理失败：{str(e)}")
    finally:
        if 'progress_window' in locals():
            progress_window.destroy()

# history persistence is provided by core.history

# Ensure project root is on sys.path so top-level `gui` package is importable
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from gui.main_window import start_gui


if __name__ == "__main__":
    print("Python executable:", sys.executable)
    services = {
        'TONE_STYLES': TONE_STYLES,
        'COLOR_SCHEME': COLOR_SCHEME,
        'detect_and_translate': detect_and_translate,
        'process_file_translation': process_file_translation,
        'load_history': load_history,
        'save_history': save_history,
        'HistoryRecord': HistoryRecord,
        'MAX_HISTORY': MAX_HISTORY,
        'pyperclip': pyperclip,
        'TEMP_AUDIO': TEMP_AUDIO,
        'HISTORY_DIR': HISTORY_DIR,
        'HISTORY_COLUMNS': HISTORY_COLUMNS,
        'pyttsx3': pyttsx3
    }
    start_gui(services)