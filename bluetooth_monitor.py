#!/usr/bin/env python3

"""
:author: Kenneth & Cajun
:email: ngjookiat2168@gmail.com & cajuntai02@gmail.com
"""

"""
To create a bluetooth serial connection to control the UGV
"""

import rospy
from std_msgs.msg import Bool
import netifaces as ni
import pyserial as Serial
import subprocess as sp

def logout():
    sp.call(['shutdown', '-f', '-s', '-t', '60'])

def restart():
    sp.call(['shutdown', '-f', '-r', '-t', '60'])

def shutdown():
    sp.call(['shutdown', '-f', 'P', 't', '60'])


if __name__ == '__main__':
	rospy.init_node('bluetooth_monitor')
	pub = rospy.Publisher("/bluetooth_monitor", Bool, queue_size=10)
	rate = rospy.Rate(50)
	while not rospy.is_shutdown():
        try:
            print("Bluetooth Serial Monitor Menu\n1. Wifi\n 2. Power")
            bluetooth_input = int(input("Please insert an option: "))
            if bluetooth_input == 1:
                wifi_input = int(input("1. Connect\n2. Disconnect\n3. IP address"))
                if wifi_input == 1:
                    displayAvailableNetworks()
                    print("Connected")
                elif wifi_input == 2:
                    print("Disconnected")
                elif wifi_input == 3:
                    print("IP Address")
                    # list_interface = ni.interfaces()
                    # for i in range (0,list_interface):
                    #     print("{1}.{2}").format(i, interface)
                else:
                    input("Please insert available option")
            elif bluetooth_input == 2:
                power_input = int(input("1. Power Off\n2. Suspend\n3. Logout\n4. Restart"))
                if power_input == 1:
                    print("The system has been shut down")
                    shutdown()
                elif power_input == 2:
                    print("User has been suspended from the system")
                elif power_input == 3:
                    print("User has been logout from the system")
                    logout()
                elif power_input == 4:
                    print("The system has been restarted")
                    restart()
                else:
                    print("Please insert available option")
            else:
                print("Please insert available option")
        except:
            print("Please insert a numerical value")
