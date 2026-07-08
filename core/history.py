import json
import os
from datetime import datetime

# Use project root relative path for output
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HISTORY_DIR = os.path.join(PROJECT_ROOT, "output")
os.makedirs(HISTORY_DIR, exist_ok=True)
HISTORY_FILE = os.path.join(HISTORY_DIR, "translation_history.json")


class HistoryRecord:
    def __init__(self, input: str, output: str, style):
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.input = input[:30]
        self.output = output[:30]
        # accept a ToneStyle or a plain string
        self.style = style.name if hasattr(style, 'name') else str(style)


def save_history(history_records):
    """保存历史记录到文件"""
    data = [{
        "timestamp": r.timestamp,
        "input": r.input,
        "output": r.output,
        "style": r.style
    } for r in history_records]
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)


def load_history():
    """从文件加载历史记录"""
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [HistoryRecord(item.get("input", ""), item.get("output", ""), item.get("style", "")) for item in data]
    return []