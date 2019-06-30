import numpy as np
import json
result_json = '/home/fengzicai/Documents/predict/val_400_100_100_(1)/val_stastic.pkl.json'
with open(result_json, 'r') as f:
    result_data = json.load(f)
count = []
for i in result_data:
    count.append(i['image_id'])
np.savetxt('/home/fengzicai/Documents/predict/val_400_100_100_(1)/count.txt', np.array(list(set(count))).reshape(-1, 1), fmt='%s')
