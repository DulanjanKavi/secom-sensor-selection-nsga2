# download the dataset

import io
import pathlib
import urllib.request
import zipfile

URL = "https://archive.ics.uci.edu/static/public/179/secom.zip"
DATA_DIR = pathlib.Path("data")

def main():
    DATA_DIR.mkdir(exist_ok=True) # Crerate new Folder if there is no data directory
    if (DATA_DIR / "secom.data").exists() and (DATA_DIR / "secom_labels.data").exists():#check if priviosly download the data
        print("SECOM already downloaded.")
        return
    print("Downloading SECOM...")
    with urllib.request.urlopen(URL) as response:
        archive = zipfile.ZipFile(io.BytesIO(response.read()))
    archive.extractall(DATA_DIR)
    print("Files saved:", archive.namelist())

if __name__=="__main__":
    main()
