stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):

    items_ammount = 0
    
    print ("Inventory:")
    for item in sorted(inventory):
        print(str(inventory[item]) + ' ' + item)
        items_ammount += inventory[item]
    print("Total number of items: " +str(items_ammount))

displayInventory(stuff)