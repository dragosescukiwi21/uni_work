from a4classes import myVector

class Controller:
    def __init__(self, repo):
        self.repo = repo

    def createVector(self, id, color, type, values):
        obj = myVector(id, color, type, values)
        self.repo.add(obj)


    def readVector(self):
        id = int(input("Enter ID: "))
        color = int(input("Enter color: "))
        type = int(input("Enter type: "))

        listOfVals = []

        n = (int(input("Enter number of elements: ")))
        for i in range(n):
            val = input("Enter value: ")
            listOfVals.append(val)

        self.createVector(id, color, type, listOfVals)


    def updateVectorIndex(self, i, nid, ncl, nty, nvl):
        if i > len(self.repo.get_vectors()) or i < 0:
            raise IndexError("Index out of range")

        else:
            veclist = self.repo.get_vectors()
            veclist[i].setNameID(nid)
            veclist[i].setColor(ncl)
            veclist[i].setType(nty)
            veclist[i].setValues(nvl)


    def updateVectorID(self, id, nid, ncl, nty, nvl):
        veclist = self.repo.get_vectors()

        index = 0
        for vec in self.repo.get_vectors():
            if vec.getNameId() == id:
                veclist[index].setNameID(nid)
                veclist[index].setColor(ncl)
                veclist[index].setType(nty)
                veclist[index].setValues(nvl)

                break

            index += 1


    def deleteVectorIndex(self, i):
        if i > len(self.repo.get_vectors()) or i < 0:
            raise IndexError("Index out of range")

        else:
            veclist = self.repo.get_vectors()
            del veclist[i]


    def deleteVectorID(self, id):
        veclist = self.repo.get_vectors()

        index = 0
        for vec in self.repo.get_vectors():
            if vec.getNameId() == id:
                del veclist[index]
                break
            index += 1


    def printVectors(self):
        for vec in self.repo.get_vectors():
            print(vec)


    def printVectorIndex(self, i):
        if i > len(self.repo.get_vectors()) or i < 0:
            raise IndexError("Index out of range")

        else:
            veclist = self.repo.get_vectors()
            print(veclist[i])