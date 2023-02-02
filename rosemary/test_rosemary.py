from rosemary import Item, update


# normal item parametrs check
def test_normal_item_name():
    item = Item('Bread', days_left = 3, quality = 5)
    update(item)
    return item.name == 'Bread'


def test_normal_item_decreases_days_left():
    item = Item('Bread', days_left = 3, quality = 5)
    update(item)
    return item.days_left == 2


def test_normal_item_decrease_quality():
    item = Item('Bread', days_left = 3, quality = 5)
    update(item)
    return item.quality == 4


#special ocasions for normal items


def test_normal_item_not_bellow_zero_days_left():
    item = Item('Bread', days_left = 0, quality = 5)
    update(item)
    return item.days_left == -1

def test_normal_item_quality_zero():
    item = Item('Bread', days_left = 3, quality = 0)
    update(item)
    return item.quality == 0

def test_normal_item_faster_quality_decrese():
    item = Item('Bread', days_left = 0, quality = 5)
    update(item)
    return item.quality == 3

def test_normal_item_decrease_quality_near_zero_days_left():
    item = Item('Bread', days_left = 1, quality = 5)
    update(item)
    return item.quality == 4

def test_normal_item_bellow_zero_days_left_quality_zero():
    item = Item('Bread', days_left = 0, quality = 0)
    update(item)
    return item.quality == 0

#   SPECIAL ITEMS TESTS

#  diamond set of tests

def test_diamond_name():
    item = Item('Diamond', days_left = 100, quality = 100)
    update(item)
    return item.name == 'Diamond'

def test_diamond_days_left():
    item = Item('Diamond', days_left = 100, quality = 100)
    update(item)
    return item.days_left == 100

def test_diamond_quality():
    item = Item('Diamond', days_left = 100, quality = 100)
    update(item)
    return item.quality == 100

# aged brie set of tests

def test_brie_name():
    item = Item('Aged Brie', days_left = 0, quality = 5)
    update(item)
    return item.name == 'Aged Brie'

def test_brie_days_left():
    item = Item('Aged Brie', days_left = 5, quality = 5)
    update(item)
    return item.days_left == 4

def test_brie_days_left_bollow_zero():
    item = Item('Aged Brie', days_left = 0, quality = 5)
    update(item)
    return item.days_left == -1

def test_brie_quality():
    item = Item('Aged Brie', days_left = 4, quality = 5)
    update(item)
    return item.quality == 6

def test_brie_quality_near_zero_days_left():
    item = Item('Aged Brie', days_left = 0, quality = 5)
    update(item)
    return item.quality == 6

def test_brie_quality_at_max():
    item = Item('Aged Brie', days_left = 0, quality = 50)
    update(item)
    return item.quality == 50

# tickets set of tests

def test_tickets_name():
    item = Item('Tickets', days_left = 30, quality = 5)
    update(item)
    return item.name == 'Tickets'

def test_tickets_days_left_decrease():
    item = Item('Tickets', days_left = 30, quality = 5)
    update(item)
    return item.days_left == 29

def test_tickets_quality_increase():
    item = Item('Tickets', days_left = 30, quality = 5)
    update(item)
    return item.quality == 6

def test_tickets_quality_increase_plus_two_upper():
    item = Item('Tickets', days_left = 10, quality = 5)
    update(item)
    return item.quality == 7

def test_tickets_quality_increase_plus_two_lower():
    item = Item('Tickets', days_left = 6, quality = 5)
    update(item)
    return item.quality == 7

def test_tickets_quality_increase_plus_three_upper():
    item = Item('Tickets', days_left = 5, quality = 5)
    update(item)
    return item.quality == 8

def test_tickets_quality_increase_plus_three_upper():
    item = Item('Tickets', days_left = 1, quality = 5)
    update(item)
    return item.quality == 8

def test_tickets_quality_zero():
    item = Item('Tickets', days_left = 0, quality = 5)
    update(item)
    return item.quality == 0

def test_tickets_quality_above_fifty():
    item = Item('Tickets', days_left = 30, quality = 50)
    update(item)
    return item.quality == 50

def test_tickets_quality_higher_fifty():
    item = Item('Tickets', days_left = 4, quality = 50)
    update(item)
    return item.quality == 50