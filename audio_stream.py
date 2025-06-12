import sounddevice as sd
import numpy as np

DURACION_CHUNK = 1  # segundos
SAMPLERATE = 16000

def start_audio_stream(callback):
    print("[audio_stream] 🔊 Iniciando stream de audio...")
    def consumer():
        while True:
            audio_chunk = sd.rec(int(DURACION_CHUNK * SAMPLERATE), samplerate=SAMPLERATE, channels=1, dtype='int16')
            sd.wait()
            audio_data = np.squeeze(audio_chunk)
            print("[audio_stream] Chunk de audio recibido.")
            print("[audio_stream] ⏱ Procesando nuevo fragmento...")
            callback(audio_data, SAMPLERATE)

    print("[audio_stream] 🌀 Hilo de procesamiento iniciado.")
    consumer()
