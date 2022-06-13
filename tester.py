import Filereader
import HuffmanCodeBuilder
import Sorter

fSrcName = "./src_out/Jabberwocky.txt"

srcText = Filereader.reader(fSrcName)

print(Sorter.sortFreqArray(srcText))

print(HuffmanCodeBuilder.returnNodes(srcText).char +
      str(HuffmanCodeBuilder.returnNodes(srcText).freq))

print(HuffmanCodeBuilder.returnNodes(srcText).left.char +
      str(HuffmanCodeBuilder.returnNodes(srcText).left.freq))
print(HuffmanCodeBuilder.returnNodes(srcText).right.char +
      str(HuffmanCodeBuilder.returnNodes(srcText).right.freq))

print(HuffmanCodeBuilder.returnNodes(srcText).right.left.left.travers)

dictionary = HuffmanCodeBuilder.returnPath(
    HuffmanCodeBuilder.returnNodes(srcText))

x = 0
while x < len(dictionary):
  char = dictionary[x][0]
  print(char)
  x = x + 1
