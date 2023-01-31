#!/usr/bin/env python3

"""
:author: Kenneth & Cajun
:email: ngjookiat2168@gmail.com & cajuntai02@gmail.com
"""

from serial import Serial, SerialException
import rospy

from wifi_menu import *
from hotspot_menu import *
from power_menu import *


class SerialApplication:
    def __init__(self):
        self.menus = {}
        self.is_input_valid = True
        
        for i in range(10):
            try:
                self._serial = Serial(f"/dev/ttyUSB{i}")
                
                print("come here in Serial Application")
                rospy.loginfo(f"Connected to /dev/ttyUSB{i}")
                break
            except:
                rospy.logerr("Serial port not found!")

    def add_menu(self, menu, key):
        self.menus[key] = menu
    
    def add_option(self, option, key):
        self.menus[key] = option
        
    def print_main_menu(self):
        if len(self.menus) == 0:
            print("No options to show")
            return

        for i, main_menu_option in enumerate(self.menus):
            print(f"     {i+1}. {self.menus[i].name}")
            self._serial.write(f"     {i+1}. {self.menus[i].name}\n".encode())

    def connect_bt_serial(self):
        try:
            self._serial.write("\nSend any input to initialize...\n".encode())
            self._serial.readline()
            self._serial.write("Connected".encode())
        except SerialException:
            rospy.logerr("Unable to initialize communication with Bluetooth Serial")
            pass
    
    def check_valid_input(self):
        try:
            self.menus[self.serial_input]
            self.is_input_valid = True
        except:
            rospy.logerr("Invalid input")
            self._serial.write("Invalid input\n".encode())
            self.is_input_valid = False
    
    def run(self):
        
        while True:
            self.print_main_menu()
            self._serial.write("\nPlease input a value:\n".encode())
            try:
                self.serial_input = int(self._serial.readline().decode().strip()) - 1
            except ValueError:
                self._serial.write("Please enter an integer value:\n".encode())
                continue
            
            self.check_valid_input()
            
            if self.is_input_valid == True:
                self.menus[self.serial_input].execute()
                    

if __name__ == "__main__":
    rospy.init_node("bluetooth_serial")
    
    serial_app = SerialApplication()
    
    vars_copy = vars().copy()
    for k, v in vars_copy.items():
        if isinstance(v, Option) or isinstance(v, Menu):
            v.init_serial(serial_app)
            
    menu_list = [wifi_menu, hotspot_menu, power_menu]
    
    for menu in menu_list:
        serial_app.add_menu(menu, menu.key)
    
    serial_app.run()    

