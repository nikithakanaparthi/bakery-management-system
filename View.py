import matplotlib.pyplot as plt

VIEW_MENU = [
    "Employee",
    "Make",
    "Sale Item",
    "Sales",
    "Supplier",
    "Product Request",
    "Bakery",
    "Purchase",
    "Sold To",
    "Customer",
    "Wants Delivery",
    "Delivery",
    "Requests",
    "Customer Requests"
]
    

class View:
    def __init__(self):
        print("Welcome to Bakery Management System")

    def printUsernameInput(self):
        print("Please enter the Username : ")
    
    def printPasswordInput(self):
        print("Please enter the Password : ")

    def printException(self, message):
        print(message)

    def printTable(self, table):
        print("The details are :  \n", table + "\n\n")

    def printLoggedInMessage(self):
        print("\nSuccessfully logged in \n" + "\n\n")

    def printFeaturesMenu(self):
        print("1.View Tables \n2.Edit Tables \n3.Additional Features\n\n")

    def printViewTableMenu(self):
        temp = ""
        for idx, item in enumerate(VIEW_MENU):
            temp = temp + str(idx+1) + ". " + "View " + str(item) + " Table \n\n"
        print(temp)

    def printTableDetails(self, table):
        # table = pd.DataFrame(table)
        print(table)
        print("\n\n")

    def printAdditionalFeaturesMENU(self):
        print("\n\n1. Group Items sold by Postal code - bar chart \n\n2. Generate Profit Loss Statement per product")

    def printSalesChartByLocation(self, values):
        y,x = values
        plt.bar(x,y)
        plt.xlabel("Pincode")
        plt.ylabel("Sales Count")
        plt.show()

    def printProfitLossStatement(self, values):
        x,y = values
        plt.barh(x,y)
        plt.ylabel("Product name")
        plt.xlabel("Profit")
        plt.show()
        
            
