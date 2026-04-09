# split sound files into 3-second chunks and save them as .npy files for quantization

import argparse
from pathlib import Path
import librosa
import numpy as np
import numpy.typing as npt
import onnxruntime as ort


DOCKER_DATASET_ABSOLUTE_PATH = "/home/hxia/git/BirdNET-Model-V2.4-RKNN/dataset"


def split_audio_file(
    src: Path,
    dest: Path,
    rate: float = 48000,
    overlap: float = 0.0,
    seconds: float = 3.0,
    min_len: float = 1.5,
):
    print(f"Reading {src.name} ... ", end=" ", flush=True)

    # see: https://github.com/birdnet-team/BirdNET-Lite/blob/main/analyze.py#L115
    signal, rate = librosa.load(
        path=src.absolute(), sr=rate, mono=True, res_type="kaiser_fast"
    )

    chunks: list[npt.NDArray[np.float32]] = []

    for i in range(0, len(signal), int((seconds - overlap) * rate)):
        chunk = signal[i : i + int(seconds * rate)]

        if len(chunk) < int(min_len * rate):
            break

        if len(chunk) < int(rate * seconds):
            temp = np.zeros((int(rate * seconds)))
            temp[: len(chunk)] = chunk
            chunk = temp

        # input expects float32. reshape from [144000] to [1, 14000]
        chunk = np.expand_dims(chunk.astype(np.float32), axis=0)

        chunks.append(chunk.astype(np.float32))

    print(f"Done! Read {str(len(chunks))} chunks. ")

    file_name = src.name
    # timestamp = datetime.now()

    print(f"Writing {file_name} chunks to {dest.name}")

    chunk_paths: list[str] = []

    for i, chunk in enumerate(chunks):
        chunk_name: str = (
            # timestamp.strftime("%Y-%m-%d-%H:%M:%S") +
            file_name + "_" + str(i) + ".npy"
        )
        chunk_dest = dest / chunk_name

        np.save(str(chunk_dest.absolute()), chunk)
        chunk_paths.append(DOCKER_DATASET_ABSOLUTE_PATH + "/" + chunk_name + "\n")

    return chunk_paths


class Args(argparse.Namespace):
    src: list[str] = ["../example/"]
    dest: str = "../dataset/"
    txt: str = "../dataset.txt"


def main():
    parser = argparse.ArgumentParser()
    _ = parser.add_argument(
        "--src",
        type=list[str],
        # action="append",
        nargs="+",
        help="Path to input file directory",
        default=["../example/"],
    )

    _ = parser.add_argument("--dest", type=str, help="Path to output file directory")
    _ = parser.add_argument(
        "--txt", type=str, help="Path to dataset.txt", default="../dataset.txt"
    )

    args = parser.parse_args(namespace=Args())

    src: list[str] = args.src
    dest = Path(args.dest)
    txt = Path(args.txt)

    dataset_txt: list[str] = []

    for dir in src:
        dir = "".join(dir)
        print(f"Reading {dir} ...")

        for s in Path(dir).iterdir():
            if s.suffix != ".mp3" and s.suffix != ".wav":
                continue

            dataset_txt += split_audio_file(src=s, dest=dest)

    with open(txt, "w") as f:
        f.writelines(dataset_txt)

    print(f"Done! wrote {str(len(dataset_txt))} lines to {txt}. ")


if __name__ == "__main__":
    main()
