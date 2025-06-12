import sounddevice as sd
import numpy as np
import queue
import threading
import time
from stt import transcribe
from ia import responder
from tts import hablar

# Configuración de grabación
samplerate = 16000
block_duration = 1  # en segundos
silence_threshold = 0.01  # umbral de silencio
max_silence_blocks = 2

# Estados de control
estado = "ESCUCHANDO"  # Puede ser ESCUCHANDO o PENSANDO

# Buffers y colas
audio_q = queue.Queue()
texto_acumulado = []
silence_count = 0


def audio_callback(indata, frames, time_info, status):
    if status:
        print(f"[audio_stream] ⚠️ Estado del stream: {status}")
    audio_q.put(indata.copy())


def consumer():
    global texto_acumulado, silence_count, estado
    while True:
        data = audio_q.get()
        if estado == "PENSANDO":
            print("[main] 🚫 Estado actual: PENSANDO → Ignorando fragmento.")
            continue

        print("[audio_stream] ⏱ Procesando nuevo fragmento...")
        audio_np = np.concatenate(data, axis=0) if isinstance(data, list) else data
        texto = transcribe(audio_np, samplerate)

        if texto:
            print(f"[main] ✅ Texto detectado: {texto}")
            texto_acumulado.append(texto)
            silence_count = 0
        else:
            silence_count += 1
            print("[main] ⏳ En espera de más voz...")

        # Si hay silencio prolongado y texto acumulado, se responde
        if silence_count >= max_silence_blocks and texto_acumulado:
            estado = "PENSANDO"
            pregunta = ' '.join(texto_acumulado)
            print(f"[main] 🧠 Pensando respuesta para: {pregunta}")
            respuesta = responder(pregunta)
            print(f"[main] 🤖 IA responde: {respuesta}")
            hablar(respuesta)
            texto_acumulado = []
            silence_count = 0
            estado = "ESCUCHANDO"


if __name__ == "__main__":
    print("📱 Llamada iniciada. Habla cuando quieras...")
    print("🔊 [audio_stream] Iniciando stream de audio...")
    stream = sd.InputStream(callback=audio_callback, samplerate=samplerate, channels=1, blocksize=int(samplerate * block_duration))

    with stream:
        print("🌀 [audio_stream] Hilo de procesamiento iniciado.")
        threading.Thread(target=consumer, daemon=True).start()
        try:
            while True:
                time.sleep(0.1)
        except KeyboardInterrupt:
            print("\n👋 Llamada finalizada por el usuario.")
