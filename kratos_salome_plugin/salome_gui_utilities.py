#  _  __         _          ___       _               ___ _           _
# | |/ /_ _ __ _| |_ ___ __/ __| __ _| |___ _ __  ___| _ \ |_  _ __ _(_)_ _
# | ' <| '_/ _` |  _/ _ (_-<__ \/ _` | / _ \ '  \/ -_)  _/ | || / _` | | ' \
# |_|\_\_| \__,_|\__\___/__/___/\__,_|_\___/_|_|_\___|_| |_|\_,_\__, |_|_||_|
#                                                               |___/
# License: BSD License ; see LICENSE
#
# Main authors: Philipp Bucher (https://github.com/philbucher)
#

"""
This file contains functions for interacting with the Salome GUI
see https://docs.salome-platform.org/latest/gui/GUI/text_user_interface.html
NOTE: salome.sg has less functionalities when running in TUI mode (compared to when running in GUI mode)
NOTE: This file must NOT have dependencies on other files in the plugin!
"""

# python imports
from typing import List

# salome imports
import salome


def GetAllSelected() -> List[str]:
    """get the list of IDs of all selected objects"""
    return salome.sg.getAllSelected()

def ClearSelection() -> None:
    """clear the selection (set all objects unselected)"""
    salome.sg.ClearIObjects()

def SelectObjects(list_identifiers: List[str]) -> None:
    """selects the given objects"""
    ClearSelection()
    for identifier in list_identifiers:
        salome.sg.AddIObject(identifier)

def HideAll() -> None:
    """hide all objects"""
    salome.sg.EraseAll()
    salome.sg.UpdateView() # update view

def DisplayObjectsOnly(list_identifiers: List[str]) -> None:
    """displays a list of objects (hides all other objects)"""
    HideAll()
    SelectObjects(list_identifiers)
    salome.sg.FitSelection()
