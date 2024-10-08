# 📸 Image Filter by Face Recognition

Welcome to the **Image Filter by Face Recognition** project! This tool is designed to help you automatically filter out images of a specific person from a large directory of images. If you have a directory full of photos—like your wedding pictures—and you want to find all the images that feature a person named Charles, you're in the right place!

## 🚀 Features

- **Automatic Image Filtering**: Place a single image of the person you want to filter in a reference folder, and the tool will automatically find all images containing that person.
- **High Definition Support**: Optimized for high-definition images by first detecting faces and then applying face landmark detection.
- **Face Recognition Technology**: Uses state-of-the-art face recognition and face detection techniques to ensure accurate results.

## 🛠️ Technologies Used

- **face_recognition**: For recognizing and comparing faces.
- **OpenCV**: For face detection and image processing.

## 📝 How It Works

1. **Reference Image**: Place one image of the person you want to filter in the `reference_image/` folder.
2. **Image Directory**: Place all your images (e.g., wedding photos) in the `images/`.
3. **Run the Script**: The code will scan through all the images in the `images/`, detect faces, extract face landmarks, and compare them to the reference image.
4. **Result**: All matching images will be saved in the `matched/` for easy access.

## 🖥️ Setup & Installation

1. **Clone the repository**:
    ```bash
    https://github.com/AbdulHaseeb007/image_filteration_face_landmarks.git
    ```
   
2. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Add your images**:
    - Place the reference image(s) in the `reference_image/` folder.
    - Place the images to scan in the `images/` folder.

4. **Run the code**:
    ```bash
    python filter_images.py
    ```

## 🏗️ Project Structure

```plaintext
face-recognition-filter/
├── reference_images/    # Folder containing reference image(s) of the person
├── images/     # Folder containing images to be scanned
├── matched/     # Folder where matched images will be saved
├── main.py     # Main script to run the image filtering
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## 📂 Example

Let's say you want to filter out images of Charles from your wedding album:

- **Step 1**: Place one clear image of Charles in the `reference_image/` folder.
- **Step 2**: Place all your wedding images in the `images/`.
- **Step 3**: Run the script and find all images containing Charles in the `matched/`.

## 🌟 Why This Approach?

Initially, the challenge was dealing with high-definition images where getting face landmarks directly was computationally expensive and less reliable. To overcome this:

- **Step 1**: Detect faces in each image.
- **Step 2**: Extract face landmarks from each detected face.
- **Step 3**: Compare the landmarks with the reference image.

This approach ensures accurate detection and efficient processing, even with high-resolution images.

## 🙌 Note
This code is still in initial stage might skip some images 
Feel free to add your features 
Happy coding 

Contributions are welcome! If you have ideas for improving this project, feel free to fork the repository and submit a pull request.

## 🧑‍💻 Author

- **AbdulHaseeb007** - [GitHub Profile](https://github.com/AbdulHaseeb007)

