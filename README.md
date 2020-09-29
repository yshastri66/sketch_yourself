# Sketch Yourself
### Clone this repository by downloading zip or by running following command in Git or terminal :
```
https://github.com/yshastri66/sketch_yourself.git
```
### Create a new python environment and install the requirments using requirment.txt file by executing following commands : 
``` conda create -n env_name
    conda activate env_name
    pip install -r requirment.txt
```

### You can draw yourself like an artist by just running one command in your terminal or Anaconda prompt :
```
python sketch_yourself.py
```


Here I used OpenCV library for getting sketch. I used Gaussian Blur for cleaning up noises. Canny library to get edges or lines in the image.

### You can adjust the contrast by using 'Trackbar' which will be at the bottom left corner of the window as shown in below image : 
![toolbar image](https://github.com/yshastri66/sketch_yourself/blob/master/images/toolbar.png)

### Press 'S' to save the image when you like the image.The resulting image will be of '.jpg' format and saved in the name of sketch.jpg. An example is shown below :
![example image](https://github.com/yshastri66/sketch_yourself/blob/master/images/sketch.jpg)
