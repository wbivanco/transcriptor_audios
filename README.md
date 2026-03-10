# Transcriptor de audios OGG con Whisper

Transcribe archivos de audio en formato **OGG** usando [OpenAI Whisper](https://github.com/openai/whisper) y guarda cada transcripción en un archivo `.txt` en la carpeta `textos`.

## Requisitos

- **Python 3.8+**
- **FFmpeg** instalado en el sistema (Whisper lo usa para leer audio).

### Instalar FFmpeg

- **Ubuntu/Debian:** `sudo apt update && sudo apt install ffmpeg`
- **macOS:** `brew install ffmpeg`
- **Windows:** [Descargar desde ffmpeg.org](https://ffmpeg.org/download.html) o `choco install ffmpeg`

## Instalación

```bash
cd transcriptor_audios
python -m venv .venv
source .venv/bin/activate   # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Uso

1. Coloca tus archivos `.ogg` en la carpeta **`audios`** (crea la carpeta si no existe).
2. Ejecuta:

```bash
python transcribe_ogg.py
```

Las transcripciones se guardan en la carpeta **`textos`**, con el mismo nombre del audio y extensión `.txt`.

### Opciones

| Opción       | Descripción                                      | Por defecto |
|-------------|---------------------------------------------------|-------------|
| `--audios`  | Carpeta con los archivos .ogg                     | `audios`    |
| `--textos`  | Carpeta donde guardar los .txt                    | `textos`    |
| `--modelo`  | Modelo Whisper: tiny, base, small, medium, large  | `base`      |
| `--idioma`  | Código de idioma (ej. es, en)                     | `es`        |

Ejemplos:

```bash
# Usar modelo más preciso (más lento)
python transcribe_ogg.py --modelo medium

# Transcripción en inglés
python transcribe_ogg.py --idioma en

# Rutas personalizadas
python transcribe_ogg.py --audios mis_audios --textos mis_textos
```

## Estructura del proyecto

```
transcriptor_audios/
├── audios/          # Aquí van los archivos .ogg
├── textos/          # Aquí se generan los .txt
├── transcribe_ogg.py
├── requirements.txt
└── README.md
```
