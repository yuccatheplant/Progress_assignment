import pkg_resources
  
def checkLibraries(libArray):
    result = 0
    for lib in libArray:
        checkVersion = True
        try:
            pkg_resources.get_distribution(lib[0])
        except Exception as err:
            print(lib[0]+" library is not installed!")
            result = result + 1
            checkVersion = False
        
        if checkVersion and lib[1] != "":
            currentVersion = pkg_resources.get_distribution(lib[0]).version
            if currentVersion != lib[1]:
                print(lib[0]+" library version missmatch! Installed: "+currentVersion+", required: "+lib[1])
                result = result + 1
    return result