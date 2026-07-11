import os
import sys
import threading
import time
import tkinter as tk
from tkinter import filedialog

# 确保路径正确
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import flet as ft
import pyperclip
import pyttsx3
from pydub import AudioSegment
from pydub.playback import play

from core.file_io import process_file
from core.history import HistoryRecord, load_history, save_history
from core.translate import TONE_STYLES, detect_and_translate

def main(page: ft.Page):
    # 窗口设置
    page.title = "Aminoac Translate V2.3"
    page.window.width = 1100      
    page.window.height = 800
    page.bgcolor = "#F1F3F4"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 30
    
    # 基础逻辑
    style_map = {style.name: style for style in TONE_STYLES}
    style_names = [style.name for style in TONE_STYLES]
    history_records = load_history()

    # --- 功能函数定义 ---
    def translate_click(e):
        if not input_field.value: return
        output_field.value = detect_and_translate(input_field.value, style_map[tone_dropdown.value])
        page.update()

    def translate_file_click(e):
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        file_path = filedialog.askopenfilename()
        root.destroy()
        if file_path:
            translated_lines = process_file(file_path, style_map[tone_dropdown.value])
            output_field.value = "\n".join(translated_lines)
            page.update()

    def speak_click(e):
        text = output_field.value or input_field.value
        if not text: return
        # 这里直接调用你原本的线程逻辑
        threading.Thread(target=lambda: pyttsx3.speak(text), daemon=True).start()

    # --- UI 控件定义 ---
    input_field = ft.TextField(multiline=True, min_lines=12, max_lines=12, expand=True, border=ft.InputBorder.NONE, hint_text="输入文字...", text_size=18)
    output_field = ft.TextField(multiline=True, min_lines=12, max_lines=12, expand=True, read_only=True, border=ft.InputBorder.NONE, hint_text="翻译结果", text_size=18, color="#1A73E8")
    
    tone_dropdown = ft.Dropdown(
        value=style_names[0],
        options=[ft.dropdown.Option(name) for name in style_names],
        width=150,
        border=ft.InputBorder.NONE,
        text_size=16,
        color="#1A73E8",
    )

    history_view = ft.ListView(expand=True, spacing=10)

    # --- 布局构建 (函数定义后才能引用函数) ---
    main_layout = ft.Container(
        content=ft.Column([
            ft.Row([ft.Text("Aminoac Translate", size=24, color="#5F6368")], alignment=ft.MainAxisAlignment.START),
            ft.Container(
                content=ft.Row([
                    ft.Container(input_field, expand=True, padding=10),
                    ft.VerticalDivider(width=1, color="#DADCE0"),
                    ft.Container(output_field, expand=True, padding=10),
                ], alignment=ft.MainAxisAlignment.START),
                bgcolor="#FFFFFF",
                border=ft.Border.all(1, "#DADCE0"),
                border_radius=10,
                height=350,
            ),
            ft.Row([
                tone_dropdown, 
                ft.ElevatedButton("翻译", on_click=translate_click, bgcolor="#1A73E8", color="#FFFFFF"),
                ft.OutlinedButton("文档", icon="file_upload", on_click=translate_file_click),
                ft.OutlinedButton("朗读", icon="volume_up", on_click=speak_click),
            ]),
            ft.Text("历史记录", size=16),
            ft.Container(content=history_view, height=200),
        ], expand=True),
        expand=True
    )

    page.add(main_layout)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)