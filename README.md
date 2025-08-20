# DICOM-to-PDF
Created a simple python script to convert all DICOM Medical Scanned Images to PDF and merge them into a single PDF document.

## Requirements
1. Python

2. DICOM images i.e., images with a ".dcm" extension

3. Windows OS (I have not tested on other systems yet. But the codes should be fairly similar) 

## Installation
Before you get started, you will need to have python installed as this script uses certain libraries. 

Install the following libraries and their dependencies if they pop up (using the `pip` command): 
1. [pydicom](https://pydicom.github.io/pydicom/stable/tutorials/installation.html)
```python
pip install pydicom
```

2. [Pillow](https://pypi.org/project/pillow/)
```python
pip install Pillow
```

3. [PyPDF2](https://pypi.org/project/PyPDF2/)
```python
pip install PyPDF2
```

## Running the script
There are two ways you can go about it. 

1. Clone the repo, place all your dicom images inside the dicom-images folder and run the [conversion-script.py](https://github.com/Aaptha0204/DICOM-to-PDF/blob/main/conversion-script.py) file.

2. Download the python script, place it outside the folder containing your dicom images and run it. 

### Hope this helps! And get well soon if you needed a scan because you are sick!!
