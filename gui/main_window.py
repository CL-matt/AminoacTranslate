import os
import time
import threading
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog
from pydub import AudioSegment
from pydub.playback import play


class TranslationApp:
    def __init__(self, root, services: dict):
        self.services = services
        self.root = root
        self.root.title("阿弥诺斯语翻译器 V2.2")
        self.root.geometry("900x650")
        self.style_var = tk.StringVar(value=self.services['TONE_STYLES'][0].name)
        self.setup_ui()
        self.history_records = self.services['load_history']()
        self.audio_lock = threading.Lock()
        self.engine = self.init_tts_engine()

    def setup_ui(self):
        style = ttk.Style()
        style.theme_use("clam")
        cs = self.services['COLOR_SCHEME']
        style.configure("TFrame", background=cs["background"])
        style.configure("TLabel",
                      background=cs["background"],
                      foreground=cs["text"],
                      font=("微软雅黑", 12))
        style.configure("TButton",
                      font=("微软雅黑", 12, "bold"),
                      background=cs["primary"],
                      foreground="white")

        main_frame = ttk.Frame(self.root)
        main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        input_label = ttk.Label(main_frame, text="请输入中文内容：")
        input_label.grid(row=0, column=0, sticky=tk.W)
        self.input_area = scrolledtext.ScrolledText(main_frame,
                                                   wrap=tk.WORD,
                                                   height=8,
                                                   font=("微软雅黑", 12))
        self.input_area.grid(row=1, column=0, sticky=tk.EW, pady=10)

        control_frame = ttk.Frame(main_frame)
        control_frame.grid(row=2, column=0, pady=15, sticky=tk.EW)

        style_menu = ttk.OptionMenu(
            control_frame,
            self.style_var,
            self.services['TONE_STYLES'][0].name,
            *[s.name for s in self.services['TONE_STYLES']]
        )
        style_menu.pack(side=tk.LEFT, padx=5)

        btn_frame = ttk.Frame(control_frame)
        btn_frame.pack(side=tk.RIGHT)

        ttk.Button(btn_frame,
                   text="立即翻译",
                   command=self.translate_text).pack(side=tk.LEFT, padx=5)

        ttk.Button(btn_frame,
                   text="翻译文档",
                   command=lambda: threading.Thread(
                       target=self.services['process_file_translation'],
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

        output_label = ttk.Label(main_frame, text="翻译结果：")
        output_label.grid(row=3, column=0, sticky=tk.W)
        self.output_area = scrolledtext.ScrolledText(main_frame,
                                                    wrap=tk.WORD,
                                                    height=8,
                                                    font=("Consolas", 12),
                                                    state="disabled")
        self.output_area.grid(row=4, column=0, sticky=tk.EW)

        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)
        main_frame.rowconfigure(4, weight=1)

    def get_current_style(self):
        current_name = self.style_var.get()
        for style in self.services['TONE_STYLES']:
            if style.name == current_name:
                return style
        return self.services['TONE_STYLES'][0]

    def translate_text(self):
        try:
            input_text = self.input_area.get("1.0", tk.END).strip()
            if not input_text:
                messagebox.showwarning("输入提示", "请输入需要翻译的中文内容")
                return
            current_style = self.get_current_style()
            translated = self.services['detect_and_translate'](input_text, current_style)

            self.output_area.config(state='normal')
            self.output_area.delete("1.0", tk.END)
            self.output_area.insert(tk.END, translated)
            self.output_area.config(state='disabled')
            self.history_records.insert(0, self.services['HistoryRecord'](input_text, translated, current_style))
            if len(self.history_records) > self.services['MAX_HISTORY']:
                self.history_records = self.history_records[:self.services['MAX_HISTORY']]
            self.services['save_history'](self.history_records)

        except Exception as e:
            messagebox.showerror("错误", f"翻译失败: {str(e)}")

    def copy_result(self):
        try:
            content = self.output_area.get("1.0", tk.END).strip()
            if content:
                self.services['pyperclip'].copy(content)
                messagebox.showinfo("复制成功", "结果已复制到剪贴板")
        except Exception as e:
            messagebox.showerror("复制失败", f"无法复制内容: {str(e)}")

    def show_history(self):
        history_win = tk.Toplevel(self.root)
        history_win.title("历史记录")
        history_win.geometry("600x300")

        tree = ttk.Treeview(history_win, columns=self.services['HISTORY_COLUMNS'], show="headings")
        for col in self.services['HISTORY_COLUMNS']:
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
                    self.services['pyperclip'].copy(values[2])
                    messagebox.showinfo("已复制", "输出已复制到剪贴板")

        tree.bind("<Double-1>", on_double_click)

    def init_tts_engine(self):
        try:
            engine = self.services['pyttsx3'].init()
            for voice in engine.getProperty('voices'):
                if 'Chinese' in voice.name:
                    engine.setProperty('voice', voice.id)
                    engine.setProperty('rate', 160)
                    return engine
            messagebox.showwarning("警告", "未找到中文语音引擎")
            return None
        except Exception as e:
            messagebox.showerror("错误", f"语音引擎初始化失败：{str(e)}")
            return None

    def speak_aminoac(self):
        if not self.engine:
            return
        input_text = self.input_area.get("1.0", tk.END).strip()
        if not input_text:
            messagebox.showinfo("提示", "没有可朗读的内容")
            return

        def _speak_thread():
            try:
                with self.audio_lock:
                    self.engine.save_to_file(input_text, self.services['TEMP_AUDIO'])
                    self.engine.runAndWait()
                    time.sleep(0.1)
                    if not os.path.exists(self.services['TEMP_AUDIO']):
                        raise FileNotFoundError("音频文件未生成")
                    audio = AudioSegment.from_wav(self.services['TEMP_AUDIO'])
                    reversed_audio = audio.reverse()
                    played = False
                    try:
                        play(reversed_audio)
                        played = True
                    except Exception as e:
                        print(f"pydub play failed: {e}")
                    if not played:
                        rev_path = os.path.join(self.services['HISTORY_DIR'], f"reversed_audio_{int(time.time()*1000)}.wav")
                        import wave as _wave
                        with _wave.open(rev_path, 'wb') as wf:
                            wf.setnchannels(reversed_audio.channels)
                            wf.setsampwidth(reversed_audio.sample_width)
                            wf.setframerate(reversed_audio.frame_rate)
                            wf.writeframes(reversed_audio.raw_data)
                        try:
                            from playsound import playsound
                            playsound(rev_path)
                        except Exception as e:
                            try:
                                import winsound
                                winsound.PlaySound(os.path.abspath(rev_path), winsound.SND_FILENAME)
                            except Exception as e2:
                                messagebox.showerror("错误", f"播放失败：{e2}")
                    try:
                        if os.path.exists(self.services['TEMP_AUDIO']):
                            os.remove(self.services['TEMP_AUDIO'])
                    except Exception:
                        pass
            except Exception as e:
                messagebox.showerror("错误", f"朗读失败：{str(e)}")

        threading.Thread(target=_speak_thread, daemon=True).start()


def start_gui(services: dict):
    root = tk.Tk()
    app = TranslationApp(root, services)
    try:
        root.mainloop()
    finally:
        services['save_history'](app.history_records)
    return app
