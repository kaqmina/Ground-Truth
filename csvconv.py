# CSV Format
import csv
import os
import decimal

allClass = [ 'background', 'aeroplane', 'bicycle', 'bird', 'boat',
             'bottle', 'bus', 'car', 'cat', 'chair', 'cow', 'diningtable', 'dog',
             'horse', 'motorbike', 'person', 'potted plant', 'sheep', 'sofa', 'train',
             'tv/monitor']

colorKeywords = ['Red', 'Yellow', 'Green', 'Cyan', 'Blue', 'Magenta']
columns = []
columns.append('filename')
columns.extend(allClass)

# Extend color to columns.
for color in colorKeywords:
    columns.append(color)
    columns.append('n_' + color.lower())

row = []

def generate():
    global allClass
    global row
    ds = input('Directory path: ')
    directory = os.listdir(ds)
    i = 0

    for file in directory:
        filename = os.fsdecode(file)
        currentRow = [0] * len(columns)

        # For limiting rows.
        i+=1
        if i > 1000:
            break
        
        # Check if it is a log file.
        if filename.endswith('.log'):
            fn = filename[:-4]
            currentRow[0] = fn
            checkFile = open(ds + '\\' + filename)
            lines = checkFile.readlines()
            
            # Iterate allClass.
            for line in lines:
                # In label list.
                if any(classes in line for classes in allClass):
                    currentLine = line.split()
                    cl = currentLine[2]
                    currentLabel = cl[:-1]
                    currentValue = currentLine[3]
                    index = columns.index(currentLabel)
                    currentRow[index] = currentValue
                # In color family list.
                elif any(cfamily in line for cfamily in colorKeywords):
                    currentLine = line.split()
                    cf = currentLine[0]
                    currentFamily = cf[:-1]
                    currentPercentage = currentLine[1]
                    numberOfInstances = currentLine[3]
                    index = columns.index(currentFamily)
                    currentRow[index] = currentPercentage
                    index = columns.index('n_' + currentFamily.lower())
                    currentRow[index] = numberOfInstances
                # Not matching any keywords.
                else:
                    continue
            row.append(currentRow)
        else:
            continue        
    createFile()

def getEmotionLabel(filename):
    # Code here for getting the annotated emotion and append it to row.
    print('Not yet implemented.')

def createFile():
    filename = input('Enter new name: ')
    # Change to desired output directory.
    mainDirectory = r'C:\\Users\\K Ann\\Documents\\GitHub\\Ground-Truth\\'

    # Create file.
    with open(mainDirectory+filename+'.csv', 'w', newline='') as file:
        wr = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        wr.writerow(columns)

        for rows in row:
            wr.writerow(rows)
        print('File created!')

# Main Process
generate()