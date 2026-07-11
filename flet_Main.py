import os
import sys
import threading
import time
import wave
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
    page.title = "Aminoac Translate"
    page.window.width = 1100      
    page.window.height = 850
    page.window.resizable = True
    page.window.maximizable = True
    page.padding = 20
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.AUTO
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH

    style_map = {style.name: style for style in TONE_STYLES}
    style_names = [style.name for style in TONE_STYLES]
    history_records = load_history()

    # ==========================
    # 1. UI 控件定义区
    # ==========================
    tone_dropdown = ft.Dropdown(
        label="音调风格",
        value=style_names[0],
        options=[ft.dropdown.Option(name) for name in style_names],
        width=220,
    )
    input_field = ft.TextField(
        label="输入文本",
        multiline=True,
        min_lines=10,
        max_lines=16,
        expand=True,
        autofocus=True,
        border_radius=12,
        filled=True,
        hint_text="请输入中文或 Aminoac 内容",
    )
    output_field = ft.TextField(
        label="翻译结果",
        multiline=True,
        min_lines=10,
        max_lines=16,
        expand=True,
        read_only=True,
        border_radius=12,
        filled=True,
        hint_text="翻译结果会显示在这里",
    )
    status_text = ft.Text(value="")
    selected_file_text = ft.Text(value="未选择文件")
    
    # 历史记录视图
    history_view = ft.ListView(expand=1, spacing=8, padding=0, auto_scroll=True)
    MAX_VISIBLE_HISTORY = 6

    # ==========================
    # 2. 历史记录管理功能
    # ==========================
    def refresh_history():
        history_view.controls.clear()
        visible_history = history_records[:MAX_VISIBLE_HISTORY]
        
        if not visible_history:
            history_view.controls.append(ft.Text("暂无历史记录"))
        else:
            for record in visible_history:
                input_preview = (record.input or "").replace("\n", " ")[:24]
                output_preview = (record.output or "").replace("\n", " ")[:24]
                
                expanded = ft.Column([], spacing=4)
                expanded.controls.append(ft.Text(record.timestamp, size=11, color="#616161"))
                expanded.controls.append(ft.Text(f"输入：{record.input}", size=12, weight=ft.FontWeight.BOLD, selectable=True))
                expanded.controls.append(ft.Text(f"结果：{record.output}", size=12, selectable=True))
                expanded.controls.append(ft.Text(f"风格：{record.style}", size=11, color="#607D8B"))

                collapsed = ft.Column(
                    [
                        ft.Text(record.timestamp, size=11, color="#616161"),
                        ft.Text(input_preview, size=12, weight=ft.FontWeight.BOLD),
                        ft.Text(output_preview, size=12),
                        ft.Text(f"风格：{record.style}", size=11, color="#607D8B"),
                    ],
                    tight=True,
                    spacing=1,
                )

                card_content = ft.Column([collapsed], tight=True, spacing=0)

                def toggle_card(e, content=card_content, expanded_view=expanded, collapsed_view=collapsed):
                    if content.controls[0] is collapsed_view:
                        content.controls = [expanded_view]
                    else:
                        content.controls = [collapsed_view]
                    page.update()

                card = ft.Container(
                    ft.Column([collapsed], tight=True, spacing=0),
                    border=ft.Border.all(1, "#E0E0E0"),
                    border_radius=8,
                    padding=8, 
                    on_click=lambda e, content=card_content: toggle_card(e, content=content),
                )
                card_content = card
                history_view.controls.append(card)
        page.update()

    # ==========================
    # 3. 翻译核心逻辑
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
            status_text.value = "请输入要翻译的内容。"
            page.update()
            return
        try:
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
        page.update()

    def copy_click(e):
        if output_field.value:
            pyperclip.copy(output_field.value)
            status_text.value = "已复制到剪贴板"
            page.update()

    # ==========================
    # 4. 文件读写系统 (降维打击：原生同步弹窗)
    # ==========================
    pending_save_text = ""

    def translate_file_click(e):
        # 召唤隐藏的底层弹窗
        root = tk.Tk()
        root.withdraw() # 隐藏丑陋的主窗口
        root.attributes('-topmost', True) # 强制显示在屏幕最前面
        
        file_path = filedialog.askopenfilename(
            title="选择要翻译的文件",
            filetypes=[("支持的文档", "*.pdf;*.docx;*.txt"), ("所有文件", "*.*")]
        )
        root.destroy() # 选完立刻销毁

        if not file_path:
            return  # 用户取消了选择
        
        selected_file_text.value = f"已选择：{os.path.basename(file_path)}"
        tone_style = style_map[tone_dropdown.value or style_names[0]]
        
        try:
            status_text.value = "正在翻译文档，请稍候..."
            page.update()
            
            translated_lines = process_file(file_path, tone_style)
            
            nonlocal pending_save_text
            pending_save_text = "\n".join(translated_lines)
            output_field.value = pending_save_text
            status_text.value = "文档翻译已完成"
            
            history_records.insert(0, HistoryRecord(os.path.basename(file_path), pending_save_text[:80], tone_style))
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
            
        # 召唤隐藏的底层保存弹窗
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
            
            nonlocal pending_save_text
            pending_save_text = output_field.value
            status_text.value = f"结果已保存到：{os.path.basename(save_path)}"
        except Exception as exc:
            status_text.value = f"保存失败：{exc}"
        page.update()

    # ==========================
    # 5. 语音合成模块 (多线程)
    # ==========================
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
                    except Exception as play_error:
                        print(f"pydub play failed: {play_error}")
                        
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

    # 初始化调用一次，加载默认数据
    refresh_history()

    # ==========================
    # 6. 主页面布局拼装
    # ==========================
    page.add(
        ft.Container(
            ft.Column(
                [
                    ft.Text("Aminoac Translate", size=30, weight=ft.FontWeight.BOLD),
                    ft.Text("V2.2 ", size=13, color="#616161"),
                    
                    # 顶部操作栏
                    ft.Row(
                        [
                            tone_dropdown,
                            ft.ElevatedButton("翻译文本", icon="translate", on_click=translate_click, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8))),
                            ft.ElevatedButton("翻译文档", icon="file_open", on_click=translate_file_click, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8))),
                            ft.ElevatedButton("保存结果", icon="save", on_click=save_translated_file_click, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8))),
                            ft.ElevatedButton("复制结果", icon="copy", on_click=copy_click, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8))),
                            ft.ElevatedButton("朗读", icon="volume_up", on_click=speak_click, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8))),
                            ft.TextButton("清空", icon="clear", on_click=clear_click, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8))),
                        ],
                        spacing=10,
                        wrap=True,
                    ),
                    selected_file_text,
                    
                    # 左右双栏输入输出
                    ft.Row(
                        [
                            ft.Container(input_field, expand=True, padding=5),
                            ft.Container(output_field, expand=True, padding=5),
                        ],
                        expand=True,
                        spacing=16,
                    ),
                    status_text,
                    ft.Divider(),
                    
                    # 底部历史记录
                    ft.Text("历史记录", size=18, weight=ft.FontWeight.BOLD),
                    ft.Container(
                        history_view, 
                        height=270, 
                        border=ft.Border.all(1, "#E0E0E0"),
                        border_radius=12, 
                        padding=8
                    ),
                ],
                spacing=12,
                expand=True,
            ),
            bgcolor="#F8FAFC",
            border_radius=16,
            padding=20,
            expand=True,
        )
    )

if __name__ == "__main__":
    ft.app(target=main)