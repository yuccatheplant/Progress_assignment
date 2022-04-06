import sys

import configParser
import libChecker

if __name__ == "__main__":
    libraries = configParser.readAndParse()
    result = libChecker.checkLibraries(libraries)
    
    sys.exit(0)