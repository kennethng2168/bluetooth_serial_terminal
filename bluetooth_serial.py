#!/usr/bin/env python3

import rospy
# from std_msgs.msg import Bool
import netifaces as ni
import subprocess as sp
from serial import Serial, SerialException


class SerialCallbacks:
    def __init__(self):
        # self.function_names = ["power", "hotspot", "ip"]
        self.hotspot_con_name = "test_hotspot"
        self.hotspot_ssid     = "hotspot_test"
        self.hotspot_password = "12345678"
        self.hotspot_flag     = False
        
        self.wifi_flag        = sp.check_output(["nmcli", "radio", "wifi"]).decode().replace('\n', '')
        self.prev_wifi_flag   = self.wifi_flag
    
    def logout(self):
        sp.call(['shutdown', '-f', '-s', '-t', '60'])

    def restart(self):
        sp.call(['shutdown', '-f', '-r', '-t', '60'])

    def shutdown(self):
        sp.call(['shutdown', '-f', 'P', 't', '60'])
        
    def hotspot(self, serial_input):
        
        if self.hotspot_flag == False and serial_input == "Turn on":
            sp.run(["nmcli", "device", "wifi", "hotspot", "con-name", 
                    self.hotspot_con_name, "ssid", self.hotspot_ssid, 
                    "password", self.hotspot_password])
            self.hotspot_flag = True
            self.write("hotspot successfully activated")
            print("successful")
        elif self.hotspot_flag == True and serial_input == "Turn on":
            sp.run(["nmcli", "connection", "down", self.hotspot_con_name])
            self.hotspot_flag == False
            self.write("hotspot successfully deactivated")
            print("unsuccessful")
        
            
    def ip(self):
        pass
    
    def wifi_toggle(self):
        toggle_options = ("1", "2")
        self.wifi_flag = sp.check_output(["nmcli", "radio", "wifi"]).decode().replace('\n', '')
        
        if self.wifi_flag == 'disabled':   # Skips subproc if Wi-Fi is already enabled
            s.write("Wi-Fi status: {}. Turn it on?\n    1. Yes\n    2.   No\n".format(self.wifi_flag).encode())

            while True:
                toggle_confirm = s.readline().decode().strip() #replace("\r\n", "")
                if toggle_confirm == "1":
                    try:
                        sp.run(["nmcli", "radio", "wifi", "on"])
                        rospy.loginfo("Wi-Fi enabled")
                        s.write("Wi-Fi enabled".encode())
                    except:
                        rospy.logerr("Wi-Fi enabling failed")
                        s.write("Wi-Fi enabling failed")
                    # finally:
                    break
                elif toggle_confirm == "2":
                    print("2")
                    return
                else:
                    print("3")
                    s.write("Please input only the number of the above options".encode())
            # else:
                # s.write("Please enter only 'yes' or 'no')
                # Loop back to function (wrap inner condition statement in closure?)
                    
        elif self.wifi_flag == 'enabled':   # Skips subproc if Wi-Fi is already disabled
            s.write("Wi-Fi status: {}. Turn it off?\n    1. Yes\n    2. No\n".format(self.wifi_flag).encode())
            toggle_confirm = s.readline().decode().strip() #replace("\r\n", "")
            if toggle_confirm == "1":
                try:
                    sp.run(["nmcli", "radio", "wifi", "off"])
                    rospy.loginfo("Wi-Fi disabled")
                    s.write("Wi-Fi disabled".encode())
                except:
                    rospy.logerr("Wi-Fi disabling failed")
                    s.write("Wi-Fi disabling failed")
            elif toggle_confirm == "2":
                return
            
    def wifi_connect_netw(self):
        s.write("Enter Wi-Fi netowrk's name: ".encode())
        # if 
            
  

def search_for_bst(s):
    try:
        s.write("\nSend any input to initialize...\n".encode())
        s.readline()
    except SerialException:
        pass
  

if __name__ == "__main__":
    
    rospy.init_node("bluetooth_serial")
    
    try:
        s = Serial("/dev/ttyUSB0")
        rospy.loginfo("Connected to /dev/ttyUSB2")
    except:
        s = Serial("/dev/ttyUSB1")
        rospy.loginfo("Connected to /dev/ttyUSB1")
    
    search_for_bst(s)
    
    s.write("Connected".encode())
    
    serial_input = s.readline().decode().strip() #replace("\r\n", "")
    print(serial_input)
    
    call = SerialCallbacks()
    
    
    call.wifi_toggle()

