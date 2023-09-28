#from typing import Final, Any , Callable
#import argparse 
import csv 

class Item:
    
    pay_rate: float = 0.8
    all = []
    
    def __init__(self, name:str , price:float|int , quantity=0)->None:
        """ Initialize 

        Args:
            name (str): name of the item
            price (float | int): price of the item 
            quantity (int, optional): Number of items present. Defaults to 0.
        """
        # Run validations to the received arguments 
        assert price >= 0, f" Price {price} is not greater than or equal to zero! "
        assert quantity >= 0, f" Quantity {quantity} is not greater than or equal to zero! "
        
        # Assign to self object 
        self._name = name 
        self._price = price 
        self.quantity = quantity
        
        # Actions to execute 
        Item.all.append(self) 
    
    @property
    # Property Decorator = Read-Only Attribute
    def name(self)-> str:
        return self._name
    
    @name.setter
    def set_name(self, value):
        if len(value) > 10 :
            raise Exception("The name is too long")
        else:
            self._name = value 
    
    @property
    def price(self):
        return self._price        
            
    def apply_discount(self)-> float :
        """ Applies discount on item price

        Returns:
            float: The discounted price 
        """
        return self._price * self.pay_rate
    
    def apply_increment(self, increment_value):
        self._price = self._price + self._price * increment_value
        
    def total_item_price(self) -> float:
        """ Calculates the total price = unit price * quantity

        Returns:
            float : Total item price
        """
        return self._price * self.quantity
       
    @staticmethod
    def check_integer(num:int|float)-> bool:
        """This static method counts out the floats
        that are point zero. 
        For eg. 5.0, 6.0, 10.0
         
        Args:
            num (int|float): Number to be checked 

        Returns:
            bool: True  -> if num is int or float values like 10.0, 12.0, etc
                  False -> if num is not an integer . eg. 12.4 , etc.  
        """
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False    
    @classmethod
    def instantiate_from_csv(cls,flname)-> None:
        with open(flname,'r') as f :
            reader = csv.DictReader(f)
            items = list(reader)
            
        for item in items:
            Item(
                name=item.get('name'),
                price= int(item.get('price')) if Item.check_integer(float(item.get('price'))) else float((item.get('price'))),
                quantity=int(item.get('quantity'))
                
            )
                    
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self._price}, {self.quantity})"

    
    
#parser = argparse.ArgumentParser(description="|| Meow like a cat ||")
#parser.add_argument("-n", help="name of the item", type=str)
#parser.add_argument("-p", help="unit price of item ", type=float)
#parser.add_argument("-q", help="number of items in the store", default=0, type=int)
#args = parser.parse_args()
'''
def main()->None:
    items: list[Item] = []
    while True:
        ans = input("Want to add item in the store ? (y|n) ")
        if ans == 'y' :
            name:str = input("Enter the item name: ")
            price:float = float(input("Enter the unit price: "))
            quantity:float = float(input("Enter the number of items present: "))
            items.append(Item(name,price,quantity))
        else:
            break
        
    if items:
        for i, item in enumerate(items, start=1):
            print(f"Item {i} : {item.__dict__} total_price = {item.total_item_price()}  pay_rate = {item.pay_rate}")        
            
if __name__ == "__main__":
    main()            
'''

