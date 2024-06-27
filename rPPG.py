import numpy as np
import matplotlib.pyplot as plt
import heartpy as hp

#load example PPG signal
# 0 : a short, very clean PPG signal, sampled at 100.0 Hz
# 1 : a slightly longer (~2 minute) PPG signal, with missing signal in first third, and random noise spikes in rest of signal
# 2 : a long (~11.5 minute) PPG signal recorded 'in the wild' while driving in a driving simulator using a Pulse Sensor on the index finger and an Arduino
# ppg_signal, timer = hp.load_exampledata(1)

# 加载PPG信号数据
# 将'ppg_signal.csv'替换为你的实际PPG信号文件路径
# import heartpy as hp
# ppg_signal = np.loadtxt('ppg_signal.csv', delimiter=',')

ppg_signal = np.loadtxt(r'D:\BaiduSyncdisk\港科学业\实验室事物\实验研究\1.PhD主线-健康感知课题\高光谱\rPPG_健康感知\rPPG_code\demo1_timestamp.txt')
# print(ppg_signal.shape)

plt.figure(figsize=(12,4))
plt.plot(ppg_signal)
plt.show()

#=======================================# 





# 使用HeartPy处理PPG信号
# wd: 处理后的数据
# m: 提取的心率变异性指标
wd, m = hp.process(ppg_signal, sample_rate=100.0)

# 绘制PPG信号
plt.figure(figsize=(12, 4))
plt.plot(ppg_signal, label='PPG Signal')
plt.title('PPG Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.show()

# 绘制HeartPy分析结果
hp.plotter(wd, m)

# 打印测量指标
for measure in m.keys():
    print('%s: %f' %(measure, m[measure]))
    
# beats per minute, BPM
# interbeat interval, IBI
# standard deviation if intervals between adjacent beats, SDNN
# standard deviation of successive differences between adjacent R-R intervals, SDSD
# root mean square of successive differences between adjacend R-R intervals, RMSSD
# proportion of differences between R-R intervals greater than 20ms, 50ms, pNN20, pNN50
# median absolute deviation, MAD
# Poincare analysis (SD1, SD2, S, SD1/SD2)
# Poincare plotting

