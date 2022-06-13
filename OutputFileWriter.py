import HuffmanCodeBuilder
import Converter
import Filereader


def writeDictionary(fileIn, fileOut):

    with open(fileOut, "w") as fout:
        srcText = Filereader.reader(fileIn)
        dictionary = HuffmanCodeBuilder.returnPath(
            HuffmanCodeBuilder.returnNodes(srcText))

        dictElement = ''
        dictFull = ''
        x = 0
        while x < len(dictionary):
            char = dictionary[x][0]
            freq = dictionary[x][1]
            dictElement = char + ": " + freq + "\n"
            dictFull = dictFull + dictElement
            x = x + 1
        fout.write(dictFull)
        fout.close()

    return dictionary


def writeResult(fileIn, fileOut):

    dictionary = writeDictionary(fileIn, fileOut)

    srcText = Filereader.reader(fileIn)
    converted = Converter.compressText(srcText, dictionary)

    newConverted = ''

    i = 0
    lenConverted = len(converted)
    with open(fileOut, "a") as fout:
        fout.write(str('\n'))
        while i < lenConverted:
            newConverted = newConverted + converted[i]
            i = i + 1
        fout.write(str(newConverted))
        fout.close()
