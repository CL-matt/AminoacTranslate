import os
import time

import pyttsx3
from pydub import AudioSegment
from pydub.playback import play
from playsound import playsound


def init_tts_engine():
	"""初始化语音引擎，并优先选择中文语音。"""
	try:
		engine = pyttsx3.init()
		for voice in engine.getProperty("voices"):
			if "Chinese" in voice.name:
				engine.setProperty("voice", voice.id)
				engine.setProperty("rate", 160)
				return engine
		return engine
	except Exception as exc:
		print(f"语音引擎初始化失败: {exc}")
		return None


def speak_text(text, engine, temp_audio_path, history_dir):
	"""将输入文本转为音频并播放倒放后的结果。

	步骤：
	1. 使用 `engine.save_to_file` 生成临时音频文件并等待引擎完成。
	2. 等待文件可见并且大小>0（避免文件句柄未释放导致读取失败）。
	3. 使用 pydub 读取 WAV，倒放并导出到 `history_dir/reversed_audio.wav`。
	4. 依次尝试 `playsound`、`winsound`、`pydub.playback.play` 播放，失败则打印信息并回退。
	"""
	if not engine:
		raise RuntimeError("语音引擎不可用")

	# 生成音频文件
	engine.save_to_file(text, temp_audio_path)
	engine.runAndWait()

	# 等待输出文件被写入（有些 TTS 引擎需要短暂时间释放句柄）
	wait_seconds = 5.0
	interval = 0.1
	elapsed = 0.0
	while elapsed < wait_seconds:
		if os.path.exists(temp_audio_path) and os.path.getsize(temp_audio_path) > 0:
			break
		time.sleep(interval)
		elapsed += interval

	if not os.path.exists(temp_audio_path) or os.path.getsize(temp_audio_path) == 0:
		raise FileNotFoundError(f"音频文件未生成或为空: {temp_audio_path}")

	# 读取并倒放音频
	audio = AudioSegment.from_wav(temp_audio_path)
	reversed_audio = audio.reverse()
	# 使用唯一文件名避免播放器/缓存问题
	import time as _time
	basename = f"reversed_audio_{int(_time.time()*1000)}.wav"
	reversed_audio_path = os.path.join(history_dir, basename)
	os.makedirs(history_dir, exist_ok=True)
	# 使用标准库 wave 写入 PCM 数据，避免依赖 ffmpeg
	import wave as _wave
	with _wave.open(reversed_audio_path, 'wb') as _wf:
		_wf.setnchannels(reversed_audio.channels)
		_wf.setsampwidth(reversed_audio.sample_width)
		_wf.setframerate(reversed_audio.frame_rate)
		_wf.writeframes(reversed_audio.raw_data)

	# 播放回放音频：尝试多种方法以适配不同系统和依赖状态
	abs_path = os.path.abspath(reversed_audio_path)
	last_exc = None

	# 1) playsound（通常最简单）
	try:
		playsound(abs_path)
		return
	except Exception as e:
		print(f"playsound 播放失败: {e}")
		last_exc = e

	# 2) winsound（Windows 内建）
	try:
		import winsound

		print("尝试使用 winsound 播放...")
		winsound.PlaySound(abs_path, winsound.SND_FILENAME)
		return
	except Exception as e:
		print(f"winsound 播放失败: {e}")
		last_exc = e

	# 3) pydub.playback.play（回退到内存中的 AudioSegment 播放）
	try:
		print("尝试使用 pydub.playback.play 播放...")
		play(reversed_audio)
		return
	except Exception as e:
		print(f"pydub play 播放失败: {e}")
		last_exc = e

	# 如果都失败，抛出带有最后一个异常信息的错误
	raise RuntimeError(f"无法播放音频，最后的错误: {last_exc}")

