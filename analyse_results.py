import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
plt.rcParams.update({'font.size':16})
plt.figure(figsize=(7,6))

D = 1
L_range = range(21)
intercept = 0.01
slope_range = np.round(np.arange(0.01,0.11,0.01),2)
colors = cm.Reds(np.linspace(1., 0.3, len(slope_range)))
for i in range(len(slope_range)):
    slope = slope_range[i]
    lifetimes = np.load("/home/uttam/Dropbox/c/smart_forager/continuum_forager/results/D="+str(D)+"/lifetimes_L"+str(min(L_range))+"-"+str(max(L_range))+"_metabolism_slope="+str(slope).replace(".","p")+"_intercept_"+str(intercept).replace(".","p")+".npy")
    if i==0 or i==len(slope_range)-1:
        plt.scatter(L_range,np.mean(lifetimes,axis=1),s=50,label="Slope = "+str(slope),c=colors[i])
    else:
        plt.scatter(L_range,np.mean(lifetimes,axis=1),s=50,c=colors[i])
    plt.errorbar(L_range,np.mean(lifetimes,axis=1),np.std(lifetimes,axis=1)/np.sqrt(lifetimes.shape[1]),c=colors[i])



plt.xlabel("Detection range")
plt.ylabel("Average lifespan")
plt.yscale('log')
plt.legend()
plt.show()







