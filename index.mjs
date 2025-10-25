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

let partial = "";

while (true) {
  const { done, value } = await reader.read();
  if (done) break;

  const chunk = decoder.decode(value, { stream: true });
  
  // Ollama envía una línea JSON por cada fragmento
  const lines = chunk.split("\n").filter(line => line.trim() !== "");

  for (const line of lines) {
    try {
      const data = JSON.parse(line);
      if (data.response) {
        partial += data.response;
        process.stdout.write(data.response);
      }
      
    } catch (e) {
    
    }
    
  }
}

console.log("\n\n✅ Stream finalizado.");