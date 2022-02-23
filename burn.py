import fileOperations
import nodeBurn


fileOperations.clear('burntxs.json') # clears the `burntxs.json` file
print("Warning make sure you deleted any token from 'tokenid.json' that you want saved!!")
print("Type 'yes' to agree you realize that ALL tokens will be burned that is specified in 'tokenid.json'! This is permanent!")
agreement = input()
if agreement.lower() == 'yes':
    for x in range(fileOperations.length(fileOperations.file('tokenid.json'))): # goes through each tokenid in the file
        tokenId = fileOperations.file('tokenid.json')[x]['TokenId'] # selects token id from file
        amount = 1 # burns one token at a time
        fileOperations.write({"TX": nodeBurn.burnNft(tokenId, amount), }, 'burntxs.json') # executes burn and writes to the file
else:
    print('Please agree to continue!')
    quit()
print('Burn Complete')






