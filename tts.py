from TTS.api import TTS
import sounddevice as sd

# Cargar modelo de español una sola vez
_tts = TTS("tts_models/es/mai/tacotron2-DDC", progress_bar=False)


def hablar(texto: str) -> None:
    """Reproduce la respuesta generada por la IA usando Coqui TTS."""
    audio = _tts.tts(texto)
    sd.play(audio, _tts.synthesizer.output_sample_rate)
    sd.wait()
