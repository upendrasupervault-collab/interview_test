logs = [
    "2025-03-05 10:01:23 GET /api/products 200",
    "2025-03-05 10:01:25 POST /api/orders 201",
    "2025-03-05 10:01:28 GET /api/products 200",
    "2025-03-05 10:01:30 GET /api/users 404",
    "2025-03-05 10:01:35 GET /api/products 500"
]
 
Counts how many times each endpoint was called.
Groups the count of responses by status code
Returns a summary in dict
 
 
'/api/products': {'count': 3, 'status_codes': {'200': 2, '500': 1}}
 
 
original_string = "banana"
substring = "ana"
 
Declare @ID INT = 0

Begin Tran

Set @ID = 1

Rollback Tran

Select ID
 
def get_count(ostr,sb):

    count=0

    for i in range(len(ostr)-len(sb)+1):

        val = ostr[i:i+len(sb)]

        #print(val,sb)

        if val==sb:

            count+=1

    return count

print(get_count(original_string,substring))
 

 date , month
orderdetails , productdetails 

product names , which are ordered atleast one

# select o.orderid,p.product_name
# from orderdtails o
# innerjoin productsdetails p
# on p.product_id=o.product_id

select product_id 
from productdetails
where product_id not in(select product_id from orderdetails)


logs = [
    "2025-03-05 10:01:23 GET /api/products 200",
    "2025-03-05 10:01:25 POST /api/orders 201",
    "2025-03-05 10:01:28 GET /api/products 200",
    "2025-03-05 10:01:30 GET /api/users 404",
    "2025-03-05 10:01:35 GET /api/products 500"
]
 
# Counts how many times each endpoint was called.
# Groups the count of responses by status code
# Returns a summary in dict
 
 
# '/api/products': {'count': 3, 'status_codes': {'200': 2, '500': 1}}

def ext_info(logs):
    
    result = {}
    for l in logs:
        ts,ep,val = l.split("/")
        api,sc= val.split(" ")
        if result.get(api):
            if result[api].get('count'):
                result[api]['count']+=1
                result[api]['status_codes'].append(sc)
            else:
                result[api]['count']=1
        else:
            
            result[api]={'count':1,'status_codes':[sc]}
    print(result)

ext_info(logs)
 
 