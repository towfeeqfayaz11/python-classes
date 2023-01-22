# from folderA.fileA import funcA
# from folderA import fileA
# import folderA

from folderB import infolderB

print("in side main func: ", __name__)
if __name__ == "__main__":
    # funcA()
    # fileA.funcA()
    # folderA.fileA.funcA()

   infolderB.infileB.infuncB()