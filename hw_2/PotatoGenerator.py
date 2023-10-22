from hw_2.ItemFabric import ItemFabric
from hw_2.PotatoReward import PotatoReward


class PotatoGenerator(ItemFabric):

    def create_item(self):
        print("Создали сундук с картошкой")
        return PotatoReward()
