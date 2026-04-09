import onnx
# from onnxruntime.tools import make_input_shape_fixed

# make_dynamic_shape_fixed

FIXED_MODEL = "birdnet.fixed.onnx"
HEAD = "birdnet.head.onnx"
TAIL = "birdnet.tail.onnx"


# model = onnx.load(MODEL_PATH)
# fixed_model = make_input_shape_fixed(model, 1)

# fixed_model.save(model, FIXED_MODEL)

# fixed_model = onnx.load(FIXED_MODEL)


onnx.utils.extract_model(
    input_path=FIXED_MODEL,
    
    output_path=HEAD,
    input_names=["input"],
    output_names=["val_4"],
    check_model=True,
)

onnx.utils.extract_model(
    input_path=FIXED_MODEL,
    output_path=TAIL,
    input_names=["val_4"],
    output_names=["output"],
    check_model=True,
)
