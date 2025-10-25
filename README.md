# 🚀 Ollama Streaming Client

Cliente minimalista en Node.js para consumir la API de Ollama en modo streaming, permitiendo respuestas de modelos LLM en tiempo real.

## ✨ Características

- 🔄 **Streaming en tiempo real**: Visualiza la generación de texto token por token
- 🏠 **100% local**: Sin dependencias de servicios cloud
- 🪶 **Zero dependencies**: Usa únicamente APIs nativas de Node.js
- 🔒 **Privacidad total**: Tus datos nunca salen de tu máquina
- ⚡ **Latencia mínima**: Procesamiento local sin roundtrips

## 📋 Requisitos

- Node.js 18+ (soporte nativo para fetch)
- [Ollama](https://ollama.ai/) instalado y corriendo localmente

## 🔧 Instalación

```bash
# Instalar Ollama (si aún no lo tienes)
# macOS/Linux
curl -fsSL https://ollama.ai/install.sh | sh

#Windows
descargar la aplicacion

# Descargar un modelo (ejemplo con phi3)
ollama pull phi3

# Clonar este repositorio
git clone https://github.com/ycaballero12315/ollama-js.git
cd ollama-js

Nota: ignorar el modulo python es para LMMs pero usando la GPU de Google Colab
# No se requieren dependencias npm
node index.mjs
```

## 💻 Uso

```javascript
const response = await fetch('http://localhost:11434/api/generate', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    model: 'phi3',
    prompt: 'Explica que son los embeddings y da un ejemplo sencillo',
    temperature: 0.8,
    stream: true
  })
});

const reader = response.body.getReader();
const decoder = new TextDecoder("utf-8");

while (true) {
  const { done, value } = await reader.read();
  if (done) break;

  const chunk = decoder.decode(value, { stream: true });
  const lines = chunk.split("\n").filter(line => line.trim() !== "");

  for (const line of lines) {
    try {
      const data = JSON.parse(line);
      if (data.response) {
        process.stdout.write(data.response);
      }
    } catch (e) {
      // Ignorar líneas mal formadas, mostrar resultado limpio
    }
  }
}
```

## 🎯 Casos de Uso

- **Chatbots corporativos**: Asistentes internos sin filtración de datos
- **Herramientas de análisis**: Procesamiento de documentos confidenciales
- **Prototipado rápido**: Experimenta sin costos por API
- **Educación**: Aprende sobre LLMs sin barreras de entrada

## 📚 Modelos Compatibles

Este cliente funciona con cualquier modelo disponible en Ollama:
Ejemplos:
```bash
ollama pull llama2       # Meta Llama 2 (7B)
ollama pull mistral      # Mistral 7B
ollama pull codellama    # Code Llama (código)
ollama pull phi3         # Microsoft Phi-3
ollama pull gemma        # Google Gemma
```

## 🔍 Arquitectura

El cliente implementa el patrón de **streaming HTTP** usando:

1. **Fetch API**: Realiza peticiones HTTP nativas
2. **ReadableStream**: Procesa chunks de datos incrementalmente
3. **TextDecoder**: Decodifica bytes UTF-8 en tiempo real
4. **NDJSON parsing**: Procesa JSON line-delimited

```
┌─────────────┐      HTTP POST       ┌──────────────┐
│   Cliente   │ ──────────────────> │    Ollama    │
│  (Node.js)  │                      │   (Local)    │
│             │ <────────────────── │              │
└─────────────┘   Streaming chunks   └──────────────┘
                  (NDJSON format)
```

## ⚙️ Configuración

Personaliza el comportamiento modificando los parámetros:

```javascript
{
  model: 'phi3',           // Modelo a usar
  prompt: 'Tu pregunta',   // Prompt de entrada
  temperature: 0.8,        // Creatividad (0.0 - 1.0)
  stream: true,            // Habilitar streaming
  top_p: 0.9,              // Nucleus sampling (opcional)
  top_k: 40                // Top-k sampling (opcional)
}
```

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar este proyecto:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Roadmap

- [ ] Soporte para múltiples modelos simultáneos
- [ ] Interfaz web simple con Server-Sent Events
- [ ] Métricas de rendimiento (tokens/segundo)
- [ ] Persistencia de conversaciones
- [ ] Integración con Langchain.js

## 🙏 Agradecimientos

- [Ollama](https://ollama.ai/) - Por democratizar el acceso a LLMs locales
- Comunidad open source de Node.js

## 📧 Contacto

¿Preguntas o sugerencias? Abre un issue o contáctame en (https://www.linkedin.com/in/yoeny-caballero-gonzalez/)

---

⭐ Si este proyecto te resultó útil, ¡considera darle una estrella!
