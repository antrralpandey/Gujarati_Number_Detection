import os

if not os.path.exists("gujarati-handwritten-digit-dataset"):
    print("Downloading dataset...")
    os.system("git clone https://github.com/Parth-Goel/gujarati-handwritten-digit-dataset.git")
    print("Dataset downloaded successfully ✅")
else:
    print("Dataset already exists ✅")
  
