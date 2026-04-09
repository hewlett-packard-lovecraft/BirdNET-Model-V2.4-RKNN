# BirdNET-Model-V2.4-RKNN
Script for converting BirdNET Model V2.4 to RKNN format for use on RK3588, will quantize from FP32 to fp16/int16


## Models
- meta_model.rknn
- birdnet.tail.rknn
- birdnet.head.onnx

birdnet v2.4 takes in 3 seconds of audio at 48000 hz and constructs a mel-spectrogram. however, due to rknpu's maximum dim size of 8191, it's not possible to convert a layer with dimensions [1, 144000] to rknn format. so, we convert birdnet.onnx from justinchuby to a fixed input size, and split it into two models

birdnet.head.onnx takes in audio samples and generates the spectrogram

birdnet.tail.rknn takes in the spectrogram and outputs confidence scores for all 6522 species

meta_model.rknn is the BirdNET v2.4 range model converted from tflite to rknn. it takes in latitude, longitude, week, and outputs label, and confidence scores for each species

## TODO
- come up with a better solution that running the birdnet.tail.onnx on cpu
- check out birdnet-v3-dev, and perchv2 to rknn
- v3 has as it has variable length input
- 32khz and not 48khz


## Usage

`git clone --recurse-submodules https://github.com/hewlett-packard-lovecraft/BirdNET-Model-V2.4-RKNN`

### Docker

``` shell
bash launch.sh
python3 convert.py
```

## nix
``` shell
nix-shell
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 convert.py
```

## Source

- https://huggingface.co/justinchuby/BirdNET-onnx

```bibtex
@article{kahl2021birdnet,
  title={BirdNET: A deep learning solution for avian diversity monitoring},
  author={Kahl, Stefan and Wood, Connor M and Eibl, Maximilian and Klinck, Holger},
  journal={Ecological Informatics},
  volume={61},
  pages={101236},
  year={2021},
  publisher={Elsevier}
}
```
