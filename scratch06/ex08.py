"""
scipy.stats 모듈에서 제공하는
확률 밀도 함수(PDF: Probability Density Function),
누적 분포 함수(CDF: Cumulative Distribution Function)
"""
import scipy.stats as stats
import matplotlib.pyplot as plt

xs = [x / 10 for x in range(-30,31)] # 그래프를 그릴 x 구간
# 균등 분포(uniform distribution) 확률 밀도 함수(PDF)
ys1 = [stats.uniform.pdf(x) for x in xs]
# 균등 분포 누적 분포 함수(CDF)
ys2 = [stats.uniform.cdf(x) for x in xs]

plt.plot(xs,ys1, color ='blue',label = 'PDF')
plt.plot(xs,ys2, color ='red', label = 'CDF')
plt.legend() # label을 보려면 legend를 꼭 써주어야한다.
plt.title('Uniform Distribution PDF & CDF')
plt.show()


# 평균이 mu = 0이고, 표준 편가 sigma = 1인
# 정규 분포(Normal Distribution) 확률 밀도 함수(PDF)
ys1 = [stats.norm.pdf(x) for x in xs]
# 표준 정규 분포 누적 분포 함수 (CDF)
ys2 = [stats.norm.cdf(x) for x in xs]

plt.plot(xs,ys1, color = 'red', label = 'PDF')
plt.plot(xs,ys2,color = 'blue',label = 'CDF')
plt.legend()
plt.title('Standard Normal Distribution PDF & CDF')
plt.show()