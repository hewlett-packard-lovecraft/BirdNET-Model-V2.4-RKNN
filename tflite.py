from pyexpat import model
import sys, os
from rknn.api import RKNN


def get_env():
    model_path = os.getenv("MODEL_PATH", "./models/audio-model-fp16.tflite")
    platform = os.getenv("PLATFORM", "RK3588")
    output_path = os.getenv("OUTPUT_PATH", "./models/audio-model-fp16.rknn")
    rknn_batch_size = int(os.getenv("RKNN_BATCH_SIZE", 8))
    input_batch_size = int(os.getenv("INPUT_BATCH_SIZE", 128))

    return model_path, platform, output_path, rknn_batch_size, input_batch_size


if __name__ == "__main__":
    model_path, platform, output_path, rknn_batch_size, input_batch_size = get_env()

    # initialize rknn
    rknn = RKNN(verbose=True)

    print("Config RKNN")
    ret = rknn.load_tflite(model=model_path)

    if ret != 0:
        print(f"Loading {model_path} failed!")
        exit(ret)

    print("Done!")

    # build

    print("Build RKNN")
    ret = rknn.build(rknn_batch_size=rknn_batch_size)

    if ret != 0:
        print(f"Building {model_path} failed!")
        exit(ret)
    print("Done!")

    # Export rknn model
    print("Export rknn model")
    ret = rknn.export_rknn(output_path)
    if ret != 0:
        print("Export rknn model failed!")
        exit(ret)
    print("done")

    # Release
    rknn.release()
