

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