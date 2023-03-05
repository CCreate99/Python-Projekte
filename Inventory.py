def print_inventory(inventory, leftWidth, rightWidth):
    total_items = 0
    payload = 200
    weight = 0
    print('INVENTORY'.center(21, '-'))
    for k, v, in inventory.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

        total_items += v

        if k != inventory['Gold']:
            payload -= v
        elif k == inventory['Gold']:
            weight = gold / 20
            payload -= gewicht

    print("Total amount of Items: " + str(total_items))
    print("Now you carry " + str(200-payload) + "kg of 200kg you have " + str(payload) + "kg left")

def add_To_Inventory(inventory, dragonLoot):
    global items
    for i in range(len(dragonLoot)):
        if dragonLoot[i] not in inventory.keys():
            loot = dragonLoot[i]
            inventory[loot] = 1

        elif dragonLoot[i] in inventory.keys():
            loot = dragonLoot[i]
            inventory[loot] += 1




if __name__ == "__main__":
    while True:
        items = {'Dagger': 2, 'Potion': 5,'Key': 1,'Sword': 1,'Gold': 1,'Armor': 1}
        dragonLoot = ['Gold', 'LegendarySword', 'Gold', 'DragonArmor', 'Ruby']
        redDragonLoot = ['Elder Wand', 'Silver Coin', 'Vype', 'RedBull']

        add_To_Inventory(items, dragonLoot)
        print_inventory(items, 15, 6)
        add_To_Inventory(items, redDragonLoot)
        print_inventory(items, 15, 6)

        print(items.keys())
        break