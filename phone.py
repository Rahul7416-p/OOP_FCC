# When to use class method and when to use static methods ?
from item import Item
import csv

class Phone(Item):
    all = []
    
    def __init__(self, name:str , price:float|int , quantity=0, broken_phones=0)-> None:
        """Details of Phone Models

        Args:
            name (str): Name of the Phone model
            price (float | int): Price of the phone per unit
            quantity (int, optional): No.of Phone items present. Defaults to 0.
            broken_phones (int, optional): No.of broken phone items. Defaults to 0.
        """
        # Call to super fuunction to have access to all attributes/ method of the parent class `Item`
        super().__init__(
            name, price, quantity
        )
        # Run validations to the received arguments 
        assert broken_phones >= 0, f" Broken_phones {broken_phones} is not greater than or equal to zero! "
        
        # Assign to self object 
        self.broken_phones = broken_phones 
        
        # Actions to execute 
        Phone.all.append(self) 
    
    @classmethod
    def instantiate_from_csv(cls,flname:str)-> None:
        """ Generates Phone objects from a csv file containing phone details. 
            (name, price, quantity, broken_phones)

        Args:
            flname (str): CSV Filename containing phone details 
        """
        with open(flname,'r') as f :
            reader = csv.DictReader(f)
            phones = list(reader)
            
        for phone in phones:
            Phone(
                name=phone.get('name'),
                price= int(phone.get('price')) if Phone.check_integer(float(phone.get('price'))) else float((phone.get('price'))),
                quantity=int(phone.get('quantity')),
                broken_phones=int(phone.get('broken_phones'))
                
            )
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self._price}, {self.quantity}, {self.broken_phones})"
