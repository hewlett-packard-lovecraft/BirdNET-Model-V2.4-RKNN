# split sound files into 3-second chunks and save them as .npy files for quantization

from logging import _srcfile
from pathlib import Path
from sqlite3 import register_adapter
import librosa
import numpy as np
from numpy.typing import NDArray
from datetime import datetime


def split_chunks(sig, rate=48000, overlap=0.0, seconds=3.0, min_len=1.5):
    chunks = []

    for i in range(0, len(sig), int(seconds - overlap) * rate):
        chunk = sig[i : i + int(seconds * rate)]

        if len(chunk) < int(min_len * rate):
            break

        if len(chunk) < int(rate * seconds):
            temp = np.zeros((int(rate * seconds)))
            temp[: len(chunk)] = chunk
            split = temp

        chunks.append(chunk)

    return chunks


def load_audio_file(src: Path, rate=48000, overlap=0.0):
    print(f"Reading {src.name} ... ", end=" ", flush=True)
    signal, rate = librosa.load(
        path=str(src.absolute()), sr=48000, mono=True, res_type="kaiser_fast"
    )

    chunks = split_chunks(signal, rate, overlap)

    print(f"Done! Read {str(len(chunks))} chunks. ")

    return chunks


def write_chunks(src: Path, dest: Path, chunks: NDArray[np.float64]):
    file_name = src.name
    timestamp = datetime.now()

    print(f"Writing {file_name} chunks to {dest.name}")

    for i, chunk in enumerate(chunks):
        chunk_name: str = (
            timestamp.strftime("%Y-%m-%d-%H:%M:%S") + file_name + "_" + str(i) + ".npy"
        )
        chunk_dest = dest / chunk_name

        np.save(str(chunk_dest.absolute()), chunk)


def main():
    samples = Path("../example/")

    for s in samples.iterdir():
        s.absolute


if __name__ == "__main__":
    main()
