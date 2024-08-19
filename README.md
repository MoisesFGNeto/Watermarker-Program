## Watermarker Program
This Python program creates watermarks with text and logos to protect your photos.

#### Requirements
- Python 3.x
- PIL (Python Imaging Library)
***
#### Step - 1: Prepare Your Images
Create a folder named `/images` in your project directory and place all the images you want to watermark into this folder. (Please DO NOT change the folder's name).

![Create /images folder](./screen-shots/image-folder.png)
***
**Images inside the folder:**
![Images in /images folder](./screen-shots/all-images-in-folder.png)
***
#### Step - 2 (Optional): Add a Logo
If you want to add a logo to your images, create a folder named `/logo` and place your logo image in this folder. Valid extensions are: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`, `.tiff`.

![Create /logo folder](./screen-shots/logo-folder.png)
***
**Logo image inside the folder:**

![Logo image](./screen-shots/logo-image.png)

#### Running the Application
Execute `app.py` and you will be prompted to choose an option:

<img src="./screen-shots/select-option.png" alt="Processing" width="300"/>

#### Processing
The application will process your images according to your choices:

<img src="./screen-shots/processing.png" alt="Processing" width="400"/>

***
#### Watermarked Images
A folder named `/water_marked_images` will be created to store the watermarked images:

![Watermarked images folder](./screen-shots/folder-created.png)

**Sample watermarked images:**


With text only:
<img src="./screen-shots/image-text.png" alt="Processing" width="300"/>
***

With logo only:
<img src="./screen-shots/image-only-logo.png" alt="Processing" width="300"/>
***
With both logo and text:
<img src="./screen-shots/image-logo-text.png" alt="Processing" width="300"/>
