"""
:author: Cajun
:email: cajuntai02@gmail.com
"""


class Menu:
    def __init__(self, name, key, options=None):
        self.name = name
        self.key = key
        self.options = options if options else []
        self.serial = None
        
    def init_serial(self, serial):
        self._serial = serial._serial
    
    def print_menu(self):
        
        if len(self.options) == 0:
            print("No options to show")
            self._serial.write("No options to show".encode())
            return

        for i, option in enumerate(self.options):
            print(f"{i+1}. {option.name}")
            self._serial.write(f"{i+1}. {option.name}")
        
    def add_option(self, option):
        self.options.append(option)
    
    def remove_option(self, option):
        self.options.remove(option)

    def execute(self):
        self.print_menu()
        self._serial.write("please choose an option: ".encode())
        while True:
            try:
                input_ = int(self._serial.readline().decode().strip()) 
                break
            except ValueError:
                self._serial.write("Please enter an integer value:\n".encode())
                self.print_menu()
        
        if input_ > len(self.options) or input_ < 1:
            print("invalid input")
            return
        
        self.options[input_-1].execute()
        
    def error(self):
        pass
        

class Option:
    def __init__(self, name):
        self.name = name
        self._serial = None
        
    def init_serial(self, serial):
        self._serial = serial
    
    def execute(self):        
        print("No excute function is assigned")

    def error(self, e):
        print(e)
        pass 

