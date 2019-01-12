import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel('data.xls')
data.head()

Q = data.values[:, 0:]

def FCM(observations, clusters=3, tol=1e-3, max_iter=25):
    
    u = np.random.uniform(low=0, high=1, size=(observations.shape[0], clusters))
    centers = np.zeros((clusters, observations.shape[1]))
    
    def update_centers(observations, u, centers, power=1):
        rows, cols = u.shape
        for j in range(cols):
            c_j = observations[0, :] * np.power(u[0, j], power)
            for i in range(1, rows):
                c_j += observations[i, :] * np.power(u[i, j], power)
                
            c_j /= np.sum(np.power(u[:, j], power))
            
            centers[j, :] = c_j
        
        return centers
    
    def update_mf_matrix(observations, u, centers, power=1):
        classes = np.zeros(observations.shape[0])
        rows, cols = u.shape
        for i in range(rows):
            for j in range(cols):
                x = observations[i, :]
                c_i = centers[j, :]
                
                over_part = np.linalg.norm(x - c_i)
                
                result = 0
                for k in range(clusters):
                    c_k = centers[k, :]
                    
                    add = over_part / np.linalg.norm(x - c_k)
                    add = np.power(add, power)
                    result += add
                
                u[i, j] = 1 / result
                
            classes[i] = np.argmax(u[i, :])
            
        return u, classes
    
    def loss(observations, u, centers, power=1):
        rows, cols = u.shape
        _loss = 0
        for i in range(rows):
            for j in range(cols):
                x = observations[i, :]
                c = centers[j, :]
                l = np.power(u[i, j], power) * np.linalg.norm(x - c) ** 2
                
                _loss += l
                
        return _loss
    
    err = 1
    iteration = 1
    
    errors = [loss(observations, u, centers, power=0)]
    
    while err > tol and iteration < max_iter:

        centers = update_centers(observations, u, centers, power=iteration)
        u, classes = update_mf_matrix(observations, u, centers, power=2 / (iteration))
        l = loss(observations, u, centers, power=iteration)
        
        errors.append(l)
        
        err = np.abs(l)
        iteration += 1
    
    errors = np.array(errors)
    
    return classes, centers, u, errors
    
def plot_FCM_results(data, max_clusters=4):
    
    fig, axs = plt.subplots(nrows=np.int(max_clusters / 2), ncols=2)
    fig.set_figwidth(16)
    fig.set_figheight(8 * max_clusters // 2)
    
    mfs = []
    
    for clusters, ax in zip(range(1, max_clusters + 1), axs.flatten()):
        classes, centers, u, errors = FCM(data, clusters=clusters, tol=1e-5, max_iter=100)
        
        mfs.append((clusters, u))
        
        for cluster in range(clusters):
            cluster_data = data[np.where(classes == cluster), :][0]
            ax.plot(cluster_data[:, 0], cluster_data[:, 1], 'o', label='Cluster {}'.format(cluster + 1))
        ax.legend()
        ax.grid()
    
#     plt.show()
    
    return mfs

mfs = plot_FCM_results(Q, max_clusters=8)
P1 = data.values[:, 0]
P2 = data.values[:, 1]
CL1, CL2 = mfs[1][1][:, 0], mfs[1][1][:, 1]

from sklearn.ensemble import RandomForestRegressor

regr = RandomForestRegressor()
data_input = np.column_stack((P1, P2))
data_output = np.column_stack((CL1, CL2))
regr = regr.fit(data_input, data_output)

min_1, min_2, max_1, max_2 = np.min(P1), np.min(P2), np.max(P1), np.max(P2)

P1_in = np.linspace(min_1, max_1, num=50)
P2_in = np.linspace(min_2, max_2, num=50)
P_in = np.column_stack((P1_in, P2_in))

output = regr.predict(P_in)
CL1_out, CL2_out = output[:, 0], output[:, 1]

P1, P2 = np.meshgrid(P1_in, P2_in)
CL1, CL2 = np.meshgrid(CL1_out, CL2_out)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

axs = Axes3D(plt.figure(figsize=(13, 8)))
axs.plot_surface(P1, P2, CL1)
axs.plot_surface(P1, P2, CL2)
axs.set_xlabel('среднее Q за янв /среднее Q за год')
axs.set_ylabel('среднее Q за июль/среднее Q за год')
axs.set_zlabel('Степень истинности')
plt.show()