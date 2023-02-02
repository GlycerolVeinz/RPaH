class Item:
 
    def __init__(self, name: str, days_left: int, quality: int):
        self.name = name
        self.days_left = days_left
        self.quality = quality

def update(item: Item):
    item.days_left -= 1
