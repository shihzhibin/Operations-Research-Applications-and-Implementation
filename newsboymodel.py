# coding=utf-8
'''
:func 可易物報童模型
:author: chiyu
:date: 

'''
import numpy as np
import matplotlib.pyplot as plt


def normalpdf(x, u, v):
    return 1 / (v * np.sqrt(2 * np.pi)) * np.exp(-(x - u) ** 2 / 2 / v**2)



u = 200
v = 30
x = np.arange(u - 1 * u, u + 1 * u, 1)
y = normalpdf(x, u, v)
#y = y / max(y)

# 利润
price = 50
cost = 20
s = 10
vi = 15
bt = np.arange(80,100)
# r = 0.05
# Q0 = 50




# """典型報童最佳訂貨量(均勻分布)"""
# def uni_class_optorder(a, b):
#     return ((price + s - cost)*b + (cost - vi)*a)/(price + s - vi)


# """易貨交換最佳訂貨量(均勻分布)"""
# def uni_optorder(a, b, Q0, r):
#     return ((price+s-cost)*b+(cost-vi)*a + Q0*((1-r)*price-vi))/(price+s-vi)

# # Qc =[uni_class_optorder(0, 100) for Q0 in bt]
# # Qb = [uni_optorder(0, 100, Q0, r) for Q0 in bt]


"""易貨交換最佳訂貨量(常態分布)"""
def class_optorder(Q0):
    
    profitline = [np.sum(np.array([class_profit(Q, d, Q0) for d in x]) * y)for Q in x]
    max_value = np.max(profitline)
    max_indx = np.argmax(profitline)
    
    return max_indx, max_value


"""典型報童利潤"""
def class_profit(Q, d, Q0):
    
    if Q <= d:
        return Q*(price - cost)- s*(d - Q) - Q0*price
    else:
        return d*price + vi*(Q - d) - cost*Q - Q0*price


"""易貨交換最佳訂貨量(常態分布)"""
def optorder(Q0, r):
    
    profitline = [np.sum(np.array([profit(Q, d, Q0, r) for d in x]) * y)for Q in x]
    max_value = np.max(profitline)
    max_indx = np.argmax(profitline)
    
    return max_indx, max_value

"""易貨交換利潤"""
def profit(Q, d, Q0, r):

    if Q <= d:
        return Q*(price - cost)- s*(d - Q) - Q0*price
    
    elif Q >= d and Q <= d + Q0:
        return d*price - cost*Q + r*price*(Q - d)- price*(Q0 - Q + d)
    
    else:
        return d*price - cost*Q - r*price*Q0 + vi*(Q - Q0 - d)


"""不確定性易貨交換最佳訂貨量(常態分布)"""
def u_optorder(Q0, r, wu, wv):
    # wx = np.arange(wu - 1 * wu, wu + 1 * wu, 0.02)
    # wy = normalpdf(wx, wu, wv)
    # wy = wy/max(wy)
    profitline = [np.sum(np.array([uncertainbarter_profit(Q, d, Q0, r, wu) for d in x]) * y) for Q in x]
    max_value = np.max(profitline)
    max_indx = np.argmax(profitline)
    
    return max_indx, max_value


"""不確定性易貨交換利潤"""
def uncertainbarter_profit(Q, d, Q0, r, w):

    if Q <= d:
        return Q*(price - cost)- s*(d - Q) - Q0 * price
    
    elif Q >= d and Q <= d + w*Q0:
        return d*price - cost*Q + r*price*(Q - d)- price*(Q0 - Q + d)
    
    else:
        
        if w>=0 and w<1:
            return d*price - cost*Q - r*price*w*Q0 + vi*(Q - w*Q0 - d) - (1-w)*price*Q0
        else: 
            return d*price  - cost*Q - r*price*Q0 + vi*(Q - Q0 - d)


def orderplot(labal, x_index, Q0, r):

    b_index, b_value = optorder(Q0, r)
    cl_index, cl_value = class_optorder(Q0)
    
    profitline = [np.sum(np.array([profit(Q, d, Q0, r) for d in x]) * y)for Q in x]
    class_profitline = [np.sum(np.array([class_profit(Q, d, Q0) for d in x]) * y)for Q in x]
    
    plt.ylim(-5000, 5000,1000)# 設定y軸繪圖範圍
    # 繪圖並設定線條顏色、寬度、圖例
    line1, = plt.plot(x_index, profitline, color = 'tab:blue', label = 'barter', alpha=0.75)
    show_max1 = '({x},{y})'.format(x=round(b_index, 0), y=round(b_value, 0))
    plt.annotate(show_max1, xy=(b_index, b_value),
            arrowprops=dict(facecolor='tab:blue',shrink=0.05))
    
    line2, = plt.plot(x_index, class_profitline, color='black', label = 'classicl', alpha=1)
    show_max2 = '({x},{y})'.format(x=round(cl_index, 0), y=round(cl_value, 0))
    plt.annotate(show_max2, xy=(cl_index, cl_value),
            arrowprops=dict(facecolor='black',shrink=0.05))


    plt.legend(handles = [line1, line2], loc='upper right')
    plt.xlabel(labal)
    plt.ylabel('Profit')
    plt.show()# 顯示圖


def plot(labal, x_index, opt_inventory, opt_profit, classical_inventory, classical_profit,scale):
    """plot"""
    fig, ax1 = plt.subplots()
    plt.xlabel(labal)
    x_ticks = np.arange(x_index[0],x_index[-1],scale)
    plt.xticks(x_ticks)
    ax2 = ax1.twinx()
    
    ax1.set_ylabel('opt order', color='tab:blue')
    ax1.plot(x_index, opt_inventory, color='tab:blue', alpha=0.75)
    ax1.tick_params(axis='y', labelcolor='tab:blue')
    
    ax2.set_ylabel('Opt profit', color='black')
    ax2.plot(x_index, opt_profit, color='black', alpha=1)
    ax2.tick_params(axis='y', labelcolor='black')
    
    fig.tight_layout()
    plt.show()
    
    # #######################################################
    order_increase = [(opt_inventory[i]-classical_inventory[i])*100/classical_inventory[i] for i in range(len(x_index))]
    profit_increase = [(opt_profit[i]-classical_profit[i])*100/classical_profit[i] for i in range(len(x_index))]
    
    fig, ax1 = plt.subplots()
    plt.xlabel(labal)
    x_ticks = np.arange(x_index[0],x_index[-1],scale)
    plt.xticks(x_ticks)
    ax2 = ax1.twinx()
    
    ax1.set_ylabel('order_increase (%)', color='tab:blue')
    ax1.plot(x_index, order_increase, color='tab:blue', alpha=0.75)
    ax1.tick_params(axis='y', labelcolor='tab:blue')
    
    ax2.set_ylabel('profit_increase (%)', color='black')
    ax2.plot(x_index, profit_increase, color='black', alpha=1)
    ax2.tick_params(axis='y', labelcolor='black')
    
    fig.tight_layout()
    plt.show()


orderplot('Q', x, 50, 0.05)

"""探討隨Q0變化"""

opt_inventory_Q0 = []
opt_profit_Q0 = []

classical_inventory_Q0 = []
classical_profit_Q0 = []

bt = np.arange(80,100,2)
for Q0 in bt:
    
    index, value = optorder(Q0, r=0.05)
    opt_inventory_Q0.append(index)
    opt_profit_Q0.append(value)
    
    index, value = class_optorder(Q0)
    classical_inventory_Q0.append(index)
    classical_profit_Q0.append(value)

plot('Q0', bt , opt_inventory_Q0, opt_profit_Q0, classical_inventory_Q0, classical_profit_Q0,scale = 2)


"""探討隨r變化"""
R = np.arange(0.05,0.16,0.01)

opt_inventory_r = []
opt_profit_r = []
classical_inventory_r = []
classical_profit_r = []

for r in R:
    
    index, value = optorder(Q0=50, r=r)
    opt_inventory_r.append(index)
    opt_profit_r.append(value)
    
    index, value = class_optorder(Q0=50)
    classical_inventory_r.append(index)
    classical_profit_r.append(value)
 
plot('r', R , opt_inventory_r, opt_profit_r, classical_inventory_r, classical_profit_r,scale = 0.01)


"""探討隨w變化"""
W = np.arange(0.1,2,0.1)
opt_inventory_w = []
opt_profit_w = []
classical_inventory_w = []
classical_profit_w = []

for wu in W:
    
    index, value = u_optorder(Q0=50, r=0.05, wu=wu, wv=0.5)
    opt_inventory_w.append(index)
    opt_profit_w.append(value)
    
    index, value = class_optorder(Q0=50)
    classical_inventory_w.append(index)
    classical_profit_w.append(value)
 
plot('w', W , opt_inventory_w, opt_profit_w, classical_inventory_w, classical_profit_w,scale = 0.2)


"""探討隨d變化"""
V = np.arange(30,65,5)
opt_inventory_d = []
opt_profit_d = []
classical_inventory_d = []
classical_profit_d = []

for v in V:
    y = normalpdf(x, u=200, v=v)
    y = y / max(y)
    index, value = optorder(Q0=50, r=0.05)
    opt_inventory_d.append(index)
    opt_profit_d.append(value)
    
    index, value = class_optorder(Q0=50)
    classical_inventory_d.append(index)
    classical_profit_d.append(value)
 
plot('sigma_x', V , opt_inventory_d, opt_profit_d, classical_inventory_d, classical_profit_d,scale = 5)
