import os

FILENAME = "config.txt"

def readAndParse():
    assert os.path.exists(FILENAME) == True, f"Filename {FILENAME} does not exist."
    file = open(FILENAME, "r")
    
    configString = file.read()
    file.close()
    
    configArray = configString.split('"')
    libArray =[]
    for configPiece in configArray:
        if not (',' in configPiece) and not ('[' in configPiece) and not (']' in configPiece):
            libArray.append(configPiece)
    
    result = []
    
    for lib in libArray:
        lib = lib.replace('-', '.')
        lib = lib.split('_')
        
        isVersion = False
        isFirstPart = True
        libName = ""
        libVersion = ""
        for part in lib:
            if isVersion:
                libVersion = libVersion + '.' + part
            else:
                if part.isnumeric():
                    isVersion=True
                    libVersion = libVersion + part
                else:
                    if not isFirstPart:
                        libName = libName + '_'
                    isFirstPart = False
                    libName = libName + part
        
        if libName != "":
            result.append([libName, libVersion])
    
    return result