"""
:author: Kenneth & Cajun
:email: ngjookiat2168@gmail.com & cajuntai02@gmail.com
"""

import subprocess as sp
from types import MethodType

from interface import Menu, Option


# creating a menu
power_menu = Menu("Power", 2)


""" OPTION 1 """
power_off = Option("Power Off")

def execute_power_off(self):
    timer = 60
    # sp.call(['shutdown', '-f', 'P', 't', '{}'.format(timer)])
    print(f"shutting down in {timer}...")
    
def error_power_off(self):
    print("Unable to shut down")
    
power_off.execute = MethodType(execute_power_off, power_menu)
power_off.error = MethodType(error_power_off, power_menu)


""" OPTION 2 """
restart = Option("Restart")

def execute_restart(self):
    timer = 60
    # sp.call(['shutdown', '-f', '-r', '-t', '60'])
    print(f"Restarting in {timer}...")
    
def error_restart(self):
    print("Unable to restart")
    
restart.execute = MethodType(execute_restart, power_menu)
restart.error = MethodType(error_restart, power_menu)


""" OPTION 3 """
log_out = Option("Log out")

def execute_log_out(self):
    timer = 60
    # sp.call(['shutdown', '-f', '-s', '-t', '60'])
    print(f"Logging out in {timer}...")
    
def error_log_out(self):
    print("Unable to log out")
    
log_out.execute = MethodType(execute_log_out, power_menu)
log_out.error = MethodType(error_log_out, power_menu)


""" Add options into menu """
power_menu.add_option(power_off)
power_menu.add_option(restart)
power_menu.add_option(log_out)