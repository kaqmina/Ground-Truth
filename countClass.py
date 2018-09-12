import os

# List of classes
allClass = [ '__ignore__', '_background_', 'aeroplane', 'bicycle', 'bird', 'boat',
             'bottle', 'bus', 'car', 'cat', 'chair', 'cow', 'diningtable', 'dog',
             'horse', 'motorbike', 'person', 'potted plant', 'sheep', 'sofa', 'train',
             'tv/monitor']

def countTotal():
    global allClass
    ds = input('Directory path: ')
    directory = os.listdir(ds)
    classCount = 0
    # initialize to 0
    allCount = [0] * len(allClass)
    
    for file in directory:
        filename = os.fsdecode(file)
        if filename.endswith('.json'):
            checkFile = open(ds + "\\" + filename)
            lines = checkFile.read()
            print("Reading " + filename + "...")
            for cn in allClass:
                getOccurences = lines.count('"label": "'+ cn +'"')
                index = allClass.index(cn)
                currentCount = allCount[index]
                currentCount+=getOccurences
                allCount[index] = currentCount
        else:
            continue
    print("\n----- Classes -----")
    for x in allClass:
        getIndex = allClass.index(x)
        print('[' + str(getIndex) + '] ' + x + ': ' + str(allCount[getIndex]))
    print("------- END -------\n")
    exitNow = input("Press any key to exit...")

countTotal()
