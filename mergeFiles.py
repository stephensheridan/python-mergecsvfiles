# Import the os module
import os
import csv

def processSample(filePath):
    # Use a list to store op code counts for sample
    values = []
    print('Processing %s' % filePath)
    with open(filePath) as fp:
        for line in fp:
            count = (line.strip().split(',')[1]).strip()
            values.append(count)
    # Return the list with op code counts
    return values

def mergeFile(filePath):
    # Column headers in same order as sample files
    columns = ['add','and','call','cmp','eax','ecx','jmp','lea','mov','mul','or','push','pop','test','xor']
    # Open the master file for writing
    masterFile = open('./master.csv', 'a')
    # Create a csv writer
    write = csv.writer(masterFile)
    # Output the column headings - optional!
    write.writerow(columns)
    # Traverse the sample files as process
    for dirName, subdirList, fileList in os.walk(filePath):
        for fname in fileList:
            # Get the list of op code counts from each sample file
            counts = processSample(filePath + '/' + fname)
            # Write the op code counts as a row in the master file
            write.writerow(counts)
    # Close the master file
    masterFile.close()        


if __name__ == '__main__':
    # Pass over the folder with the sample files
    mergeFile("./data")