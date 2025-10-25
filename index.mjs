const response = await fetch('http://localhost:11434/api/generate', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    model: 'phi3',
    prompt: 'Explica embeddings',
    temperature: 0.8,
    stream: false
  })
});

const data = await response.json();
console.log(data.response);