from ModelDelegator import ModelDelegator
from View import View
from ModelDelegator import ModelDelegator

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

class ControllerLoop:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.LOGIN_MENU = True
        self.VIEW_TABLE_MENU = False
        self.EDIT_TABLE_MENU = False
        self.FEATURES_MENU = False
        self.ADDITIONAL_FEATURES_MENU = False

    def getUserLoginCredentials(self):
        self.view.printUsernameInput()
        username = str(input())
        self.view.printPasswordInput()
        password = str(input())
        return username, password

    def mainLoop(self):
        while(self.LOGIN_MENU):
            try:
                username, password= self.getUserLoginCredentials()
                print(username,password)
                if self.model.verifyUser(username, password):
                    self.FEATURES_MENU = True
                    self.view.printLoggedInMessage()
                    self.feaaturesMenuLoop()
                raise Exception("Please Enter valid credentials")
            except Exception as e:
                self.view.printException(e)

    def feaaturesMenuLoop(self):
        while(self.FEATURES_MENU):
            try:
                self.view.printFeaturesMenu()
                match str(input()):
                    case '1':
                        self.VIEW_TABLE_MENU = True
                        self.viewTableMenuLoop()
                    case '2':
                        break
                    case '3':
                        self.ADDITIONAL_FEATURES_MENU = True
                        self.additionalFeaturesMenuLoop()
                    case 'back':
                        self.FEATURES_MENU = False
                    case _:
                        raise Exception("Please enter valid input")
            except Exception as e:
                self.view.printException(e)

    def viewTableMenuLoop(self):
        while(self.VIEW_TABLE_MENU):
            try:
                self.view.printViewTableMenu()
                match str(input()):
                    case "1":
                        self.view.printTableDetails(self.model.getTableValue(VIEW_MENU[0]))
                    case "2":
                        self.view.printTableDetails(self.model.getTableValue(VIEW_MENU[1]))
                    case "3":
                        self.view.printTableDetails(self.model.getTableValue(VIEW_MENU[2]))
                    case "4":
                        self.view.printTableDetails(self.model.getTableValue(VIEW_MENU[3]))
                    case "5":
                        self.view.printTableDetails(self.model.getTableValue(VIEW_MENU[4]))
                    case "6":
                        self.view.printTableDetails(self.model.getTableValue(VIEW_MENU[5]))
                    case "7":
                        self.view.printTableDetails(self.model.getTableValue(VIEW_MENU[6]))
                    case "8":
                        self.view.printTableDetails(self.model.getTableValue(VIEW_MENU[7]))
                    case "9":
                        self.view.printTableDetails(self.model.getTableValue(VIEW_MENU[9]))
                    case "10":
                        self.view.printTableDetails(self.model.getTableValue(VIEW_MENU[10]))
                    case "11":
                        self.view.printTableDetails(self.model.getTableValue(VIEW_MENU[11]))
                    case "12":
                        self.view.printTableDetails(self.model.getTableValue(VIEW_MENU[12]))
                    case "13":
                        self.view.printTableDetails(self.model.getTableValue(VIEW_MENU[13]))
                    case "14":
                        self.view.printTableDetails(self.model.getTableValue(VIEW_MENU[14]))
                    case 'back':
                        self.VIEW_TABLE_MENU = False
                    case _:
                        raise Exception("Please enter valid input")
            except Exception as e:
                self.view.printException(e)

    def additionalFeaturesMenuLoop(self):
        while(self.ADDITIONAL_FEATURES_MENU):
            try:
                self.view.printAdditionalFeaturesMENU()
                match str(input()):
                    case "1":
                        self.view.printSalesChartByLocation(self.model.querySalesGroupedByLocation())
                    case "2":
                        self.view.printProfitLossStatement(self.model.queryProfitLossStatement())
                    case 'back':
                        self.ADDITIONAL_FEATURES_MENU = False
                    case _:
                        raise Exception("Please enter valid input")
            except Exception as e:
                self.view.printException(e)


if __name__ == "__main__":
    model = ModelDelegator()
    view = View()
    ControllerLoop(model,view).mainLoop()
    



                    



