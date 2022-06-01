# Img-Pdf Converter
Just a very simple Tkinter app that allows user to convert images to pdf, and vice versa.
The motivation of this project is that I don't feel safe to do these conversions online.

## Usage
1. Simply double click the executable in the dist folder
2. There are only 2 steps:
    1. Select the target images/pdf file
    2. Select the directory that you want to save the file

## Converting the python file into executable / Updating the executable
1. Install pyinstaller on your machine, and then run:
    ```
    pyinstaller --onefile img-pdf-converter.py
    ```
2. ALTERNATIVELY, do it on docker container
    ```
    ./buildDockerImage.sh
    ./runDockerFile.sh
    pyinstaller --onefile img-pdf-converter.py
    ```

## TO-DO
1. Add pdf to image converter function

## Disclaimer
1. The test images are obtained online, I don't own them.