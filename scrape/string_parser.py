# returns the string version of the price in an input string
def find_price(string):
    index_of_dollar = string.find('$')
    index_of_next_space = string.find(' ', index_of_dollar)
    if index_of_dollar > -1 and index_of_next_space > -1:
        return string[index_of_dollar + 1: index_of_next_space].replace(',', '')
    else:
        return -1
