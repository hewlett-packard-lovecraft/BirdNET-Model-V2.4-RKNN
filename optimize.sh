#!/usr/bin/env bash

python -m onnxruntime.tools.make_dynamic_shape_fixed --dim_param batch --dim_value 1 "./models2/BirdNET_fp16.onnx" "./birdnet_fp16_fixed.onnx"
python -m onnxruntime.tools.make_dynamic_shape_fixed --dim_param batch --dim_value 1 "./models2/BirdNET_int8_arm.onnx" "./birdnet_int8_arm_fixed.onnx"
python -m onnxruntime.tools.make_dynamic_shape_fixed --dim_param batch --dim_value 1 "./models2/BirdNET_int8.onnx" "./birdnet_int8_fixed.onnx"
