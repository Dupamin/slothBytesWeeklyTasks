class Player():
    def __init__(self):
        self.money = [0, 0, 0, 0] # [quarters, dimes, nickels, pennies]
        self.inventory = {}
        
    def add_money(self, amount):
        self.money[0] += int(amount // 0.25)
        amount = amount % 0.25
        self.money[1] += int(amount // 0.10)
        amount = amount % 0.10
        self.money[2] += int(amount // 0.05)
        amount = amount % 0.05
        self.money[3] += int(amount // 0.01)
        
    def remove_money(self, amount):
        self.money[0] -= int(amount // 0.25)
        amount = amount % 0.25
        self.money[1] -= int(amount // 0.10)
        amount = amount % 0.10
        self.money[2] -= int(amount // 0.05)
        amount = amount % 0.05
        self.money[3] -= int(amount // 0.01)
        
    def add_item(self, item, amount):
        item_count = self.inventory.get(item, 0)
        amount += item_count
        self.inventory.update({item: amount})
    
    def remove_item(self, item, amount):
        item_count = self.inventory.get(item, 0)
        if item_count - amount <= 0:
            self.inventory.pop(item)
        else:
            amount -= item_count
            self.inventory.update({item: amount})
        
    def buy_item(self, item, amount):
        if can_player_purchase_item(self, item, amount):
            self.remove_money(item.value * amount)
            self.add_item(item.name, amount)
    
    def get_inventory(self):
        return self.inventory
        
    def get_money(self):
        return self.money
    
    def count_money_value(self):
        return (self.money[0] * 0.25) + (self.money[1] * 0.10) + (self.money[2] * 0.05) + (self.money[3] * 0.01)
    
class Item():
    def __init__(self, name, value):
        self.name = name
        self.value = value

def can_player_purchase_item(player, item, count=1):
    return player.count_money_value() >= item.value * count

player1 = Player()
item1 = Item("Candy Bar", 1.25)
item2 = Item("Soda", 0.75)
item3 = Item("Chips", 1.00)
item4 = Item("Gun", 100.00)

def test_code():
    print(f"Player 1's money: {player1.get_money()} meaning {player1.count_money_value():.2f}")
    print(f"Player 1's inventory: {player1.get_inventory()}")
    # For Mr SlothBye
    print(f"Can player 1 purchase item 1? {can_player_purchase_item(player1, item1)}")
    print(f"Can player 1 purchase item 2? {can_player_purchase_item(player1, item2)}")
    print(f"Can player 1 purchase item 3? {can_player_purchase_item(player1, item3)}")
    print(f"Can player 1 purchase item 4? {can_player_purchase_item(player1, item4)}")

def main():
    test_code()    
    player1.add_money(14.99)
    test_code()
    player1.buy_item(item1, 3)
    test_code()
    
if __name__ == "__main__":
    main()