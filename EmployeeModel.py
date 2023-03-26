import pandas as pd
from AbstractModel import Abstract

accessDictionary = {
        "Employee" : [False,False],
        "Make" : [True,False],
        "Sale Item" : [True,True],
        "Sales" : [True,True],
        "Supplier" : [False,False],
        "Product Request" : [True,True],
        "Bakery" : [True,False],
        "Purchase" : [True,False],
        "Sold To" : [True,False],
        "Customer" : [False,False],
        "Wants Delivery" : [True,False],
        "Delivery" : [True,False],
        "Requests" : [True,False],
        "Customer Requests" : [True,False]
    }

class Employee(Abstract):
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
    employee = Employee()
    print("access",employee.getAccessDetails())
    print("table",employee.getTableDetails("Employee"))

