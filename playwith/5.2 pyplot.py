# import matplotlib.pyplot as plt

# plt.plot([3,4,7,6,2,8,9])
# plt.savefig('test')

# import matplotlib.pyplot as plt
# import numpy as np

# t = np.arange(0.,4.,0.1)
# plt.bar(t,t**2)
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
  
# x = np.linspace(0, 1)
# y = np.sin(4 * np.pi * x) * np.exp(-5 * x)
# plt.title('The graph')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.plot(x, y,'r--')
# plt.show()

x = np.linspace(-np.pi,np.pi,300)
# plt.figure(1)
# plt.subplot(211)
# plt.plot(x,np.sin(x),'r')
# plt.subplot(212)
# plt.plot(x,np.cos(x),'g')
# plt.show()

fig,(ax0,ax1) = plt.subplots(2,1)
ax0.plot(x,np.sin(x),'r')
ax0.set_title('subplots1')
plt.subplots_adjust(hspace=0.5)
ax1.plot(x,np.cos(x),'g')
ax1.set_title('subplots2')
plt.show()

