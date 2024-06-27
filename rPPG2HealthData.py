import numpy as np
import matplotlib.pyplot as plt
import rPPG_Process 



# 加载PPG信号数据

ppg_signal = np.loadtxt(r'.\demo1rppg.txt')
# print(ppg_signal.shape)


# 打印数据的形状和内容
# print("数据大小:", ppg_signal.shape)
# print("数据内容:", ppg_signal)

# import heartpy as hp
# ppg_signal, timer = hp.load_exampledata(1)

# 绘制PPG信号
plt.figure(figsize=(12, 4))
plt.plot(ppg_signal, label='PPG Signal')
plt.title('PPG Signal from demo1_timestamp.txt')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.show()


# 处理PPG信号
wd, m = rPPG_Process.process(ppg_signal, sample_rate=40.0)


# 打印心率变异性指标
for measure in m.keys():
    print(f'{measure}: {m[measure]:.2f}')

# 处理心率数据
