"""
:author: Cajun
:email: cajuntai02@gmail.com
"""


from types import MethodType

from interface import Menu, Option


# Add to main menu
hotspot_menu = Menu("hotspot", 1)


""" OPTION 1 """
hotspot_on = Option("hotspot_on")

def execute_hotspot_on(self):
    print("hotspot on")

hotspot_on.execute = MethodType(execute_hotspot_on, hotspot_menu)


""" OPTION 2 """
hotspot_off = Option("hotspot_off")

def execute_hotspot_off(self):
    print("hotspot off")

hotspot_off.execute = MethodType(execute_hotspot_off, hotspot_menu)


""" Add options to menu """
hotspot_menu.add_option(hotspot_on)
hotspot_menu.add_option(hotspot_off)
