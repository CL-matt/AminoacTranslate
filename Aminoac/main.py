"""
用于阿弥诺斯语的翻译器
"""

__author__ = "温茶"
__copyright__ = "Copyright (C) 2025, ranrylios"
__license__ = None
__version__ = "Alpha 1.2"
__email__ = "@gmail.com"

"""别点开
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

3. 系统交互：
   - pyperclip: 剪贴板读写操作
   - json: 历史记录数据序列化/反序列化
   - os: 文件系统路径操作

4. 多线程处理：
   - threading.Thread: 实现文件处理后台线程，防止界面冻结

5. 文件处理：
   - pdfplumber: PDF文件内容提取

6. 字符处理：
   - unicodedata: Unicode字符规范化处理

7. 时间处理：
   - datetime: 记录翻译操作时间戳
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog
from pypinyin import pinyin, Style
import pyperclip
import json
import os
from threading import Thread
import pdfplumber
import unicodedata
from datetime import datetime

# 配色方案
COLOR_SCHEME = {
    "background": "#F0F3F5",
    "primary": "#2E86C1",
    "secondary": "#5DADE2",
    "text": "#2C3E50",
    "success": "#28B463",
    "warning": "#F1C40F"
}

# 全局配置
HISTORY_DIR = "./output"
HISTORY_FILE = os.path.join(HISTORY_DIR, "translation_history.json")  # 使用路径拼接
MAX_HISTORY = 20
FILE_TYPES = [
    ('PDF 文档', '*.pdf'), 
    ('文本文档', '*.txt'),
    ('所有文件', '*.*')
]
HISTORY_COLUMNS = ("时间", "输入摘要", "输出摘要", "模式") #历史记录没写完，有时间添加

# 拼音风格管理类
class ToneStyle:
    def __init__(self, name, pypinyin_style, description=""):
        self.name = name
        self.pypinyin_style = pypinyin_style
        self.description = description

# 预定义拼音风格列表
TONE_STYLES = [
    ToneStyle("古韵", Style.TONE, "保留声调符号，如 nǐ"),
    ToneStyle("音韵", Style.TONE2, "用数字表示声调，如 ni3"),
    ToneStyle("无声调", Style.NORMAL, "移除所有声调符号，如 ni")
]

def clean_pinyin(pinyin_str, style):
    """根据模式清洗拼音"""
    if style.pypinyin_style == Style.NORMAL:
        normalized = unicodedata.normalize('NFD', pinyin_str)
        cleaned = ''.join([c for c in normalized if not unicodedata.combining(c)])
        return cleaned.lower().replace(" ", "").replace("ü", "v")
    else:
        return pinyin_str

def reverse_pinyin_translation(chinese_text, tone_style):
    """核心翻译函数"""
    try:
        # 提取拼音
        raw_pinyin = [item[0] for item in pinyin(chinese_text, style=tone_style.pypinyin_style)]
        pinyin_str = "".join(raw_pinyin)
        
        # 根据模式清洗
        processed = clean_pinyin(pinyin_str, tone_style)
        
        # 反转并格式化
        reversed_str = processed[::-1]
        formatted = reversed_str[0].upper() + reversed_str[1:] if reversed_str else ""
        return formatted
    except Exception as e:
        raise ValueError(f"转换错误: {str(e)}")

def read_pdf(file_path):
    """读取PDF文件内容,没有测试过"""
    content = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                content.extend(text.split('\n'))
    return [line.strip() for line in content if line.strip()]

def process_file_translation(tone_style):
    """文件翻译处理"""
    try:
        file_path = filedialog.askopenfilename(filetypes=FILE_TYPES)
        if not file_path: return

        progress_window = tk.Toplevel()
        progress_label = ttk.Label(progress_window, text="正在处理文件...")
        progress_label.pack(padx=20, pady=20)
        progress_window.grab_set()

        # 读取文件内容
        if file_path.endswith('.pdf'):
            content = read_pdf(file_path)
        else:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read().split('\n')

        # 翻译处理
        translated = []
        for para in content:
            if para.strip():
                translated.append(reverse_pinyin_translation(para, tone_style))

        # 保存结果
        save_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=FILE_TYPES
        )
        if save_path:
            with open(save_path, 'w', encoding='utf-8') as f:
                f.write('\n\n'.join(translated))
            messagebox.showinfo("完成", f"文件已保存至：\n{save_path}")

    except Exception as e:
        messagebox.showerror("错误", f"文件处理失败：{str(e)}")
    finally:
        if 'progress_window' in locals():
            progress_window.destroy()

def save_history(history_records):
    """保存历史记录到文件"""
    try:
        data = [{
            "timestamp": r.timestamp,
            "input": r.input,
            "output": r.output,
            "style": r.style
        } for r in history_records]
        
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)
    except Exception as e:
        print(f"保存历史记录失败: {str(e)}")

def load_history():
    """从文件加载历史记录"""
    try:
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [HistoryRecord(
                    item["input"],
                    item["output"],
                    item["style"]
                ) for item in data]
        return []
    except Exception as e:
        print(f"加载历史记录失败: {str(e)}")
        return []

class TranslationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("阿弥诺斯语翻译器 V1.2")
        self.root.geometry("900x650")
        self.style_var = tk.StringVar(value=TONE_STYLES[0].name)  # 默认风格
        self.setup_ui()
        load_history()

    def setup_ui(self):
        """初始化用户界面"""
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background=COLOR_SCHEME["background"])
        style.configure("TLabel", 
                      background=COLOR_SCHEME["background"],
                      foreground=COLOR_SCHEME["text"],
                      font=("微软雅黑", 12))
        style.configure("TButton", 
                      font=("微软雅黑", 12, "bold"),
                      background=COLOR_SCHEME["primary"],
                      foreground="white")

        main_frame = ttk.Frame(self.root)
        main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        # 输入区域
        input_label = ttk.Label(main_frame, text="请输入中文内容：")
        input_label.grid(row=0, column=0, sticky=tk.W)
        self.input_area = scrolledtext.ScrolledText(main_frame, 
                                                  wrap=tk.WORD, 
                                                  height=8,
                                                  font=("微软雅黑", 12))
        self.input_area.grid(row=1, column=0, sticky=tk.EW, pady=10)

        # 控制面板
        control_frame = ttk.Frame(main_frame)
        control_frame.grid(row=2, column=0, pady=15, sticky=tk.EW)

        # 拼音风格选择菜单
        style_menu = ttk.OptionMenu(
            control_frame,
            self.style_var,
            TONE_STYLES[0].name,
            *[style.name for style in TONE_STYLES]
        )
        style_menu.pack(side=tk.LEFT, padx=5)

        # 功能按钮
        btn_frame = ttk.Frame(control_frame)
        btn_frame.pack(side=tk.RIGHT)

        ttk.Button(btn_frame, 
                 text="立即翻译",
                 command=self.translate_text).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(btn_frame,
                 text="翻译文档",
                 command=lambda: Thread(
                     target=process_file_translation,
                     args=(self.get_current_style(),)
                 ).start()).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(btn_frame,
                 text="复制结果",
                 command=self.copy_result).pack(side=tk.LEFT, padx=5)

        # 输出区域
        output_label = ttk.Label(main_frame, text="翻译结果：")
        output_label.grid(row=3, column=0, sticky=tk.W)
        self.output_area = scrolledtext.ScrolledText(main_frame,
                                                  wrap=tk.WORD,
                                                  height=8,
                                                  font=("Consolas", 12),
                                                  state="disabled")
        self.output_area.grid(row=4, column=0, sticky=tk.EW)

        # 响应式布局
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)
        main_frame.rowconfigure(4, weight=1)

    def get_current_style(self):
        """获取当前选择的拼音风格对象"""
        current_name = self.style_var.get()
        for style in TONE_STYLES:
            if style.name == current_name:
                return style
        return TONE_STYLES[0]  # 默认返回第一个风格

    def translate_text(self):
        try:
            input_text = self.input_area.get("1.0", tk.END).strip()
            if not input_text:
                messagebox.showwarning("输入提示", "请输入需要翻译的中文内容")
                return
            
            current_style = self.get_current_style()
            translated = reverse_pinyin_translation(input_text, current_style)
            
            self.output_area.config(state='normal')
            self.output_area.delete("1.0", tk.END)
            self.output_area.insert(tk.END, translated)
            self.output_area.config(state='disabled')
            
        except Exception as e:
            messagebox.showerror("错误", f"翻译失败: {str(e)}")

    def copy_result(self):
        try:
            content = self.output_area.get("1.0", tk.END).strip()
            if content:
                pyperclip.copy(content)
                messagebox.showinfo("复制成功", "结果已复制到剪贴板")
        except Exception as e:
            messagebox.showerror("复制失败", f"无法复制内容: {str(e)}")

if __name__ == "__main__":
    # 单元测试
    test_cases = [
        ("你好", TONE_STYLES[2], "Oahin"),  # 无声调模式
        ("测试", TONE_STYLES[0], "Ìhsèc")    # 带声调模式
    ]
    for text, style, expected in test_cases:
        result = reverse_pinyin_translation(text, style)
        assert result == expected, f"测试失败：{text} -> {result} (预期: {expected})"
    print("✅ 所有测试通过")
    
    # 启动GUI
    root = tk.Tk()
    app = TranslationApp(root)
    try:
        root.mainloop()
    finally:
        save_history()