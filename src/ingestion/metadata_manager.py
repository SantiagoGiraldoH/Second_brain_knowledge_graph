import frontmatter
import os
from dotenv import load_dotenv

# Cargar las variables de tu archivo .env
load_dotenv()

def inyectar_etiquetas(ruta_archivo, nuevas_etiquetas):
    # (Aquí va la misma lógica que ya escribimos en el paso anterior)
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        nota = frontmatter.load(f)
    
    etiquetas_actuales = nota.metadata.get('tags', [])
    if isinstance(etiquetas_actuales, str):
        etiquetas_actuales = [etiquetas_actuales]
        
    etiquetas_combinadas = list(set(etiquetas_actuales + nuevas_etiquetas))
    nota.metadata['tags'] = etiquetas_combinadas
    
    with open(ruta_archivo, 'w', encoding='utf-8') as f:
        f.write(frontmatter.dumps(nota))
        
    print(f"Archivo {os.path.basename(ruta_archivo)} actualizado con éxito.")

