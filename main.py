# Randomizer written by Eric Dee. The intent was to avoid using shuffle or zip for a more manual experience

import random

# First combine a list of products, and a list of prices.

products = ["shoelace", "speakers", "headset", "television", "kitchen table", "laptop", "jacket", "blanket", "beer"]

prices = []

def define_prices(prices):
    for i in range (0, 16):
        prices.append(random.randint(1,1296))

def assign_prices(products, prices):
    
    if not prices:
        define_prices(prices)

    assignments = {}

    def block_prices(prices, parallelIndex):
        '''
        Assign a price while never matching the competing object (Do not create a set)
        '''
        price = prices[random.choice(range(1, len(prices)))]
        while price == prices[parallelIndex]:
            price = prices[random.choice(range(1, len(prices)))]
        return price

    # Generate an unpriced dictionary
    returnParallelPass = lambda product_name, prices, parallelIndex : {"product_name": product_name, "priced": False if not prices else prices[parallelIndex]}
    
    # Generate a randomly priced full outer join
    returnRandomPass = lambda product_name, prices, parallelIndex : {"product_name": product_name, "priced": False if not prices else block_prices(prices, parallelIndex)}
    
    assignments = [returnRandomPass(productName, prices, productIndex) for productIndex, productName in enumerate(products)]

    # Next step build a table

    print(assignments)




####
################ Main:

assign_prices(products, prices)

# Needs test cases