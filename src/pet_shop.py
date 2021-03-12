#1
def get_pet_shop_name(pet_shop):
    return pet_shop['name']             #[]refering to a dictionary key, either {} or []
    print([])
    

#2
def get_total_cash(pet_shop):
    return pet_shop['admin']['total_cash']

#3 & 4
def add_or_remove_cash(pet_shop, amount):
    pet_shop['admin']['total_cash'] += amount
#    get_total_cash(pet_shop)+= amount doesnt work due to a infinite loop/ retunring a re assignment into a variable

#5
def get_pets_sold(pet_shop):
    return pet_shop['admin']['pets_sold']

#6
def increase_pets_sold(pet_shop, qty):
    pet_shop['admin']['pets_sold'] += qty

#7
def get_stock_count(pet_shop):
    return len(pet_shop['pets'])  #returning count of keys in dictionary 'pets'
    # total_pets=0
    # for pet in pet_shop:        
    #     total_pets += len(pet_shop['pets'][0]['names'])
    # return total_pets

#8
#def
