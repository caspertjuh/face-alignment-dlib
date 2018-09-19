Batch Face Alignment
===

This is a script for detecting and aligning faces in batch images for processing.
Alignment is a process of rotating a face to a vertically straight orientation, should the original face image is tilted.

#### Setup:
1. Run `pip install -r requirements.txt`, or alternatively install dependencies manually.
2. Download and extract shape predictor 68 landmarks at this [link](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2).
3. Place the extracted predictor in the root directory of this project.
4. Find some images with faces, most images from portraits to group photos should work as long as the resolution not too small.

#### Run:
```bash
python app.py inputfolder outputfolder
```

#### Example:
>Example input
![Input](https://i.imgur.com/VmBWpdp.png)
>Example output
![Output](https://i.imgur.com/3hQ5n8L.png)
##### Dependencies:
- [dlib](http://dlib.net/)
- [opencv-python](http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html)

##### Known bugs:
- Sometimes faces do not get detected and thus fail to get extracted.
