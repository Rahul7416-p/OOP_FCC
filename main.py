from item import Item
from phone import Phone


Item.instantiate_from_csv("items.csv")
print(Item.all)

Phone.instantiate_from_csv("phones.csv")
print(Phone.all)

print(Item.all)