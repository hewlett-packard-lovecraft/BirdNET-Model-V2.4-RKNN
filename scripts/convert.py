import sys, os
from rknn.api import RKNN

DEFAULT_QUANT = os.getenv("DEFAULT_QUANT", False)
MODEL_PATH = "../birdnet_fp16_fixed.onnx"

if __name__ == "__main__":
    model_path = MODEL_PATH
    platform = "rk3588"
    output_path = "../BirdNET_fixed_fp16.rknn"
    do_quant = True

    # Create RKNN object
    rknn = RKNN(verbose=True)

    # Pre-process config
    print("--> Config model")
    rknn.config(
        target_platform=platform,
        optimization_level=3,
        quantized_dtype="w8a8",
        #float_dtype="float16",
    )
    
    print("done")

    # Load model
    print("--> Loading model")
    ret = rknn.load_onnx(
        model=model_path,
        # inputs=["input"],
        # input_size_list=[[1, 144000]]
        # outputs=["output"],
    )
    if ret != 0:
        print("Load model failed!")
        exit(ret)
    print("done")

    # Build model
    print("--> Building model")
    ret = rknn.build(
        do_quantization=do_quant,
        auto_hybrid=True,
        dataset="./example/dataset.txt",
        # rknn_batch_size=3,
        # auto_hybrid=True,
    )
    if ret != 0:
        print("Build model failed!")
        exit(ret)
    print("done")

    # Export rknn model
    print("--> Export rknn model")
    ret = rknn.export_rknn(output_path)
    if ret != 0:
        print("Export rknn model failed!")
        exit(ret)
    print("done")

    # Release
    rknn.release()
