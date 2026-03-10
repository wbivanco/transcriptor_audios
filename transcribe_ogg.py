#!/usr/bin/env python3
"""
Script para transcribir archivos de audio OGG usando Whisper.
Lee audios de la carpeta 'audios' y guarda las transcripciones en 'textos'.
"""

import os
import argparse
from pathlib import Path

import whisper


# Rutas por defecto
AUDIOS_DIR = Path(__file__).parent / "audios"
TEXTOS_DIR = Path(__file__).parent / "textos"


def main():
    parser = argparse.ArgumentParser(description="Transcribir archivos OGG con Whisper")
    parser.add_argument(
        "--audios",
        type=Path,
        default=AUDIOS_DIR,
        help="Carpeta con archivos .ogg (por defecto: audios)",
    )
    parser.add_argument(
        "--textos",
        type=Path,
        default=TEXTOS_DIR,
        help="Carpeta donde guardar los .txt (por defecto: textos)",
    )
    parser.add_argument(
        "--modelo",
        type=str,
        default="base",
        choices=["tiny", "base", "small", "medium", "large", "large-v2", "large-v3"],
        help="Modelo Whisper a usar (por defecto: base)",
    )
    parser.add_argument(
        "--idioma",
        type=str,
        default="es",
        help="Código de idioma para la transcripción (por defecto: es)",
    )
    args = parser.parse_args()

    audios_dir = args.audios.resolve()
    textos_dir = args.textos.resolve()

    if not audios_dir.is_dir():
        print(f"Error: la carpeta de audios no existe: {audios_dir}")
        print("Créala y coloca ahí tus archivos .ogg")
        return 1

    archivos_ogg = list(audios_dir.glob("*.ogg"))
    if not archivos_ogg:
        print(f"No se encontraron archivos .ogg en {audios_dir}")
        return 0

    textos_dir.mkdir(parents=True, exist_ok=True)
    print(f"Cargando modelo Whisper '{args.modelo}'...")
    modelo = whisper.load_model(args.modelo)

    for ruta_audio in sorted(archivos_ogg):
        nombre_base = ruta_audio.stem
        ruta_txt = textos_dir / f"{nombre_base}.txt"
        print(f"Transcribiendo: {ruta_audio.name}")
        resultado = modelo.transcribe(str(ruta_audio), language=args.idioma, fp16=False)
        texto = resultado["text"].strip()
        ruta_txt.write_text(texto, encoding="utf-8")
        print(f"  → {ruta_txt.name}")

    print(f"\nListo. {len(archivos_ogg)} archivo(s) transcrito(s) en {textos_dir}")
    return 0


if __name__ == "__main__":
    exit(main())
