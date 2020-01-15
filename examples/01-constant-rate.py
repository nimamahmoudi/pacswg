import requests
import time
import pacswg
import pandas as pd

site_url = 'https://nima-dev.com/'

# the worker function should return a dict with each item having a single value
# return any value you want to keep track of in the dictionary
def worker_func():
    client_start_time = time.time() # current timestamp
    resp = requests.get(site_url)
    client_end_time = time.time() # current timestamp
    resp_len = len(resp.content)
    resp_millis = resp.elapsed.microseconds / 1000
    return {
        'resp_len': resp_len,
        'resp_millis': resp_millis,
        'client_start_time': client_start_time,
        'client_end_time': client_end_time,
    }

# Test the worker function
print(worker_func())

# Create the PACS Workload Generator
wg = pacswg.WorkloadGenerator(worker_func=worker_func, delay_func=lambda x: 1/x, 
                        rps=3, worker_thread_count=100)

wg.start_workers()
wg.prepare_test()

timer = pacswg.TimerClass()

# reset the timer
timer.tic()
while timer.toc() < 10:
    wg.fire_wait()
wg.stop_workers()

# Get the results from the workers
res = wg.get_stats()
print('Number of requests:', len(res))
df_res = pd.DataFrame(data=res)

# print the pandas dataframe
print(df_res.head())

# Output:
# {'resp_len': 53020, 'resp_millis': 122.752, 'client_start_time': 1579129304.3390362, 'client_end_time': 1579129304.4707813}
# Number of requests: 30
#    resp_len  resp_millis  client_start_time  client_end_time
# 0     53020      119.270       1.579129e+09     1.579129e+09
# 1     53020      125.307       1.579129e+09     1.579129e+09
# 2     53020      120.665       1.579129e+09     1.579129e+09
# 3     53020      141.177       1.579129e+09     1.579129e+09
# 4     53020      132.713       1.579129e+09     1.579129e+09
