import sys, os
from rknn.api import RKNN

DEFAULT_QUANT = os.getenv("DEFAULT_QUANT", False)
MODEL_PATH = "./birdnet.tail.onnx"

if __name__ == "__main__":
    model_path = MODEL_PATH
    platform = "rk3588"
    output_path = "birdnet.tail.rknn"
    do_quant = False

    # Create RKNN object
    rknn = RKNN(verbose=True, verbose_file="./rknn_log.txt")

    # Pre-process config
    print("--> Config model")
    rknn.config(
        target_platform=platform,
        optimization_level=3, # 3,
        quantized_dtype="w8a8",
        quantized_algorithm='normal', 
        quantized_method='channel',
        #remove_reshape=True,
        enable_flash_attention=True
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
        #auto_hybrid=True,
        #dataset="./dataset.txt",
        rknn_batch_size=3,
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

    
