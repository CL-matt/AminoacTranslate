import os
import sys
import threading
import time
import tkinter as tk
from tkinter import filedialog

# 确保能找到项目根目录和核心模块
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
    # ==========================
    # 窗口与谷歌极简主题设置
    # ==========================
    page.title = "Aminoac Translate"
    page.window.width = 1200      
    page.window.height = 850
    page.window.resizable = True
    page.padding = 40
    page.bgcolor = "#F1F3F4" # 谷歌经典的浅灰背景
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    style_map = {style.name: style for style in TONE_STYLES}
    style_names = [style.name for style in TONE_STYLES]
    history_records = load_history()

    # ==========================
    # 1. 无边框输入/输出区域定义
    # ==========================
    input_field = ft.TextField(
        multiline=True,
        min_lines=12,
        max_lines=18,
        expand=True,
        autofocus=True,
        border=ft.InputBorder.NONE, # 隐藏默认边框
        filled=False,               # 隐藏默认灰色填充
        hint_text="输入文字或选择文档",
        text_size=20,               # 谷歌翻译标志性的大字体
    )
    
    output_field = ft.TextField(
        multiline=True,
        min_lines=12,
        max_lines=18,
        expand=True,
        read_only=True,
        border=ft.InputBorder.NONE,
        filled=False,
        hint_text="翻译结果",
        text_size=20,
        color="#1A73E8", # 谷歌蓝字体（译文颜色）
    )

    # 顶部语言选择下拉框（仿谷歌语言栏）
    tone_dropdown = ft.Dropdown(
        value=style_names[0],
        options=[ft.dropdown.Option(name) for name in style_names],
        width=150,
        border=ft.InputBorder.NONE,
        text_size=16,
        color="#1A73E8",
        text_style=ft.TextStyle(weight=ft.FontWeight.W_500),
    )

    status_text = ft.Text(value="", size=13, color="#5F6368")
    selected_file_text = ft.Text(value="", size=13, color="#1A73E8")

    # ==========================
    # 2. 翻译与辅助功能逻辑
    # ==========================
    def apply_translation(source_text: str):
        tone_style = style_map[tone_dropdown.value or style_names[0]]
        translated = detect_and_translate(source_text, tone_style)
        output_field.value = translated
        
        history_records.insert(0, HistoryRecord(source_text, translated, tone_style))
        if len(history_records) > 20:
            history_records[:] = history_records[:20]
            
        save_history(history_records)
        refresh_history()
        return translated

    def translate_click(e):
        source_text = (input_field.value or "").strip()
        if not source_text:
            status_text.value = "请输入要翻译的内容"
            page.update()
            return
        try:
            status_text.value = "正在翻译..."
            page.update()
            apply_translation(source_text)
            status_text.value = "翻译完成"
        except Exception as exc: 
            output_field.value = ""
            status_text.value = f"翻译失败：{exc}"
        page.update()

    def clear_click(e):
        input_field.value = ""
        output_field.value = ""
        status_text.value = ""
        selected_file_text.value = ""
        page.update()

    def copy_click(e):
        if output_field.value:
            pyperclip.copy(output_field.value)
            status_text.value = "已复制到剪贴板"
            page.update()

    def translate_file_click(e):
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        
        file_path = filedialog.askopenfilename(
            title="选择要翻译的文件",
            filetypes=[("支持的文档", "*.pdf;*.docx;*.txt"), ("所有文件", "*.*")]
        )
        root.destroy()

        if not file_path:
            return
        
        selected_file_text.value = f"📄 {os.path.basename(file_path)}"
        tone_style = style_map[tone_dropdown.value or style_names[0]]
        
        try:
            status_text.value = "正在翻译文档，请稍候..."
            page.update()
            translated_lines = process_file(file_path, tone_style)
            output_field.value = "\n".join(translated_lines)
            status_text.value = "文档翻译已完成"
            
            history_records.insert(0, HistoryRecord(os.path.basename(file_path), output_field.value[:80], tone_style))
            if len(history_records) > 20:
                history_records[:] = history_records[:20]
            save_history(history_records)
            refresh_history()
            
        except Exception as exc:
            status_text.value = f"文档翻译失败：{exc}"
        page.update()

    def save_translated_file_click(e):
        if not output_field.value:
            status_text.value = "没有可保存的内容"
            page.update()
            return
            
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        
        save_path = filedialog.asksaveasfilename(
            title="保存翻译结果",
            initialfile="translated.txt",
            defaultextension=".txt",
            filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")]
        )
        root.destroy()
        
        if not save_path:
            return
            
        try:
            with open(save_path, "w", encoding="utf-8") as handle:
                handle.write(output_field.value)
            status_text.value = f"结果已保存到：{os.path.basename(save_path)}"
        except Exception as exc:
            status_text.value = f"保存失败：{exc}"
        page.update()

    def speak_click(e):
        if not (output_field.value or input_field.value):
            status_text.value = "没有可朗读的内容"
            page.update()
            return
        text_to_speak = output_field.value or input_field.value

        def _speak_thread():
            try:
                engine = pyttsx3.init()
                for voice in engine.getProperty("voices"):
                    if "Chinese" in voice.name:
                        engine.setProperty("voice", voice.id)
                        break
                engine.setProperty("rate", 160)
                temp_audio = os.path.join(PROJECT_ROOT, "output", "temp_audio.wav")
                os.makedirs(os.path.dirname(temp_audio), exist_ok=True)
                
                engine.save_to_file(text_to_speak, temp_audio)
                engine.runAndWait()
                time.sleep(0.1)
                
                if os.path.exists(temp_audio):
                    audio = AudioSegment.from_wav(temp_audio)
                    reversed_audio = audio.reverse()
                    played = False
                    try:
                        play(reversed_audio)
                        played = True
                    except Exception:
                        pass
                    if not played:
                        try:
                            import winsound
                            winsound.PlaySound(os.path.abspath(temp_audio), winsound.SND_FILENAME)
                        except Exception:
                            pass
                    try:
                        os.remove(temp_audio)
                    except Exception:
                        pass
                page.run_thread(lambda: setattr(status_text, "value", "朗读完成"))
                page.run_thread(page.update)
            except Exception as exc:
                page.run_thread(lambda: setattr(status_text, "value", f"朗读失败：{exc}"))
                page.run_thread(page.update)

        status_text.value = "正在朗读..."
        page.update()
        threading.Thread(target=_speak_thread, daemon=True).start()

    # ==========================
    # 3. 历史记录面板 (极简样式)
    # ==========================
    history_view = ft.ListView(expand=1, spacing=8, padding=0, auto_scroll=True)
    MAX_VISIBLE_HISTORY = 6

    def refresh_history():
        history_view.controls.clear()
        visible_history = history_records[:MAX_VISIBLE_HISTORY]
        
        if not visible_history:
            history_view.controls.append(ft.Text("暂无翻译历史", color="#5F6368", text_align=ft.TextAlign.CENTER))
        else:
            for record in visible_history:
                input_preview = (record.input or "").replace("\n", " ")[:30] + "..."
                output_preview = (record.output or "").replace("\n", " ")[:30] + "..."
                
                card = ft.Container(
                    content=ft.Column(
                        [
                            ft.Row([
                                ft.Text(record.timestamp, size=11, color="#9AA0A6"),
                                ft.Text(f"· {record.style}", size=11, color="#1A73E8"),
                            ]),
                            ft.Text(input_preview, size=14, color="#3C4043"),
                            ft.Text(output_preview, size=14, color="#5F6368"),
                        ],
                        spacing=4,
                    ),
                    padding=16,
                    border=ft.Border.all(1, "#DADCE0"),
                    border_radius=8,
                    bgcolor="#FFFFFF",
                )
                history_view.controls.append(card)
        page.update()
    
    refresh_history()

    # ==========================
    # 4. 谷歌翻译布局拼装 (左右分栏白底卡片)
    # ==========================
    
    # 左侧：源语言区
    source_container = ft.Container(
        expand=True,
        padding=16,
        content=ft.Column(
            [
                # 顶部栏：检测到的语言
                ft.Row([
                    ft.Text("中文 / Aminoac", size=16, weight=ft.FontWeight.W_500, color="#1A73E8"),
                    selected_file_text,
                ]),
                ft.Divider(height=1, color="#E8EAED"),
                # 主输入区
                ft.Container(input_field, expand=True),
                # 底部工具栏
                ft.Row(
                    [
                        ft.IconButton(icon="file_upload", icon_color="#5F6368", tooltip="翻译文档", on_click=translate_file_click),
                        ft.IconButton(icon="clear", icon_color="#5F6368", tooltip="清空", on_click=clear_click),
                        ft.Container(expand=True), # 弹簧占位符
                        ft.Text(value="5000 / 5000", size=12, color="#9AA0A6"), # 模拟字符计数器
                        ft.ElevatedButton(
                            "翻译", 
                            bgcolor="#1A73E8", 
                            color="#FFFFFF", 
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=4)),
                            on_click=translate_click,
                            height=40,
                            width=100
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                )
            ],
            spacing=8
        )
    )

    # 右侧：目标语言区
    target_container = ft.Container(
        expand=True,
        padding=16,
        content=ft.Column(
            [
                # 顶部栏：目标风格选择
                ft.Row([tone_dropdown]),
                ft.Divider(height=1, color="#E8EAED"),
                # 主输出区
                ft.Container(output_field, expand=True),
                # 底部工具栏
                ft.Row(
                    [
                        ft.IconButton(icon="copy", icon_color="#5F6368", tooltip="复制", on_click=copy_click),
                        ft.IconButton(icon="volume_up", icon_color="#5F6368", tooltip="朗读译文", on_click=speak_click),
                        ft.IconButton(icon="save_alt", icon_color="#5F6368", tooltip="保存结果", on_click=save_translated_file_click),
                        ft.Container(expand=True),
                        status_text,
                    ],
                    alignment=ft.MainAxisAlignment.START,
                )
            ],
            spacing=8
        )
    )

    # 中间的整体卡片（带边框和阴影，白底）
    translation_card = ft.Container(
        content=ft.Row(
            [
                source_container,
                ft.VerticalDivider(width=1, color="#DADCE0"), # 左右分割线
                target_container,
            ],
            spacing=0,
            expand=True,
        ),
        bgcolor="#FFFFFF",
        border_radius=12,
        border=ft.Border.all(1, "#DADCE0"),
        height=400, # 限制输入框区域高度
    )

    # 整个页面组合
    page.add(
        ft.Column(
            [
                # App Header
                ft.Row(
                    [
                        ft.Icon("translate", color="#5F6368", size=30),
                        ft.Text("Aminoac 翻译", size=24, color="#5F6368", weight=ft.FontWeight.NORMAL),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Container(height=10), # 间距
                
                # 核心翻译区域
                translation_card,
                
                ft.Container(height=20),
                
                # 历史记录区域
                ft.Text("历史记录", size=16, color="#3C4043", weight=ft.FontWeight.W_500),
                ft.Container(
                    content=history_view,
                    height=250, # 历史记录区高度
                ),
            ],
            width=1000, # 控制最大宽度，使界面居中更美观
            expand=True,
        )
    )

if __name__ == "__main__":
    ft.app(target=main)