from pypinyin import Style

COLOR_SCHEME = {
    "background": "#F0F3F5",
    "primary": "#2E86C1",
    "secondary": "#5DADE2",
    "text": "#2C3E50",
    "success": "#28B463",
    "warning": "#F1C40F"
}

TONE_STYLES = [
    {"name": "古韵", "style": Style.TONE, "description": "保留声调符号，如 nǐ"},
    {"name": "音韵", "style": Style.TONE2, "description": "用数字表示声调，如 ni3"},
    {"name": "无声调", "style": Style.NORMAL, "description": "移除所有声调符号，如 ni"}
]