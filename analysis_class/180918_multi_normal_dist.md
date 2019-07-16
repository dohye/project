
## 다변량 정규분포

<img src="https://latex.codecogs.com/svg.latex?\Large&space;p"> - 차원 확률벡터 <img src="https://latex.codecogs.com/svg.latex?\Large&space;\mathbf{X}"> 가 평균이 <img src="https://latex.codecogs.com/svg.latex?\Large&space;\mu"> 이고 공분산이 <img src="https://latex.codecogs.com/svg.latex?\Large&space;\Sigma">인 다변량 정규분포를 따를 때, 확률밀도함수 <img src="https://latex.codecogs.com/svg.latex?\Large&space;f(x)">는 아래와 같다.


![12](https://user-images.githubusercontent.com/37234822/60961741-cdaa3400-a347-11e9-90f1-3f684402b36d.JPG)

### Example

![13](https://user-images.githubusercontent.com/37234822/60961744-cdaa3400-a347-11e9-9762-98043e165f72.JPG)
----------------------------

<br/>

### multivariate normal distribution in python

>**Contour Plot**

```{python}
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
  
mu = [1, 2]
cov = [[2, 1],[1, 2]]
rv = stats.multivariate_normal(mu, cov) # 다변량 정규분포를 따르는 난수 생성
  
# Create grid
x = np.linspace(-2, 4, 100) # -2부터 4를 100개의 구간으로 나누기
y = np.linspace(-1, 5, 100) # x.shape : (100,) / y.shape : (100,)
X, Y = np.meshgrid(x,y) # X.shape : (100, 100) / Y.shape : (100, 100)
  
# Make a contour plot  
plt.grid(False) # grid 제거
plt.contourf(X, Y, rv.pdf(np.dstack([X,Y]))) # contourf : 3차원 자료 시각화(color)
# np.dstack : 제3의 축(깊이) 방향으로 배열을 합친다. -> 차원 추가 
# np.dstack([X,Y]).shape : (100, 100, 2)
plt.show()
  
```
![contour plot](https://user-images.githubusercontent.com/37234822/60961923-1bbf3780-a348-11e9-8fb1-9260078fb49d.png)


<br/>
<br/>
<br/>

>**3D Surface Plot**
```{python}
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
  
mu = [1, 2]
cov = [[2, 1],[1, 2]]
rv = stats.multivariate_normal(mu,cov)
  
# Create grid 
x = np.linspace(-2,4,500)
y = np.linspace(-1,5,500) # x.shape : (500,) / y.shape : (500,)
X, Y = np.meshgrid(x,y) # X.shape : (500, 500) / Y.shape : (500, 500)
  
# Make a surface plot
fig = plt.figure()
ax = fig.gca(projection='3d') # 좌표를 3d로 지정
ax.plot_surface(X, Y, rv.pdf(np.dstack([X, Y])),cmap='viridis',linewidth=0) #surface flot
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
```

![3dplot](https://user-images.githubusercontent.com/37234822/60961921-1b26a100-a348-11e9-8a94-f1393ad340a8.png)
