
# Python Bulk Ergo NFT minter

This program will allow users to easily mint NFTs  on the Ergo Blockchain in bulk!\
This uses Ergo Node API methods.


## Prerequisites 

 - Have python installed on system
 - Have pip installed on system
 - Have an IDE to work with
    - [Pycharm](https://www.jetbrains.com/pycharm/download/#section=windows) is recommended
    - Community edition works fine
 - Have an [ergo node](https://ergoplatform.org/en/blog/2019_12_02_how_to_setup/) running with access to its wallet
    - This is where you send and receive transaction from 
 - Have links to images
 - Have a metadata file
 

## Minting Program Setup

 * Either download zip or git clone
 * Open extracted file in IDE
 * Navigate to the `.env` file and add your node configurations 
    * For example
      ```
      NODE_IP=localhost:9053
      API_KEY=hello
      PW=b$*ab242qm*dzci!
      WALLET_ADDRESS=9fijDm4Y8AmQD8aw36YbWKYkaF23JQ5HwfvowABCj8cJdt4FVGc
      NODE_IP_BURN=localhost:9053
      API_KEY_BURN=hello
      PW_BURN=b$*ab242qm*dzci!
      WALLET_ADDRESS_BURN=9fijDm4Y8AmQD8aw36YbWKYkaF23JQ5HwfvowABCj8cJdt4FVGc
      ```
* Navigate to `main.py` and fill in the following:
  * `imageFolderPath`
    * This specifies the location of where the folder for images are 
    * This is required to calculate the hash
  * `metadataPath`
    * This specifies the location of the metadata file
    * This is required to get the name, link, and description of the NFT
  * `numOfImages`
    * This specifies the total amount of NFT images there are in your image folder
    * This is required to calculate the hash
  * `amountToMint`
    * This specifies the amount of NFTs that will be minted
    * NFTs can be minted all at once or a couple at a time due to this 
  * `numOfLastNFTminted`
    * This specifies the last NFT **minted**
    * This is especially important if NFTs are minted in short intervals 
    * For example if you have ten NFTs to mint and six are already minted then this would be set to six
    * The program will also tell what to set this variable to once minting is complete
    * This is important as it lets the program keep track of which NFTs are already minted
  * For example
    ```
    imageFolderPath = r"C:\Users\ergonaut\NFT\test-nfts\build\images"
    metadataPath = r"C:\Users\ergonaut\NFT\test-nfts\build\json\metadata.json"
    numOfImages = 50
    amountToMint = 2
    numOfLastNFTminted = 0
    ```
* Run `pip install -r requirements.txt`
* Run `python main.py`
  * Transaction IDs are saved in `txid.json`
  * Each time the program is run this will get overwritten

## Token Burner Program Setup 

There is a token buring program included. This will **permanently** destroy tokens. Use with **caution**!\
NFTs and tokens are the same thing.

* Configure the `.env` as shown in the prior steps
* Run `pip install -r requirements.txt` (if you haven't already)
* Run `python token_extracter.py`
    * This gets ALL the tokens from the node wallet
* Clear entires from `tokenid.json` as necessary 
* Run `python burn.py`
  * The first program to execute will get **ALL** tokens from your node wallet
  * Any token **included** in `tokenid.json` will be burned
  * Transaction IDs will be stored in `burntxs.json` this gets overwritten each time the program is run
* Run `python  clearTokenID.py`
    * This clears everything from `tokenid.json` to start fresh


## How to upload images to IPFS

It is important that image links are ready before minting with this program. Images can be stored on a server but the best practice is to store it on a decentralized platform such as IPFS.

Images can be uploaded to IPFS by running you own node and supporting its network. Another method is by using a \
pining service such as [pinata.cloud](https://www.pinata.cloud/). The latter will be demonstrated.

- Make an account with pinata
- Upload the entire folder containing only images of the NFTs
- The naming convention for these images is important
- Make sure they are sequential
    - The first image would be `1.png` then `2.png` and so on
- After upload pinata will give a hash (CID) of the folder
    - For example this is the CID of a folder with images `QmZcHTFTpRS1NezMVQxvxagxQygvWPegj284cmA89nPxEQ`
    - This link uses a gateway which allows browsers without IPFS  support to visit it `https://gateway.pinata.cloud/ipfs/QmZcHTFTpRS1NezMVQxvxagxQygvWPegj284cmA89nPxEQ`
    - To visit the first image the link would be `https://gateway.pinata.cloud/ipfs/QmZcHTFTpRS1NezMVQxvxagxQygvWPegj284cmA89nPxEQ/1.png`
    - The second image would be `https://gateway.pinata.cloud/ipfs/QmZcHTFTpRS1NezMVQxvxagxQygvWPegj284cmA89nPxEQ/2.png` and so on
    - Notice how the CID always stays the same
    - The link that should be used for the metadata is `ipfs://QmZcHTFTpRS1NezMVQxvxagxQygvWPegj284cmA89nPxEQ`
        - Notice the gateway is not there
    - Although this CID works fine it is not the most recent standard. This step is completely optional but it is always recommended to use the most recent version
        - The `Qm` CID is the older version
        - The `bafy` CID is the recent version
        - To convert `Qm` to `bafy` go to [cid.ipfs.io](https://cid.ipfs.io/)
        - Then paste the `Qm` hash in the input box
        - Below the newer `bafy` CID will be available 
        - For example the CID `QmZcHTFTpRS1NezMVQxvxagxQygvWPegj284cmA89nPxEQ` would be converted to `bafybeifhohije2niwm6awfmhpgthp4ytn3saot4dclzvkgr7ixi2mjtgiu`
        - Use the `bafy` CID from now on. The image metadata would be `ipfs://bafybeifhohije2niwm6awfmhpgthp4ytn3saot4dclzvkgr7ixi2mjtgiu`

        


## Metadata File

The metadata file is import as it contains all the information that the program will pull from. Below is an example of \
what the file should look like.

```
[
  {
    "name": "Test NFT #1",
    "description": "Test NFT please ignore me",
    "image": "ipfs://bafybeifhohije2niwm6awfmhpgthp4ytn3saot4dclzvkgr7ixi2mjtgiu/1.png",
    "dna": "fd00cb316d22e89557b63a4ce3101d6ae29e191a",
    "edition": 1,
    "attributes": [
      " Background Black",
      " Eyeball Red",
      " Eye Color Cyan",
      " Iris Small",
      " Shiny Yes",
      " Lid Middle",
      " Top Lid High"
    ]
  },
  {
    "name": "Test NFT #2",
    "description": "Test NFT please ignore me",
    "image": "ipfs://bafybeifhohije2niwm6awfmhpgthp4ytn3saot4dclzvkgr7ixi2mjtgiu/2.png",
    "dna": "375b19882207577b50d17a6a9eafcab276abf181",
    "edition": 2,
    "attributes": [
      " Background Black",
      " Eyeball White",
      " Eye Color Yellow",
      " Iris Large",
      " Shiny Yes",
      " Lid High",
      " Top Lid High"
    ]
  },
  {
    "name": "Test NFT #3",
    "description": "Test NFT please ignore me",
    "image": "ipfs://bafybeifhohije2niwm6awfmhpgthp4ytn3saot4dclzvkgr7ixi2mjtgiu/3.png",
    "dna": "16cfe12b7f7de2a0f17ac61a00725354d32b53aa",
    "edition": 3,
    "attributes": [
      " Background Black",
      " Eyeball White",
      " Eye Color Green",
      " Iris Small",
      " Shiny Yes",
      " Lid Low",
      " Top Lid Middle"
    ]
  },
  {
    "name": "Test NFT #4",
    "description": "Test NFT please ignore me",
    "image": "ipfs://bafybeifhohije2niwm6awfmhpgthp4ytn3saot4dclzvkgr7ixi2mjtgiu/4.png",
    "dna": "817731a672218f9f500ca7454776da55746224de",
    "edition": 4,
    "attributes": [
      " Background Black",
      " Eyeball Red",
      " Eye Color Green",
      " Iris Small",
      " Shiny Yes",
      " Lid Low",
      " Top Lid Middle"
    ]
  },
  {
    "name": "Test NFT #5",
    "description": "Test NFT please ignore me",
    "image": "ipfs://bafybeifhohije2niwm6awfmhpgthp4ytn3saot4dclzvkgr7ixi2mjtgiu/5.png",
    "dna": "b0e64e427776f8f5b0abc641b8d1053ceaf4429a",
    "edition": 5,
    "attributes": [
      " Background Black",
      " Eyeball White",
      " Eye Color Yellow",
      " Iris Small",
      " Shiny Yes",
      " Lid Low",
      " Top Lid Low"
    ]
  }
]
```

- The `name`, `description`, and `image` entries are required
- Pay careful attension to brackets and commas 



## Future updates

- Intergration with appkit so a node won't be required. Although the program may need to use another programming language
- Perhaps a method of calculating the sha256 hash without having the image folder locally 

