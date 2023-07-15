import csv

sales = open('sales.csv', 'r')
sales_record = csv.reader(sales, delimiter=',')

report = open('salesreport.csv','w')

report.write('Customer ID,Total \n')
next(sales_record)
customer_ids = {}
for record in sales_record:
    total = float(record[3]) + float(record[4]) + float(record[5])
    if record[0] in customer_ids:
        customer_ids[record[0]] += total
    else:
        customer_ids[record[0]] = total

for k,v in customer_ids.items():
    customer_report = k +',' + str(v) +'\n'
    report.write(customer_report)

report.close()
sales.close()