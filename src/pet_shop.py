#1
def get_pet_shop_name(pet_shop):
    return pet_shop['name']             #[]refering to a dictionary key, either {} or []
    print([])
    

#2
def get_total_cash(pet_shop):
    return pet_shop['admin']['total_cash']

#3
def add_or_remove_cash(pet_shop, amount):
    pet_shop['admin']['total_cash'] += amount
#    get_total_cash(pet_shop)+= amount

#4
