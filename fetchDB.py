import json


def getData(src):
    with open(src) as f:
        data = json.load(f)
    return data

def getIndex(src):
    index = 0
    with open(src) as f:
        data = json.load(f)
        for _ in data['all']:
            index += 1
    return index


class ReviewData():
    # a class for review data

    def __init__(self, header, content):
        self.headerText = header
        self.contentText = content

    def printFull(self):
        print(self.headerText, '\n' + self.contentText)



def fetchAllData():
    data = getData('data.json')
    amountOfInputs = getIndex('data.json')
    reviews = []


    for index in range(amountOfInputs):
        rev = ReviewData(data['all'][index]['header'], data['all'][index]['content'])
        reviews.append(rev)


    return reviews