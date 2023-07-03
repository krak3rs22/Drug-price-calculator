def drug_price(prices, refund_level, name, insurance, refund=100):
    
    if name not in prices:
        return "This drug is not available at the pharmacy."

    if name not in refund_level:
        return prices[name]

    if insurance:
        if "LS" in refund_level[name]:
            return 3.20
        else:
            lump_sum = refund if refund <= 100 else 100
            return prices[name] * lump_sum / 100
    else:
        return prices[name]


# DICTIONARY OF REFUNDS
refund_level = {
    "Actelsar": [30],
    "Budiair": [30, "LS"],
    "Fromili 500": [50],
    "Metformax 100": ["LS"],
    "Pulmicort": [30, "LS"],
    "Zyrtec": [30],
}

# DICTIONARY OF PRICES
prices = {
    "Navasin 0.05": 16.70,
    "Actelsar": 25.68,
    "Enterol 250": 20.37,
    "Ibuprofen Hasco": 6.85,
    "Budiair": 64.32,
    "Apap": 17.95,
    "Altacel": 7.50,
    "Fromilid 500": 48.06,
    "Metformax 1000": 21.17,
    "Pulmicort": 79.41,
    "Zyrtec": 17.15,
}

# TESTING
print("data: drug_price(prices, refund_level, 'Apap', True)")
print(drug_price(prices, refund_level, "Apap", True))
print("data: drug_price(prices, refund_level, 'Apap', False)")
print(drug_price(prices, refund_level, "Apap", False))
print("data: drug_price(prices, refund_level, 'Fenistil', True)")
print(drug_price(prices, refund_level, "Fenistil", True))
print("data: drug_price(prices, refund_level, 'Pulmicort', False)")
print(drug_price(prices, refund_level, "Pulmicort", False))
print("data: drug_price(prices, refund_level, 'Pulmicort', True)")
print(drug_price(prices, refund_level, "Pulmicort", True))
print("data: drug_price(prices, refund_level, 'Navasin 0.05', True)")
print(drug_price(prices, refund_level, "Navasin 0.05", True))
print("data: drug_price(prices, refund_level, 'Fromili 500', False)")
print(drug_price(prices, refund_level, "Fromili 500", False))
print("data: drug_price(prices, refund_level, 'Zyrtec', True)")
print(drug_price(prices, refund_level, "Zyrtec", True))
print("data: drug_price(prices, refund_level, 'Metformax 1000', True)")
print(drug_price(prices, refund_level, "Metformax 1000", True))

# This function calculates the price of a drug depending on factors such as insurance, and a lump sum of the drug, the dictionaries could be expanded by adding different data to them