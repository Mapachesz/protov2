from gpt4all import GPT4All

# Cargar modelo
model = GPT4All(model_name="mistral-7b-openorca.Q4_0.gguf", allow_download=False)

def responder(texto):
    prompt = f"Eres un asistente útil que responde en español de forma natural y concisa. Responde en menos de 3 líneas.\nUsuario: {texto}\nIA:"
    respuesta = model.generate(prompt)
    return respuesta.strip()
