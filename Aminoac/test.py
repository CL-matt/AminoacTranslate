import os
import sys
base_dir = os.path.dirname(os.path.abspath(__file__))
libs_path = os.path.join(base_dir, "libs")
sys.path.insert(0, libs_path)
print("当前 Python 路径:", sys.path)