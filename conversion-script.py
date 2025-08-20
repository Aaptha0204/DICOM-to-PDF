import pydicom
import os, sys, shutil
from PIL import Image
from PyPDF2 import PdfMerger

# keep this file in the same directory as the folder containing images
imgFolderPath = "dicom-images"

# pdf merger
merger = PdfMerger()
if not os.path.exists("PDF"):
    os.makedirs("PDF")

print("\nConverting DICOM files to PDF.\n")
for img in os.listdir(imgFolderPath):
    if img.endswith(".dcm"):
        imgPath = os.path.join(imgFolderPath, img)
        ds = pydicom.dcmread(imgPath)

        pdfImgPath = "PDF/" + img.split(".")[0] + ".pdf"
        Image.fromarray(ds.pixel_array).convert("RGB").save(pdfImgPath)
        merger.append(pdfImgPath)
    else: 
        continue

# combining all PDF
# check if merger is empty
if merger.pages:
    print("Merging all PDF files to a single PDF file.\n")
    merger.write("merged-scans.pdf")
    merger.close()
else:
    print("No PDF files to merge.\nCheck your dicom-images folder if it contains valid DICOM files. Exiting...\n")
    shutil.rmtree("PDF")
    exit(1)

# deleting single PDF files (optional. Comment if you want all scans as separate PDFs)
print("Deleting separate PDF files.\n")
try:
    shutil.rmtree("PDF")
except OSError as e:
    print("Error: %s - %s." % (e.filename, e.strerror))
    print("Failed to delete separate PDF files. Exiting...\n")
    exit(1)

print("Operation Complete.\n")