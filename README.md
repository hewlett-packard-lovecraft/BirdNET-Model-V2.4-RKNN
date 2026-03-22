# BirdNET-Model-V2.4-RKNN
Script for converting BirdNET Model V2.4 to RKNN format for use on RK3588

## Notes
doesn't work. will segmentation fault. also requires at least 140GB of ram. 
- `W build: The weight (148269 MiB) of the model is too large, only the basic graph is saved to 'check3_fuse_ops.onnx'!`
- onnx-converter converted the entire model to fp16, memory requirements are the same
  - `W load_onnx: Please note that some float16/float64 data types in the model have been modified to float32!`
- rknn can't accept arbitrary inputs
  - `python -m onnxruntime.tools.make_dynamic_shape_fixed --dim_param batch --dim_value 1 birdnet-fp16.onnx birdnet-fp16-fixed.onnx`

birdnet-fp16-fixed.onnx:
``` 
E RKNN: [20:36:21.810] failed to malloc cpu memory, size: 18446744072612741120
```

birdnet-int8-fixed.onnx:

``` 
ValueError: The DynamicQuantizeLinear('model/MEL_SPEC1/stft/mul_C_0_QuantizeLinear') will cause the graph to be a dynamic graph! Remove it manually and try again!
```

next steps:
- quantize birdnet-fp16-fixed.onnx to int8 through rknn-toolkit
- use onnxruntime to do static quantization before converting to rknn

	
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
