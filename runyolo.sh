#!/bin/sh

cd ../darknet
rm predictions.jpg
echo "removed \n"
timeout 3s ./darknet detect cfg/yolo.cfg yolo.weights inputImage.jpg
rm inputImage.jpg
exit 0