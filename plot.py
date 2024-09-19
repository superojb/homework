import matplotlib.pyplot as plt
import csv
import matplotlib

matplotlib.rcParams['font.family'] = 'Microsoft YaHei'
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
        # print(f"地点: {location}, 温度: {temperature}°C")
        print(data)
        
        
# 提取地点和温度
locations, temperatures = zip(*data)

# 创建图形和坐标轴
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制温度数据的条形图
ax.bar(locations, temperatures, color='skyblue')

# 设置图表标题和标签
ax.set_title('各地点的温度', fontsize=16)
ax.set_xlabel('地点', fontsize=14)
ax.set_ylabel('温度 (°C)', fontsize=14)

# 旋转 x 轴标签以避免重叠
ax.set_xticklabels(locations, rotation=45, ha='right', fontsize=12)

# 自动调整布局以适应标签
plt.tight_layout()

# 显示图表
plt.show()