from decimal import *
import math
import time
from sklearn.linear_model import LinearRegression
import numpy as np
from tqdm import tqdm
import subprocess




subprocess.Popen(["open.exe"])
time.sleep(7)
print(' ___________________________________')
print('|             各取所需              |')
print('| Start the CPU   | Start the GPU   |')
print('|   benchmark     |   benchmark     |')
print('|                 |                 |')
print('|  Enter start --f|  Enter start --e|')
print('|_________________|_________________|')
print('Press the window close button to exit')
while True:
    o = input()
    if o =='start --f':
        print('It is ready, please make sure the heat dissipation and power supply of the equipment is normal')
        print('\033[91m' + 'Warning: Devices with abnormal or poor performance, power supply, heat dissipation, and other indicators should be operated with caution, resulting in adverse consequences. This program and its authors are not responsible for any responsibility.\n警告：设备性能异常或较差，电源、散热等指标应谨慎操作，否则会造成不良后果。本程序及其作者不承担任何责任。' + '\033[0m')
        print('\033[95m' + 'Warning: Please visit before use https://space.bilibili.com/1178334264 Read relevant program instructions videos for instructions on how to use them\n警告：请在使用前访问 https://space.bilibili.com/1178334264 阅读相关程序说明视频以获取有关如何使用它们的说明' + '\nThen enter sure to run' + '\033[0m')
        s = input()
        if s == 'sure':
            getcontext().prec = 14210  # 将精度设置为10000

            time_each = []
            start_time = time.time()

            def calc_pi():
                pi = Decimal(0)
                k = 0
                pbar = tqdm(total=14210)  # 创建进度条
                while True:
                    if k == 14210:
                        break
                    pi += (Decimal(1) / 16**k) * (
                        Decimal(4) / (8*k+1) -
                        Decimal(2) / (8*k+4) -
                        Decimal(1) / (8*k+5) -
                        Decimal(1) / (8*k+6)
                    )
                    k += 1
                    end_time = time.time()
                    time_each.append(end_time - start_time)
                    pbar.update(1)
                pbar.close()
                return pi

            pi = calc_pi()
            end_time = time.time()
            time_all = end_time - start_time

            X = np.array(range(len(time_each))).reshape(-1, 1)
            y = np.array(time_each)

            model = LinearRegression()
            model.fit(X, y)

            result = model.predict(np.array([[1000000]]))
            #print("计算到第1000000位所需的时间预测值：", result[0])
            #____________
            getcontext().prec = 10000000  # 将精度设置为 1000000

            start_time = time.time()
            time_each = []
            results = []

            i = 1
            pbar = tqdm(total=34210)  # 创建进度条
            while True:
                if i == 34210:
                    break
                a = Decimal(str(i))
                b = Decimal(str(i + 1))
                result_1 = a + b
                results.append(result_1)
                end_time = time.time()
                time_each.append(end_time - start_time)
                pbar.update(1)
                i += 1
            pbar.close()

            X = np.array(range(len(time_each))).reshape(-1, 1)
            y = np.array(time_each)

            model = LinearRegression()
            model.fit(X, y)

            result_1 = model.predict(np.array([[1000000000]]))
            result_1[0]=int(result_1[0])
            result[0] = int(result[0])
            #print("预测计算到第 1000000 位所需的时间: ", result_1[0])
            while True:

                if result[0]>=10000:
                    result[0]=result[0]*0.9#也可以用还原所需次数判定分数
                elif 0<=result[0]<=10000:
                    break
            num = result[0]
            if 0 < num < 10000 and num:
                num_1 = 10000 - num

            elif num == 0:
                num_1 = 10000

            elif num >= 10000:
                num_1 = 0
            num = result_1[0]
            if 0 < num < 10000 and num:
                num_2 = 10000 - num

            elif num == 0:
                num_2 = 10000

            elif num >= 10000:
                num_2 = 0
            lastresult = int(num_1+num_2)
            num_1 = int(num_1)
            num_2 = int(num_2)
            print('\033[92m'+'The single-core benchmark score is:'+str(num_1)+'\033[0m'+'The better score:↑')
            print('\033[92m' + 'The multicore benchmark score is:' + str(num_2) + '\033[0m'+'The better score:↑')
            print('\033[92m' + 'The composite CPU benchmark score is:' + str(lastresult) + '\033[0m'+'The better score:↑')



        else:
            print('\033[91m' +'invalid instruction'+ '\033[0m')
    elif o == 'start --e':

        print('It is ready, please make sure the heat dissipation and power supply of the equipment is normal')
        print('\033[91m' + 'Warning: Devices with abnormal or poor performance, power supply, heat dissipation, and other indicators should be operated with caution, resulting in adverse consequences. This program and its authors are not responsible for any responsibility.\n警告：设备性能异常或较差，电源、散热等指标应谨慎操作，否则会造成不良后果。本程序及其作者不承担任何责任' + '\033[0m')
        print("\033[31mWarning: This test carries a risk of developing photosensitive epilepsy. Please take responsibility for any serious consequences caused\n警告：该测试有发生光敏性癫痫的风险。由此造成的严重后果请您自行承担\033[0m")
        print('\033[95m' + 'Warning: Please visit before use https://space.bilibili.com/1178334264 Read relevant program instructions videos for instructions on how to use them\n警告：请在使用前访问 https://space.bilibili.com/1178334264 阅读相关程序说明视频以获取有关如何使用它们的说明'+'\nThen enter sure to run' + '\033[0m')
        d = input()
        if d == 'sure':
            subprocess.Popen(["count.exe"])

            print('wait about 30 seconds and then exit...')
            start_time = time.time()

            while True:


                # 每次循环时计算当前时间与程序开始时间的差值
                current_time = time.time()
                elapsed_time = current_time - start_time


                # 检查是否已经达到30秒
                if elapsed_time >= 30:
                    break


                # 执行程序运行命令，并将stdout和stderr重定向到日志文件中
                with open("log.txt", "a") as logfile:
                    subprocess.run("windows.exe", stdout=logfile, stderr=logfile)

                # 等待一定时间再次循环，这里的时间可以根据需要进行调整
                time.sleep(1)
                fpslist = []

                with open("fps.txt", "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if not line:  # 如果读取到的行为空，则跳过
                            continue
                        try:
                            fps = float(line)
                            fpslist.append(fps)
                        except ValueError:
                            print(f"Invalid FPS value: {line}")

                themax = max(fpslist)
                themin = min(fpslist)
                difference = themax - themin
                mean_fps = sum(fpslist)/len(fpslist)
                resultfps = 10000-mean_fps+difference
                print('\033[92m' + 'The composite GPU benchmark score is:' + str(int(resultfps)) + '\033[0m' + 'The better score:↓')

        else:
            print('\033[91m' + 'invalid instruction'  + '\033[0m')

    else:
        print('\033[91m' + 'invalid instruction' + '\033[0m')


