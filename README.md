# Second Brain Knowledge Graph
Un sistema RAG de gestión del conocimiento 100% local, diseñado para procesar, interconectar y consultar archivos `.md` de Obsidian mediante procesamiento del lenguaje natural (NLP) y LLMs.

## Arquitectura del Sistema

El proyecto aborda el reto del Coste de Inferencia en Machine Learning dividiendo la carga computacional en dos fases:

1. **Batch Processing (Heavy-Compute / Cloud):** Indexación masiva del corpus histórico. Utiliza GPUs de alto rendimiento (ej. Kaggle T4x2) para generar embeddings mediante `sentence-transformers`, calcular similitudes cosenoidales e inyectar *backlinks* lógicos en los archivos legacy.
2. **Streaming & Ingesta Continua (Low-Compute / Local):** Un pipeline de inferencia local y de baja latencia utilizando LLMs cuantizados (formato GGUF, ej. Llama 3 8B / Mistral) para procesar nuevas notas capturadas vía Web Clipper, extraer entidades e integrarlas al grafo de conocimiento sin depender de APIs de terceros.

##  Stack Tecnológico

*   **Embeddings & Vectorización:** PyTorch, HuggingFace (`sentence-transformers`).
*   **Base de Datos Vectorial:** ChromaDB / DuckDB.
*   **Local LLM Engine:** Ollama / vLLM / Llama.cpp.
*   **Automatización:** Python, Model Context Protocol (MCP).
*   **Interfaz Gráfica / Grafo:** Obsidian.

##  Flujo de Datos (Pipeline)

1. **`/raw`**: Punto de entrada de datos no estructurados (capturas web, transcripciones).
2. **Ingesta Autónoma**: Un agente local lee, resume y extrae taxonomía de la nueva nota.
3. **`/wiki`**: Almacenamiento estructurado donde los nodos interactúan mediante métricas de similitud vectorial.
