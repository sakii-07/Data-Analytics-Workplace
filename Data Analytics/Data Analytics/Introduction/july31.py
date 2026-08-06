retail_branches = {
  301: {
    "branch_name": "Pune Central",
    "location": ("Pune", "Maharashtra"),
    "manager": "Amit",
    "sales": [4500, 7200, 3200, 9800, 5600, 11000],
    "products": ["Laptop", "Mobile", "Keyboard", "Laptop", "Headphones", "Mobile"],
    "cost_prices": [3800, 6000, 2500, 8200, 4200, 9000],
    "payment_modes": ["UPI", "Card", "Cash", "Card", "UPI", "Card"],
    "order_status": ["Completed", "Completed", "Returned", "Completed", "Pending", "Completed"],
    "customer_ratings": [4, 5, 3, 5, 4, 5]
  },
  302: {
    "branch_name": "Mumbai West",
    "location": ("Mumbai", "Maharashtra"),
    "manager": "Sneha",
    "sales": [8500, 12500, 4300, 6700, 15000],
    "products": ["Television", "Laptop", "Mouse", "Mobile", "Television"],
    "cost_prices": [7000, 10500, 3000, 5600, 12500],
    "payment_modes": ["Card", "Card", "Cash", "UPI", "UPI"],
    "order_status": ["Completed", "Completed", "Completed", "Cancelled", "Completed"],
    "customer_ratings": [4, 5, 4, 2, 5]
  },
  303: {
    "branch_name": "Nashik Road",
    "location": ("Nashik", "Maharashtra"),
    "manager": "Rahul",
    "sales": [2200, 3500, 4800, 7500, 2900, 6200],
    "products": ["Keyboard", "Mouse", "Headphones", "Mobile", "Keyboard", "Smartwatch"],
    "cost_prices": [1600, 2500, 3500, 6300, 2100, 5000],
    "payment_modes": ["Cash", "UPI", "Card", "UPI", "Cash", "Card"],
    "order_status": ["Completed", "Returned", "Completed", "Completed", "Completed", "Pending"],
    "customer_ratings": [3, 2, 4, 5, 4, 3]
  },
  304: {
    "branch_name": "Nagpur East",
    "location": ("Nagpur", "Maharashtra"),
    "manager": "Priya",
    "sales": [5600, 8900, 10500, 3200, 7800],
    "products": ["Mobile", "Laptop", "Television", "Mouse", "Mobile"],
    "cost_prices": [4500, 7400, 8800, 2300, 6500],
    "payment_modes": ["UPI", "Card", "Card", "Cash", "UPI"],
    "order_status": ["Completed", "Completed", "Pending", "Completed", "Returned"],
    "customer_ratings": [4, 5, 4, 3, 2]
  }
}


'''
Task 1: Calculate Branch Sales, Cost, and Profit
For every branch, calculate and print the total sales, total cost, and total profit.
'''

for branch_id, branch in retail_branches.items():
    print('Branch : ', branch['branch_name'])
    total_sales = 0
    total_cost = 0
    for key, value in branch.items():
        if key == 'sales':
            total_sales = sum(value)

        if key == 'cost_prices':
            total_cost = sum(value)

    print('Total sales : INR ',total_sales)
    print('Total cost : INR', total_cost)
    profit = total_sales - total_cost
    print('Total Profit : INR',profit)

    print()

'''
Task #2: Print a Transaction-Wise Profit Report
For every transaction, print all related information by matching values through the same list index.
'''



'''
Task #3: Calculate Completed, Lost, and Pending Revenue
For every branch, calculate revenue based on order status.
• Completed Revenue: include only orders with status "Completed".
• Lost Revenue: include orders with status "Returned" or "Cancelled".
• Pending Revenue: include orders with status "Pending"
'''

for branch_id, branch in retail_branches.items():
    print('Branch : ', branch['branch_name'])
    status_dict = {}
    for i in range(len(branch['order_status'])):
        if branch['order_status'][i] not in status_dict:
            status_dict[branch['order_status'][i]] = branch['sales'][i]
        else:
            status_dict[branch['order_status'][i]] = status_dict[branch['order_status'][i]] +branch['sales'][i]
    for status, sales in status_dict.items():
        print(status, '--->',sales)
    print()
 
        

'''
Task #4: Create a Product Performance Dictionary
Create a company-wide dictionary containing product-level metrics.
• For each product calculate quantity, total revenue, total cost, and total profit.
• Generate product names dynamically; do not manually write product keys.
product_performance = {
  "Laptop": {
    "quantity_sold": 0,
    "total_revenue": 0,
    "total_cost": 0,
    "total_profit": 0
  }
}
'''
for branch_id, branch in retail_branches.items():
    print('Branch : ', branch['branch_name'])
    product_performance = {}
    for i in range(len(branch['order_status'])):
        product =  branch['products'][i]
        if product not in product_performance:
            product_performance[product] = {
            'quantity_sold' : 1,
            'total_revenue': branch['sales'][i],
            'total_cost' : branch['cost_prices'][i],
            'total_profit' :branch['sales'][i]- branch['cost_prices'][i]
            }
        else:
            product_performance[product]['quantity_sold'] += 1
            product_performance[product]['total_revenue'] +=  branch['sales'][i]
            product_performance[product]['total_cost'] +=  branch['cost_prices'][i]
            product_performance[product]['total_profit'] = product_performance[product]['total_profit'] + branch['sales'][i]- branch['cost_prices'][i]

    for i,v in product_performance.items():
        print(i,"\n","\t",v)
            
    print()

# Task #5: Find the Most Profitable Product
# Using the product performance dictionary, identify the product with the highest total profit.
# • Print product name, transaction count, total revenue, total cost, and total profit.
# • The result must be calculated dynamically.

for branch_id, branch in retail_branches.items():
    print('Branch : ', branch['branch_name'])
    product_performance = {}
    for i in range(len(branch['order_status'])):
        product =  branch['products'][i]
        if product not in product_performance:
            product_performance[product] = {
            'quantity_sold' : 1,
            'total_revenue': branch['sales'][i],
            'total_cost' : branch['cost_prices'][i],
            'total_profit' :branch['sales'][i]- branch['cost_prices'][i]
            }
        else:
            product_performance[product]['quantity_sold'] += 1
            product_performance[product]['total_revenue'] +=  branch['sales'][i]
            product_performance[product]['total_cost'] +=  branch['cost_prices'][i]
            product_performance[product]['total_profit'] = product_performance[product]['total_profit'] + branch['sales'][i]- branch['cost_prices'][i]

    for i,v in product_performance.items():
        print(i,"\n","\t",v)
        print(max(product_performance))
            
    print()