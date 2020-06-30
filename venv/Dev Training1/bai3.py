import requests
import json
import csv
customerUrl = 'https://5a3009c08acb4398bad7c0f9406075a9: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@leduccuong.myshopify.com/admin/api/2020-07/customers.json'
requests = requests.get(customerUrl)
data = requests.json()
print(data)
customer = data['customers']
file_csv = open('test.csv', 'w')
csvwriter = csv.writer(file_csv)
count = 0
for c in customer:
      if count == 0:
             header = c.keys()
             csvwriter.writerow(header)
             count += 1
      csvwriter.writerow(c.values())
file_csv.close()
