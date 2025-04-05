from  Base.base_page import BasePage


class Loaddata():
    def __init__(self):
        super().__init__()
        self.load_test_data=BasePage

    def read(self,filename='TestData/testdata/Employee_info.json'):
        data = self.load_test_data(filename)
        print (data['First_name'])
        return data
k=Loaddata()
print(k.read())


