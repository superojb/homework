import matplotlib.pyplot as plt
import csv

data = []

with open('latest_1min_temperature_uc.csv', newline='', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')

    next(spamreader)
    
    # 遍历每一行数据
    for row in spamreader:
        # 跳过空行
        if not row:
            continue
        
        # 读取中间的地点和后面的温度
        location = row[1]  # 第二列是地点
        temperature = float(row[2])  # 第三列是温度，转换为浮点数
        
        # 将数据添加到列表中
        data.append((location, temperature))
        
        # 打印地点和温度
        print(f"地点: {location}, 温度: {temperature}°C")