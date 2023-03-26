import pandas as pd
from AbstractModel import Abstract

accessDictionary = {
        "Employee" : [True,False],
        "Make" : [True,False],
        "Sale Item" : [True,False],
        "Sales" : [True,False],
        "Supplier" : [True,False],
        "Product Request" : [True,True],
        "Bakery" : [True,True],
        "Purchase" : [True,False],
        "Sold To" : [True,False],
        "Customer" : [True,False],
        "Wants Delivery" : [True,False],
        "Delivery" : [True,False],
        "Requests" : [True,False],
        "Customer Requests" : [True,False]
    }

class Supervisor(Abstract):
    def __init__(self, cursor, empID, heirarchy):
        super().__init__()
        self.accessDictionary = accessDictionary
        self.empID = empID
        self.cursor = cursor
        self.heirarchy = heirarchy


    def getAccessDetails(self):
        return super().getAccessDetails()

    def getTableDetails(self, tableName):
        return super().getTableDetails(tableName)

if __name__ == "__main__":
    print("here")
    supervisor = Supervisor()
    print("access",supervisor.getAccessDetails())
    print("table",supervisor.getTableDetails("Manufacturer"))




