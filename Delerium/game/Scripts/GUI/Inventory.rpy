init python:
    class Inventory():
        #initializes self, items list and number of items
        def __init__(self, items, num_of_items):
            self.items = items
            self.num_of_items = num_of_items
        #add and remove items, increases and decreases item increment by 1
        def add_item(self, item):
            self.items.append(item)
            self.num_of_items += 1

        def remove_item(self, item):
            self.items.remove(item)
            self.num_of_items -= 1

        def list_items(self):
            if len(self.items) < 1:
                y ("I'm not carrying anything")
            else:
                y ("I am currently carrying:")
                for item in self.items:
                    #prefacing f before strings allows you to directly use variables include {} in pure python
                    y (f"{item.name}. {item.description}.")

        

    class InventoryItem():
        def __init__(self, name, description):
            self.name = name
            self.description = description