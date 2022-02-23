import hashlib
import fileOperations


def hasher(z, imageFolderPath):  # hashes specified file and returns a json entry
    z = z + 1
    filepath = imageFolderPath + "\\" + str(z) + ".png"
    with open(filepath, "rb") as f:
        bytes = f.read()  # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest()
        return {"SHA 256 Hash": readable_hash, }


def sha256(numOfTimesToRun, imageFolderPath):
    fileOperations.clear("sha256.json")
    for z in range(numOfTimesToRun):
        fileOperations.write(hasher(z, imageFolderPath), "sha256.json")
