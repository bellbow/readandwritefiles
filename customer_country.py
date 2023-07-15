import csv

customers = open('customers.csv','r')
customer_file = csv.reader(customers, delimiter=',')

country_file = open('customer_country.csv','w')

next(customer_file)
for record in customer_file:
    country_file.write(record[1]+ ' ' + record[2] + ' ' + record[4] + '\n')

country_file.close()
customers.close()