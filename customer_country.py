import csv

customers = open('customers.csv','r')
customer_file = csv.reader(customers, delimiter=',')

country_file = open('customer_country.csv','w')

counter = 0

next(customer_file)
for record in customer_file:
    country_file.write(record[1]+ ' ' + record[2] + ' ' + record[4] + '\n')
    counter += 1

print("Total Customers: " + str(counter))

country_file.close()
customers.close()