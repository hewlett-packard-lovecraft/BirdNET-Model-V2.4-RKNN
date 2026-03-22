	
FROM	airockchip/rknn-toolkit2
WORKDIR	/usr/src/birdnet

CMD ["python", "convert.py"]
