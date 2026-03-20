import sys, os
from rknn.api import RKNN

DEFAULT_QUANT = os.getenv("DEFAULT_QUANT", False)
MODEL_PATH = "./models/birdnet.onnx"

if __name__ == "__main__":
    model_path = MODEL_PATH
    platform = "rk3588"
    output_path = "./models/birdnet.rknn"
    do_quant = False

    # Create RKNN object
    rknn = RKNN(verbose=False)

    # Pre-process config
    print("--> Config model")
    rknn.config(target_platform=platform)
    print("done")

    # Load model
    print("--> Loading model")
    ret = rknn.load_onnx(
        model=model_path,
        inputs=["input"],
        input_size_list=[[1, 144000]],  # 1 is batch size
        outputs=["output"],
    )
    if ret != 0:
        print("Load model failed!")
        exit(ret)
    print("done")

    # Build model
    print("--> Building model")
    ret = rknn.build(
        do_quantization=do_quant,
        # rknn_batch_size=8,
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
