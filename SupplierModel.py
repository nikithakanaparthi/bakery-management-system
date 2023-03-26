import pandas as pd
from AbstractModel import Abstract

accessDictionary = {
        "Employee" : [False,False],
        "Make" : [False,False],
        "Sale Item" : [False,False],
        "Sales" : [False,False],
        "Supplier" : [False,False],
        "Product Request" : [True,False],
        "Bakery" : [False,False],
        "Purchase" : [False,False],
        "Sold To" : [False,False],
        "Customer" : [False,False],
        "Wants Delivery" : [False,False],
        "Delivery" : [False,False],
        "Requests" : [False,False],
        "Customer Requests" : [False,False]
    }

class Supplier(Abstract):
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
    employee = Supplier()
    print("access",employee.getAccessDetails())
    print("table",employee.getTableDetails("Raw Material"))
    print("table",employee.getTableDetails("Supplier"))


