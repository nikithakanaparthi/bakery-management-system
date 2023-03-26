import pandas as pd
from abc import ABC, abstractmethod

accessDictionary = {
        "Employee" : [False,False],
        "Make" : [False,False],
        "Sale Item" : [False,False],
        "Sales" : [False,False],
        "Supplier" : [False,False],
        "Product Request" : [False,False],
        "Bakery" : [False,False],
        "Purchase" : [False,False],
        "Sold To" : [False,False],
        "Customer" : [False,False],
        "Wants Delivery" : [False,False],
        "Delivery" : [False,False],
        "Requests" : [False,False],
        "Customer Requests" : [False,False]
    }

class Abstract(ABC):
    def __init__(self):
        self.accessDictionary = accessDictionary
        self.empID = None
        self.cursor = None

    @abstractmethod
    def getAccessDetails(self):
        access=self.accessDictionary
        print("I am here")
        return access

    @abstractmethod
    def getTableDetails(self, tableName):
        try:
            if self.accessDictionary[tableName][0] == True:
                employeeTable = self.getTable(tableName)
                return employeeTable
            raise Exception("Access Denied")
        except Exception as e:
            print(e)

    def getTable(self,tableName):
        table = {"dummyKey" : "dummyValue"}
        return table





