"""
:author: Cajun
:email: cajuntai02@gmail.com
"""


from types import MethodType
import subprocess as sp
import rospy

from interface import Menu, Option


# creating a menu
wifi_menu = Menu("wifi", 0)


""" OPTION 1 """
wifi_on = Option("Wi-Fi on")

def execute_wifi_on(self):
    
    self.wifi_flag = sp.check_output(["nmcli", "radio", "wifi"]).decode().strip()
    
    if self.wifi_flag == 'disabled':   # Skips subproc if Wi-Fi is already enabled
        try:
            sp.run(["nmcli", "radio", "wifi", "on"])
            rospy.loginfo("Wi-Fi Enabled")
            self._serial.write("Wi-Fi Enabled".encode())
        except:
            rospy.logerr("Wi-Fi enabling failed")
    else:
        rospy.loginfo("Wi-Fi already enabled")
        
def error_wifi_on(self):
    self._serial.write("Error: Unable to Turn on Wi-Fi".enocde())

wifi_on.execute = MethodType(execute_wifi_on, wifi_menu)
wifi_on.error = MethodType(error_wifi_on, wifi_menu)



""" OPTION 2 """
wifi_off = Option("Wi-Fi off")

def execute_wifi_off(self):
    self.wifi_flag = sp.check_output(["nmcli", "radio", "wifi"]).decode().strip()
    
    if self.wifi_flag == 'enabled':   # Skips subproc if Wi-Fi is already enabled
        try:
            sp.run(["nmcli", "radio", "wifi", "off"])
            rospy.loginfo("Wi-Fi disabled")
            self._serial.write("Wi-Fi disabled".encode())
        except:
            rospy.logerr("Wi-Fi disabling failed")
    else:
        rospy.loginfo("Wi-Fi already disabled")

wifi_off.execute = MethodType(execute_wifi_off, wifi_menu)



"""" Add options to the menu """
wifi_menu.add_option(wifi_on)
wifi_menu.add_option(wifi_off)


