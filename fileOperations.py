import json


# this module includes operations to write to files, open files, return the length of files, and clear files

def write(new_data, filename):  # function that appends data to the specified file
    with open(filename, "r") as file1:
        data = json.load(file1)
        data.append(new_data)
    with open(filename, "w") as file1:
        # Sets file's current position at offset.
        file1.seek(0)
        json.dump(data, file1, indent=4)


def clear(file):  # function to clear the file so appended data isn't constantly repeated
    dict1 = []  # After everything is cleared this is what will be put back into the fresh  file
    out_file = open(file, "w")

    json.dump(dict1, out_file, indent=6)

    out_file.close()


def file(x):  # Function to load specified file
    with open(x, 'r+') as file:
        return json.load(file)


def length(data): # returns the length of provided file
    # data = data_file()
    return len(data)
