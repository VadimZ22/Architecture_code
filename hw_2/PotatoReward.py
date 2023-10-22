import zope.interface
from hw_2.IGameItem import IGameItem


@zope.interface.implementer(IGameItem)
class PotatoReward:
    def open(self):
        print("Открыли сундук с картошкой")
