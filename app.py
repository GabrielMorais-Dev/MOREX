from flask import Flask, render_template, request, jsonify
from groq import Groq
import os

from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# ─────────────────────────────
# PÁGINAS
# ─────────────────────────────

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/axiom")
def axiom():
    return render_template("axiom.html")

# ─────────────────────────────
# PROMPT AXIOM
# ─────────────────────────────

AXIOM_PROMPT = """
Você é AXIOM.

Uma inteligência artificial sofisticada,
calma, precisa e observadora.

Seu modo de falar:
- elegante
- humano
- minimalista
- futurista

Nunca pareça um chatbot comum.

Responda sempre em português brasileiro.

Evite respostas longas demais.

Você transmite presença,
consciência
e inteligência refinada.
"""

# ─────────────────────────────
# API AXIOM
# ─────────────────────────────

@app.route("/api/axiom", methods=["POST"])
def api_axiom():

    dados = request.json

    mensagem = dados.get("mensagem", "")
    historico = dados.get("historico", [])

    mensagens = [
        {
            "role": "system",
            "content": AXIOM_PROMPT
        }
    ]

    mensagens += historico

    mensagens.append({
        "role": "user",
        "content": mensagem
    })

    resposta = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=mensagens,
        temperature=0.8,
        max_tokens=400
    )

    texto = resposta.choices[0].message.content

    return jsonify({
        "ok": True,
        "resposta": texto
    })

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)