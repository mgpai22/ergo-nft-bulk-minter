import serializer
import sha256
import node
import json
import fileOperations

# The main minting program
# Go through README.md

imageFolderPath = r""  # Change this
metadataPath = r""  # Change this
numOfImages = 50  # Change this
amountToMint = 2  # Change this
numOfLastNFTminted = 0  # this is important. Put the number of the last NFT minted. If this is the first time
# leave it as '0'


sha256.sha256(numOfImages, imageFolderPath)  # retrieves the sha256 hash of each image in the folder and stores it

x = numOfLastNFTminted - 1
fileOperations.clear('txid.json')  # clears this file
for i in range(amountToMint):  # for loop to mint the amount of times specified
    x = x + 1
    name = fileOperations.file(metadataPath)[x]["name"]  # gets the name from metadata
    description = json.dumps(fileOperations.file(metadataPath)[x], indent=4)  # gets the description from metadata
    hash = fileOperations.file('sha256.json')[x]["SHA 256 Hash"]  # gets the sha256 hash from 'sha256.json'
    encodedHash = serializer.hashSerializer(hash)  # encodes the hash so it can be put into registers
    link = fileOperations.file(metadataPath)[x]["image"]  # gets the link from metadata
    encodedLink = serializer.serializer(link)  # encodes the link so it can be put into registers
    fileOperations.write({"TX": node.mintNft(name, description, encodedHash, encodedLink), }, 'txid.json') # executes mint and writes the txid to 'txid.json'
    if i == amountToMint - 1: # this notifies what to change the variable to the on the next run
        print("Next time this program is run change 'numOfLastNFTminted' to " + str(numOfLastNFTminted + amountToMint))
