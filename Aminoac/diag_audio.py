import os
import contextlib
import wave
import sys
from pydub import AudioSegment

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(os.path.dirname(PROJECT_ROOT), "output")
TEMP_AUDIO = os.path.join(OUTPUT_DIR, "temp_audio.wav")
REVERSED = os.path.join(OUTPUT_DIR, "reversed_audio.wav")

def print_info(path):
    print("===", path)
    print("exists:", os.path.exists(path))
    if not os.path.exists(path):
        print()
        return
    try:
        print("size:", os.path.getsize(path), "bytes")
    except Exception as e:
        print("size error:", e)
    try:
        with contextlib.closing(wave.open(path, 'rb')) as wf:
            print("wave: channels=", wf.getnchannels(), "sampwidth=", wf.getsampwidth(), "framerate=", wf.getframerate(), "nframes=", wf.getnframes(), "comptype=", wf.getcomptype())
    except Exception as e:
        print("wave open failed:", e)
    try:
        seg = AudioSegment.from_file(path)
        print("pydub: channels=", seg.channels, "frame_rate=", seg.frame_rate, "sample_width=", seg.sample_width, "duration_ms=", len(seg))
    except Exception as e:
        print("pydub failed:", e)
    print()

if __name__ == '__main__':
    print("PROJECT_ROOT:", PROJECT_ROOT)
    print("OUTPUT_DIR:", OUTPUT_DIR)
    print_info(TEMP_AUDIO)
    print_info(REVERSED)

    # If temp exists, try to re-export it as PCM 16-bit WAV for testing
    if os.path.exists(TEMP_AUDIO):
        fixed = os.path.join(OUTPUT_DIR, "temp_fixed.wav")
        try:
            seg = AudioSegment.from_file(TEMP_AUDIO)
            # write using wave module to avoid ffmpeg
            import wave as _wave
            with _wave.open(fixed, 'wb') as _wf:
                _wf.setnchannels(seg.channels)
                _wf.setsampwidth(seg.sample_width)
                _wf.setframerate(seg.frame_rate)
                _wf.writeframes(seg.raw_data)
            print("Exported fixed temp to:", fixed, "size:", os.path.getsize(fixed))
            print_info(fixed)
        except Exception as e:
            print("Failed to re-export temp audio:", e)

    # If reversed is missing or empty, create it by reversing TEMP_AUDIO
    try:
        if os.path.exists(TEMP_AUDIO):
            need_create = (not os.path.exists(REVERSED)) or (os.path.exists(REVERSED) and os.path.getsize(REVERSED) == 0)
            if need_create:
                print("Creating reversed audio from temp...")
                seg = AudioSegment.from_file(TEMP_AUDIO)
                rev = seg.reverse()
                import wave as _wave
                with _wave.open(REVERSED, 'wb') as _wf:
                    _wf.setnchannels(rev.channels)
                    _wf.setsampwidth(rev.sample_width)
                    _wf.setframerate(rev.frame_rate)
                    _wf.writeframes(rev.raw_data)
                print("Reversed audio written to", REVERSED, "size", os.path.getsize(REVERSED))
                print_info(REVERSED)
    except Exception as e:
        print("Failed to create reversed audio:", e)