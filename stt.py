import vosk
import wave
import os
import numpy as np

# Cargar modelo solo una vez
model = vosk.Model("models/vosk-es")

def transcribe(audio_data, samplerate):
    wf_path = "temp.wav"
    try:
        # Guardar audio temporal
        with wave.open(wf_path, "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(samplerate)
            wf.writeframes((audio_data * 32767).astype(np.int16).tobytes())

        # Transcribir
        rec = vosk.KaldiRecognizer(model, samplerate)
        with wave.open(wf_path, "rb") as wf:
            while True:
                data = wf.readframes(4000)
                if len(data) == 0:
                    break
                rec.AcceptWaveform(data)

        result = rec.Result()
        text = eval(result).get("text", "")
        return text.strip()
    finally:
        if os.path.exists(wf_path):
            os.remove(wf_path)
