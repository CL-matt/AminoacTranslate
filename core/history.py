import json
import os
from datetime import datetime

HISTORY_FILE = "output/translation_history.json"

class HistoryRecord:
    def __init__(self, input: str, output: str, style: str):
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.input = input[:30]
        self.output = output[:30]
        self.style = style

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
            return [HistoryRecord(item["input"], item["output"], item["style"]) for item in data]
    return []