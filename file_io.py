# Reading file
sample_text = open('sample_text.txt')
# print(sample_text.readline()) # only read first line
print(sample_text.read()) # read all context

sample_text.close() # closing file

# Read, Write, Append
# r - read, w - write, a - append
with open('./sampleImport/sample_io_path.txt', mode='a') as sample_path:
    inputSamples = sample_path.write('Sample Text')
    # print(sample_path.read())