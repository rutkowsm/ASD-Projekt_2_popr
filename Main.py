import HuffmanCodeBuilder
import Converter
import Filereader
import OutputFileWriter

fSrcName = "./src_out/Jabberwocky.txt"
fOutName = "./src_out/CompressedJaberwocky.txt"

srcText = Filereader.reader(fSrcName)

OutputFileWriter.writeResult(fSrcName, fOutName)
