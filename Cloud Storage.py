import os
import shutil

folder = "CloudStorage"
os.makedirs(folder, exist_ok=True)

def upload_file():
    path = input("Enter file path: ")
    if os.path.isfile(path):
        shutil.copy(path, folder)
        print("File uploaded successfully!")
    else:
        print("File not found!")

def view_files():
    files = os.listdir(folder)
    if files:
        print("Files in Cloud Storage:")
        for name in files:
            print(name)
    else:
        print("Storage is empty!")

def download_file():
    name = input("Enter file name: ")
    source = os.path.join(folder, name)

    if os.path.isfile(source):
        destination = os.path.join(
            os.path.expanduser("~"), name
        )
        shutil.copy(source, destination)
        print("File downloaded successfully!")
    else:
        print("File not found!")

while True:
    print("\n--- Cloud Storage System ---")
    print("1. Upload File")
    print("2. View Files")
    print("3. Download File")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        upload_file()
    elif choice == "2":
        view_files()
    elif choice == "3":
        download_file()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")