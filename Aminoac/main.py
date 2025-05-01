"""
用于阿弥诺斯语的翻译器
"""

__author__ = "温茶"
__copyright__ = "Copyright (C) 2025, ranrylios"
__license__ = None
__version__ = "Alpha 1.2"
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
HISTORY_DIR = "output"  # 将缓存文件存储在 output 文件夹下

# 自动创建导出历史记录文件夹
if not os.path.exists(HISTORY_DIR):
    os.makedirs(HISTORY_DIR)

HISTORY_FILE = os.path.join(HISTORY_DIR, "translation_history.json")  # 历史记录文件路径
TEMP_AUDIO = os.path.join(HISTORY_DIR, "temp_audio.wav")  # 临时音频文件路径
# print(HISTORY_FILE) 测试
MAX_HISTORY = 20
FILE_TYPES = [
    ('PDF 文档', '*.pdf'),
    ('Word 文档', '*.docx'),
    ('文本文档', '*.txt'),
    ('所有文件', '*.*')
]
HISTORY_COLUMNS = ("时间", "输入摘要", "输出摘要", "模式") # 已完善

# 拼音风格管理类
class ToneStyle:
    def __init__(self, name, pypinyin_style, description=""):
        self.name = name
        self.pypinyin_style = pypinyin_style
        self.description = description

# 历史记录
class HistoryRecord:
    def __init__(self, input: str, output: str, style: ToneStyle):
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.input = input[:30]
        self.output = output[:30]
        self.style = style.name

# 预定义拼音风格列表
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

def reverse_pinyin_translation(chinese_text, tone_style):
    # 如果在自定义字典里，直接返回
    if chinese_text in CUSTOM_TRANSLATION_DICT:
        return CUSTOM_TRANSLATION_DICT[chinese_text]

    # 精确模式断句，避免重叠片段
    words = jieba.cut(chinese_text, cut_all=False)

    # 先按词得到拼音串
    pinyin_parts = []
    for word in words:
        if word in CUSTOM_TRANSLATION_DICT:
            pinyin_parts.append(CUSTOM_TRANSLATION_DICT[word])
        else:
            chars_pinyin = pinyin(word, style=tone_style.pypinyin_style)
            combined = ''.join([syllable[0] for syllable in chars_pinyin])
            pinyin_parts.append(combined)
    pinyin_str = ' '.join(pinyin_parts)

    # 清洗拼音（去声调符号或保留数字声调）
    processed = clean_pinyin(pinyin_str, tone_style)

    # 先整体反转词序，再对每个词内部字符倒放
    rev_parts = [seg[::-1] for seg in processed.split()[::-1]]
    out = ' '.join(rev_parts)            # e.g. "eijihs oahin"

    # 整体首字母大写
    return out[0].upper() + out[1:] if out else ""
    
def wtranslate_with_punctuation(text: str, tone_style) -> str:
    _PUNCT_RE = re.compile(r'([，。！？；："＂＇＇＇""''‘’"“”()（）【】\{\}\[\]〈〉《》﹏…—,.!?;:\-\s])')
    """
    分阶段处理：
    1. 中文→拼音（保持词序）
    2. 反转每个词的拼音字母
    3. 反转句子顺序+首字母大写
    """
    # 阶段一：中文→拼音（保持词序）
    def to_pinyin(s: str) -> str:
        words = list(jieba.cut(s))
        pinyin_words = []
        for word in words:
            if _PUNCT_RE.fullmatch(word):  # 标点符号原样保留
                pinyin_words.append(word)
            else:
                pys = pinyin(word, style=tone_style.pypinyin_style)
                pinyin_words.append(''.join([p[0] for p in pys]))
        return ' '.join(pinyin_words)  # 保留空格

    # 阶段二：反转拼音字母
    def reverse_pinyin(s: str) -> str:
        segments = _PUNCT_RE.split(s)
        result = []
        for seg in segments:
            if not seg:
                continue
            if _PUNCT_RE.fullmatch(seg):  # 标点符号原样保留
                result.append(seg)
            else:
                result.append(seg[::-1])  # 反转字母
        return ''.join(result)

    # 阶段三：反转句子顺序+首字母大写
    sentences = re.split(r'([，。！？；,.!?])', text)  # 按标点符号分割
    processed = []
    current = []
    
    for seg in sentences:
        if not seg.strip():
            continue
        if re.fullmatch(r'[，。！？；,.!?]', seg):  # 标点符号
            if current:
                content = ''.join(current)
                # 阶段一和阶段二处理
                pinyin_content = to_pinyin(content)
                reversed_content = reverse_pinyin(pinyin_content)
                processed.append((reversed_content, seg))
                current = []
        else:
            current.append(seg)
    
    if current:
        content = ''.join(current)
        pinyin_content = to_pinyin(content)
        reversed_content = reverse_pinyin(pinyin_content)
        processed.append((reversed_content, ''))

    # 反转句子顺序
    reversed_sentences = processed[::-1]
    
    # 首字母大写
    if reversed_sentences:
        first_content, first_punct = reversed_sentences[0]
        if first_content:
            for i, c in enumerate(first_content):
                if c.isalpha():
                    first_content = first_content[:i] + c.upper() + first_content[i+1:]
                    break
        reversed_sentences[0] = (first_content, first_punct)
    
    return ''.join([content + punct for content, punct in reversed_sentences])

def translate_with_punctuation(text: str, tone_style) -> str:
    """
    严格按照要求的新实现：
    1. 先提取句子框架（保留原标点）
    2. 每句内部分词并反转拼音
    3. 反转句子顺序
    4. 添加空格并首字母大写
    """
    # 第一步：提取句子框架（句子和标点符号分离）
    sentences = []
    delimiters = []
    
    # 用正则匹配中文标点分割
    pattern = re.compile(r'([，。！？；,.!?])')
    parts = pattern.split(text)
    
    current_sent = []
    for part in parts:
        if not part.strip():
            continue
        if pattern.fullmatch(part):  # 是标点符号
            if current_sent:
                sentences.append(''.join(current_sent))
                current_sent = []
            delimiters.append(part)
        else:  # 是句子内容
            current_sent.append(part)
    
    if current_sent:
        sentences.append(''.join(current_sent))
    
    # 第二步：处理每个句子（分词→拼音→反转）
    reversed_sents = []
    for sent in sentences:
        words = list(jieba.cut(sent))
        reversed_words = []
        for word in words:
            # 中文转拼音
            pys = pinyin(word, style=tone_style.pypinyin_style)
            py_str = ''.join([p[0] for p in pys])
            # 清洗拼音
            cleaned = clean_pinyin(py_str, tone_style)
            # 反转拼音
            reversed_word = cleaned[::-1]
            reversed_words.append(reversed_word)
        reversed_sents.append(' '.join(reversed_words))  # 词间加空格
    
    # 第三步：反转句子顺序并组合
    reversed_sents = reversed_sents[::-1]
    final_parts = []
    for i, sent in enumerate(reversed_sents):
        final_parts.append(sent)
        if i < len(delimiters):
            final_parts.append(delimiters[len(delimiters) - i - 1])  # 反转标点符号顺序
    
    # 第四步：首字母大写
    result = ''.join(final_parts).strip()
    if result:
        for i, c in enumerate(result):
            if c.isalpha():
                result = result[:i] + c.upper() + result[i+1:]
                break
    
    return result

# ---------- 与 docx 结合的示例流程 -------------
def translate_docx(input_path: str, output_path: str, tone_style):
    doc = Document(input_path)
    with open(output_path, 'w', encoding='utf-8') as f:
        for para in doc.paragraphs:
            if not para.text.strip():
                f.write("\n")  # 保留空行
            else:
                translated = translate_with_punctuation(para.text, tone_style)
                f.write(translated + "\n")  # 确保换行

def read_pdf(file_path):
    """读取 PDF 文件内容"""
    content = []
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    content.extend(text.split('\n'))
        return [line.strip() for line in content if line.strip()]
    except Exception as e:
        raise ValueError(f"无法读取 PDF 文件: {str(e)}")

def read_word(file_path):
    """读取 Word 文件内容"""
    content = []
    try:
        doc = docx.Document(file_path)
        for paragraph in doc.paragraphs:
            if paragraph.text.strip():
                content.append(paragraph.text.strip())
        return content
    except Exception as e:
        raise ValueError(f"无法读取 Word 文件: {str(e)}")

def load_custom_dict(file_path="custom_dict.json"):
    """加载自定义翻译字典并更新 jieba 词典"""
    try:
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                custom_dict = json.load(f)
                # 将自定义词条添加到 jieba 词典
                for word in custom_dict.keys():
                    jieba.add_word(word)
                return custom_dict
        else:
            return {}
    except Exception as e:
        print(f"加载自定义字典失败: {str(e)}")
        return {}

CUSTOM_TRANSLATION_DICT = load_custom_dict()

def split_long_text(text, max_length=50):
    """将长文本按标点符号或固定长度分段"""
    import re
    sentences = re.split(r'(。|！|\!|\.|？|\?)', text)  # 按标点符号分割
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

    # 如果没有标点符号，按固定长度分段
    if not segments:
        for i in range(0, len(text), max_length):
            segments.append(text[i:i + max_length])

    return segments

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

        # 读取文件内容
        content = []
        if file_path.endswith('.pdf'):
            content = read_pdf(file_path)
        elif file_path.endswith('.docx'):
            content = read_word(file_path)
        else:
            import chardet
            with open(file_path, 'rb') as f:
                raw_data = f.read()
                detected = chardet.detect(raw_data)
                encoding = detected['encoding'] if detected['encoding'] else 'utf-8'
            with open(file_path, 'r', encoding=encoding) as f:
                content = f.read().split('\n')

        # 翻译处理
        translated = []
        for para in content:
            if para.strip():
                # 分段处理长句子
                segments = split_long_text(para)
                for segment in segments:
                    translated.append(reverse_pinyin_translation(segment, tone_style))

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
        self.history_records = load_history()
        self.audio_lock = threading.Lock()  # 音频操作锁
        self.engine = self.init_tts_engine()

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
        
        ttk.Button(btn_frame,
                 text="查看历史",
                 command=self.show_history).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame,
             text="朗读",
             command=self.speak_aminoac).pack(side=tk.LEFT, padx=5)

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
            translated = translate_with_punctuation(input_text, current_style)
            
            self.output_area.config(state='normal')
            self.output_area.delete("1.0", tk.END)
            self.output_area.insert(tk.END, translated)
            self.output_area.config(state='disabled')
            self.history_records.insert(0, HistoryRecord(input_text, translated, current_style))
            if len(self.history_records) > MAX_HISTORY:
                self.history_records = self.history_records[:MAX_HISTORY]
            save_history(self.history_records)

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

    def show_history(self):
        history_win = tk.Toplevel(self.root)
        history_win.title("历史记录")
        history_win.geometry("600x300")
    
        tree = ttk.Treeview(history_win, columns=HISTORY_COLUMNS, show="headings")
        for col in HISTORY_COLUMNS:
            tree.heading(col, text=col)
            tree.column(col, anchor="w", width=150)
        tree.pack(fill=tk.BOTH, expand=True)

        for record in self.history_records:
            tree.insert("", tk.END, values=(record.timestamp, record.input, record.output, record.style))

        def on_double_click(event):
            selected = tree.focus()
            if selected:
                values = tree.item(selected, "values")
                if values:
                    pyperclip.copy(values[2])
                    messagebox.showinfo("已复制", "输出已复制到剪贴板")

        tree.bind("<Double-1>", on_double_click)

    def init_tts_engine(self):
        """初始化支持中文的TTS引擎"""
        try:
            engine = pyttsx3.init()
            # 寻找中文语音包（Windows系统）
            for voice in engine.getProperty('voices'):
                if 'Chinese' in voice.name:
                    engine.setProperty('voice', voice.id)
                    engine.setProperty('rate', 160)  # 优化语速
                    return engine
            messagebox.showwarning("警告", "未找到中文语音引擎")
            return None
        except Exception as e:
            messagebox.showerror("错误", f"语音引擎初始化失败：{str(e)}")
            return None

    def speak_aminoac(self):
        """朗读倒放的阿米诺斯语"""
        if not self.engine:
            return

        # 获取原始中文文本
        input_text = self.input_area.get("1.0", tk.END).strip()
        if not input_text:
            messagebox.showinfo("提示", "没有可朗读的内容")
            return

        def _speak_thread():
            try:
                with self.audio_lock:
                    # 生成原始中文语音
                    print("生成语音文件...")
                    self.engine.save_to_file(input_text, TEMP_AUDIO)
                    self.engine.runAndWait()
                    time.sleep(0.1)  # 确保文件句柄释放

                    # 确保文件生成完成后再加载
                    if not os.path.exists(TEMP_AUDIO):
                        raise FileNotFoundError("音频文件未生成")
                    if not os.access(TEMP_AUDIO, os.R_OK):
                        raise PermissionError(f"无法读取文件：{TEMP_AUDIO}")

                    print(f"TEMP_AUDIO 路径: {TEMP_AUDIO}")
                    print(f"文件是否存在: {os.path.exists(TEMP_AUDIO)}")
                    print(f"文件是否可读: {os.access(TEMP_AUDIO, os.R_OK)}")
                    print(f"文件是否可写: {os.access(TEMP_AUDIO, os.W_OK)}")

                    # 加载并倒放音频
                    audio = AudioSegment.from_wav(TEMP_AUDIO)
                    reversed_audio = audio.reverse()
                    print("倒放音频...")

                    # 保存倒放后的音频
                    reversed_audio_path = os.path.join(HISTORY_DIR, "reversed_audio.wav")
                    reversed_audio.export(reversed_audio_path, format="wav", codec="pcm_s16le")
                    print(f"倒放音频已保存到: {reversed_audio_path}")

                    # 播放倒放音频
                    print("准备播放倒放音频...")
                    from playsound import playsound
                    playsound(reversed_audio_path)
                    print("播放完成")

            except Exception as e:
                messagebox.showerror("错误", f"朗读失败：{str(e)}")
            #finally:
                # 如果不需要删除临时文件，可以注释掉以下代码
                # if os.path.exists(TEMP_AUDIO):
                #     try:
                #         os.remove(TEMP_AUDIO)
                #     except Exception as e:
                #         print(f"无法删除临时文件: {str(e)}")

        threading.Thread(target=_speak_thread, daemon=True).start()

if __name__ == "__main__":
    # 单元测试
    test_cases = [
        ("你好", TONE_STYLES[2], "Oahin"),                      # 无声调模式
        ("测试", TONE_STYLES[0], "Ìhsèc"),                      # 带声调模式
        ("你好,世界.", TONE_STYLES[2], "Eijihs,oahin."),        # 分词后带空格
        ("空 格 处 理", TONE_STYLES[0], "Ǐl ùhc ég gnōk"),      # 空格处理
        ("我爱编程", TONE_STYLES[0], "Gnéhcnāib ià ǒw")         # 保留声调
    ]
    for text, style, expected in test_cases:
        result = translate_with_punctuation(text, style)
        assert result == expected, f"测试失败：{text} -> {result} (预期: {expected})"
    print("✅ 所有测试通过")
    
    # 启动GUI
    root = tk.Tk()
    app = TranslationApp(root)
    try:
        root.mainloop()
    finally:
        save_history(app.history_records)