import subprocess
import sys

# 需要的第三方模块（模块名: 推荐的安装命令）
required_packages = {
    "pyttsx3": "pyttsx3 pywin32",
    "pypinyin": "pypinyin",
    "jieba": "jieba",
    "pdfplumber": "pdfplumber",
    "pyperclip": "pyperclip",
    "pydub": "pydub",
    "playsound": "playsound",
    "python-docx": "python-docx",
}

def is_installed(module_name):
    try:
        __import__(module_name)
        return True
    except ImportError:
        return False

def install_package(packages_str):
    print(f"正在安装：{packages_str}")
    subprocess.check_call([sys.executable, "-m", "pip", "install"] + packages_str.split())

def main():
    missing = []
    for module, install_cmd in required_packages.items():
        if not is_installed(module):
            print(f"[缺少] {module}")
            missing.append(install_cmd)
    
    if missing:
        all_to_install = " ".join(set(missing))
        print(f"\n需要安装的依赖包：{all_to_install}\n")
        try:
            install_package(all_to_install)
            print("\n✅ 所有缺失模块已安装完毕！")
        except Exception as e:
            print(f"❌ 安装失败: {e}")
            print("请手动运行：")
            print(f"pip install {all_to_install}")
    else:
        print("\n✅ 所有依赖模块都已安装，无需操作。")

if __name__ == "__main__":
    main()
    print("检查完成！")