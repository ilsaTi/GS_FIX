
# import necessary modules
import sys
import numpy as np


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('python file.py filename')
        exit(1)

    filename = sys.argv[1]

    #intitating data dictionary 
    # data_product dictionary to keep track of product, later on used for calculating average value.
    data = dict()
    data_product = dict()

    # loop to read line by line of generated fake message
    for line in open(filename, 'r'):
        #print line
        line = line.strip().split('|')[2:]
        for item in line:
            item = item.split('=')
            if item[0] in data.keys():
                data[item[0]].append(item[1])
            else:
                data[item[0]] = [item[1]]
            if item[0]=='55':
                if item[1] in data_product.keys():
                    data_product[item[1]].append(int(line[2].split('=')[1]))
                else:
                    data_product[item[1]] = [int(line[2].split('=')[1])]

    # data 1: show the count of stock types
    print('Count of stock types')
    print('# FUT:', data['167'].count('FUT'))
    print('# OPT:', data['167'].count('OPT'))
    print('# CS:', data['167'].count('CS'))

    # data 2: show the minimum,mean,median,maximum values for 'buy' and 'sell'.
           # Also shows 'average gain-difference of mean values',
           #a +ve value = profit, a -ve value = loss for the overall investment trend
    buy = []; sell = []
    for index_val, val in enumerate(data['54']):
        if val == '1':
            buy.append(float(data['44'][index_val]))
        else:
            sell.append(float(data['44'][index_val]))
    print('\n', 'Comparison of Buy and Sell prices')
    print('buy:')
    print('The minimum is: ', np.min(buy))
    print('The mean is: ', np.mean(buy))
    print('The median is: ', np.median(buy))
    print('The maximum is: ', np.max(buy))

    print('sell:')
    print('The minimum is: ', np.min(sell))
    print('The mean is: ', np.mean(sell))
    print('The median is: ', np.median(sell))
    print('The maximum is: ', np.max(sell))

    print('avg. gain:',  np.mean(sell) - np.mean(buy))

    #data 3 - occurences of unique symbol
    print('\n', 'Occurences of unique symbols')
    uniq_symbol = set(data['55'])
    max_symbol = ''
    max_symbol_count = -np.inf
    for item in uniq_symbol:
        count_symbol = data['55'].count(item)
        print(item, ':', count_symbol)
        if count_symbol > max_symbol_count:
            max_symbol = item
            max_symbol_count = count_symbol

    #data 4 - most popular symbol:
    print('Most popular symbol')

    print ('max_pop_sym', max_symbol, 'count:', max_symbol_count)



    #data 5 - occurences of unique orders
    print ('\n','Occurences of unique orders')

    orders ={'1':'Market', '2':'Limit','3':'Stop','4':'Stop limit','5':'Market on close'}
    popular_order = set(data['40'])
    max_order = ''
    max_order_value = -np.inf
    for order in popular_order:
        count_order = data['40'].count(order)
        print(orders[order], ':', count_order)
        if count_order > max_order_value:
            max_order = order
            max_order_value = count_order

    #data 6 - most popular order-types
    print ('Most popular order:', orders[max_order], ' occurence:', max_order_value, '\n')

    #data 7 - average ordered quantity per product
    print ('Average ordered quantity per product: ')
    for k,v in data_product.items():
        print(k, sum(v)/float(len(v)))