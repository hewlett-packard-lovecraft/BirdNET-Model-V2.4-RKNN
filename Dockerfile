	
FROM	airockchip/rknn-toolkit2
RUN	mkdir -p /usr/src/birdnet
COPY	./BirdNET_v2.4_tflite	/usr/src/birdnet
COPY	./model_config.yml	/usr/src/birdnet
