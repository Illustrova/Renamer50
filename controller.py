from model import MainModel
from design import Ui_MainWindow
import re
import os

class MainController:
    def __init__(self, model: MainModel):
        self.model = model
        self.counter = {}

    def resetPattern(self):
        self.model.pattern = ""

    def addFile(self, fileData):
        self.model.files.update(fileData)
        self.model.announce_update()

    def deleteFile(self, filepath):
        del self.model.files[filepath]

    def updateFileName(self, path, newname):
        if path in self.model.files:
            self.model.files[path]["out"] = newname

    def resetCounter(self):
        self.counter = {}

    def updatePattern(self, pattern):
        self.model.pattern = pattern
        self.model.announce_update()

    def updateFilenames(self):
        for file in self.model.files:
            newName = []
            for index, block in enumerate(self.model.pattern):
                nameBlock = self.resolveBlock(file, block)
                if block["case"]:
                    nameBlock = self.toCase(nameBlock, block["case"])

                if block["separator"] and index != len(self.model.pattern) - 1:
                    nameBlock = self.addSeparator(nameBlock, block["separator"])

                newName.append(nameBlock)
            self.model.files[file]["out"] = "".join(newName)
        self.resetCounter()

    def resolveBlock(self, file, block):
        if block["value"] == "ParentDir":
            ''' Name of parent directory '''
            return os.path.basename(os.path.dirname(file))

        elif block["value"] == "OriginalName":
            ''' Original file name '''
            return os.path.splitext(os.path.basename(file))[0]

        elif block["value"].startswith("Word"):
            ''' Word at the given index in the currect filename '''
            separators = block["value"].split(":")[2]
            if len(separators) < 1:
                separators = " "
            wordsList = re.split("[" + re.escape(separators).replace("\ ", "\s").replace("|", "") + "]", self.model.files[file]["in"])
            wordIndex = int(block["value"].split(":")[1])

            if len(wordsList) <= (wordIndex - 1):
                return ""
            else:
                return wordsList[wordIndex-1]

        elif block["value"].startswith("Nr:"):
            ''' Number  value '''
            if block["value"].endswith("All"):
                ''' Number of files to be renamed '''
                return str(len(self.model.files))

            elif block["value"].endswith("Folder"):
                ''' Number of files in parent directory '''
                folder = os.path.dirname(file)
                return str(len([name for name in os.listdir(folder) if os.path.isfile(os.path.join(folder, name))]))

            else:
                ''' Counter '''
                indexStr = block["value"].split(":")[1]
                index = int(indexStr)
                # get number of leading zeroes
                if index == 0:
                    a = re.search('(?!0)', indexStr)
                    zeroes = a.start()
                else:
                    a = re.search('(?!0)', indexStr)
                    zeroes = a.start() + 1

                if not block["value"] in self.counter:  # Check if counter already exists
                    self.counter[block["value"]] = index

                currIndex = self.counter[block["value"]]
                self.counter[block["value"]] += 1
                return str(currIndex).zfill(zeroes)

        else:
            ''' Value contains exact text which has to be used '''
            return block["value"]


    def toCase(self, string, case):
        if case == "L":
            return string.lower()
        elif case == "U":
            return string.upper()
        elif case == "R":
            return ''.join(c.lower() if c.isupper() else c.upper() for c in string)
        else:
            return string

    def addSeparator(self, string, separator):
        return string + separator
