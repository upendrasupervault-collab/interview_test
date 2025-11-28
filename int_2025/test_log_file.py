
# Read the log file efficiently (assume it can be several GBs).
# Parse the data and compute:
# Total number of unique users.
# 
# Top 10 users by number of actions performed.
# Handle missing or malformed rows gracefully.
# Optimize for memory and speed (streaming approach preferred).
 
 
# Constraints:
# Use Python (no external big data frameworks like Spark for now).
# Assume the file is too large to fit into memory at once.
# Output results in a structured format (dictionary or JSON).


#Count of each action type (e.g., login, click, logout).
# unique_users_count
 
# action_counts
 
# top_users
 
def get_analytics(filepath):
    result= {"user":{},'operation_count':{}}
    skip = 0
    with open(filepath) as r:
        for line in r:
            if skip < 1:
                skip += 1
                continue
            #print(line)
            data = line.strip().split(",")
            if len(data) != 3:
                continue
            timestamp ,user_id,action= data
            #print(user_id, action, timestamp)
            
            result['operation_count'][action] = result['operation_count'].get(action, 0) + 1
            result['user'][user_id] = result['user'].get(user_id, 0) + 1
    #print(result['user'])
    sorted_user_data = sorted(result['user'].items(), key=lambda x:x[1],reverse=True)
    
    top_2_users = sorted_user_data[:10]
    result['top_users'] = dict(top_2_users)
    result["unique_users_count"] = len(result['user'])
    del result['user']
    print(result)


    
    
    

if __name__ == "__main__":
    filepath = "/Users/upendrakumar/vs_code_projects/interview_test/int_2025/random_log.csv"
    get_analytics(filepath=filepath)    
    
    
    
    
    
    
    
    