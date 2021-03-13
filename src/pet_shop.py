#1
from typing import Collection, Counter


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
# def get_pets_by_breed(pet_shop, breed):
#     pets= pet_shop['pets']
    
#     breed_found = []
#     breed_not_found = []
    
#     for pet in pets:
#         if pet['breed'] == 'British Shorthair':
#             breed_found.append(pet['breed'])
#         return len(breed_found)
    

def get_pets_by_breed(pet_shop, breed):
    breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == 'British Shorthair':
            breed.append(pet)
            print(len(breed))
    return breed












# import copy
# def get_pets_by_breed(pet_shop, breed):
    
#     pets= pet_shop['pets']
    
#     list_of_breeds = list()
#     breed_type = pet_shop.items()
#     for item  in breed_type:
#         if item[0] == breed:
#             list_of_breeds.append(item[0])
#     list_of_breeds = [key  for (key, value) in pets.items() if value == 'British Shorthair'] 
#     return  len(list_of_breeds)


#list comprehension        














    # breed_count = []        
    
    # if breed in pet_shop == 'British Shorthair':
    #     breed_count.append(breed)
    #     pet_shop.get('breed')
    #     len(breed)
    
    
    # # elif breed =='Dalmation':
    # #     breed_count.append(breed)
    
    # # len(breed_count)
    # #pet_list=pet_shop['pets']['breed']
    
    # # breed_count=[]
    # # for breed in pet_shop:
    # #     if breed == 'British Shorthair':
    # #         breed_count.append(pet_list.count(breed))
    
    # return breed_count

    