import random
import datetime

# Parameters
num_records = 100_000
file_name = "random_log.csv"
actions = ['login', 'click', 'logout', 'purchase']

# Generate log data
with open(file_name, 'w') as f:
    f.write("timestamp,user_id,action\n")  # header
    for _ in range(num_records):
        timestamp = datetime.datetime.utcnow().isoformat() + 'Z'
        user_id = random.randint(10000, 99999)
        action = random.choice(actions)
        f.write(f"{timestamp},{user_id},{action}\n")

print(f"Log file '{file_name}' with {num_records} records generated successfully.")

 