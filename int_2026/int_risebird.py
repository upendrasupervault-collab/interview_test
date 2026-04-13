# Write a Python script to process a 10GB log file:

# Extract error records
# Group by error type
# Return top 5 errors by frequency
# 👉 Constraints: Must be memory efficient (generator/iterators)

path = logfile.txt

def process_log(file):
    with open(path,'r') as r:
        line = r.readline()
        
        log ,status_code = line.split(" ")
        result = {}
        if status_code in [400,401,403,404,501,502,503]:
            result[status_code]+=result.get('status_code',0)
        
        #soting dict based on count
        sorted_result = sorted(result.items(),key=lambda x:x[1])
        top_5_result = sorted_result[:5]
        return dict(top_5_result)

Async API with Dependency Injection

Build a FastAPI service:

Async endpoints
DB dependency injection
Request validation (Pydantic)
Proper exception handling


from mysql import mysql
def sql_connect():
    host=127.0.0.1
    user_name = os.env.get("username",'kapricon')
    password = os.env.get("password",'abcd1234')
    port=5432
    
    conn = mysql.connection().connect(
        username=username,
        host=host,
        password=password,
        port=port
        )
    
    return conn


####################
# this is my py file
from fastapi import FastApi
from Pydantic import basemodel
from logger import logging
import uvicorn

app = FastAppi()
class Records(basemodel):
    id= int

logger = logging()

async def get_records(request:Records,sql_connect):
    con = sql_connect()
    try:
        data = con.execute(f'select id,name,details from Records where id = {request.id}')
        data = jsonify(data)
        return data
    except Exception as e:
        logger.error(f' we got error while fetching data from db {e}')
if __name__ == __main__():
    app.start(host=localhost,port=8000,debug=True)
    

