# Operations-Research-Applications-and-Implementation 
### Theme: The newsvendor problem with barter exchange 

### **Team Member**    

| 編輯者       |    暱稱         |                      LinkedIn                                                            |
| :-----------:|:-----------:   |:---------------------------------------------------------------------------------------: |
|  洪志宇      | CHI-YU HONG     | [https://www.linkedin.com/in/chiyuhong/](https://www.linkedin.com/in/chiyuhong/)     
|  施智臏      | ZHI-BIN SHIH     | [https://www.linkedin.com/in/zhibin-shih-9a0a711a9/](https://www.linkedin.com/in/zhibin-shih-9a0a711a9/)     


## Tutorial of the newsvendor problem with barter exchange  
<details open="open">
  <summary><b>Table of Contents</b></summary>
  <ol>
    <li>
      <a href="#introduction">Introduction</a>
      <ul>
        <li><a href="#the-barter-exchange">The Barter Exchange</a></li>
    </li>
      </ul>
    <li>
      <a href="#the-model">The Model</a>
      <ul>
        <li><a href="#python-and-gurobi-implementation">Python and Gurobi Implementation</a></li>
        <li><a href="#parameter-setting">Parameter Setting</a></li>
        <li><a href="#the-classical-newsvendor-model-with-consumption">The Classical Newsvendor Model with Consumption</a></li>
        <li><a href="#the-newsvendor-model-with-barter-exchange">The Newsvendor Model with Barter Exchange</a></li>
        <ul>
          <li><a href="#the-newsvendor-model-with-barter-exchange-demand-uncertainty">The Newsvendor Model with Barter Exchange: Demand uncertainty</a></li>
        </ul>
      </ul>
    </li>
    <li><a href="#visualization">Visualization</a></li>
    <li><a href="#conclusion">Conclusion</a></li>
  </ol>
</details>

# __Introduction__
This repository is a tutorial for the implementation of __The newsvendor problem with barter exchange__ based on the design of the paper _"The newsvendor problem with barter exchange"_  by [Hua, G., Zhang, Y., Chang, T.C.E, Wang, S., & Zhang, J. (2020)]("https://www.sciencedirect.com/science/article/abs/pii/S0925527313001837?via%3Dihub"). I wrote this tutorial as a showcase of application for the course "_Operations Research Applications and Implementation_" intructed by professor _Chia-Yen Lee_.  
## __The Barter Exchange__
> The barter exchange is an alternative to move distressed inventory, it has become increasingly popular in business. Many companies barter their unsold product for the product they need via barter exchange platforms at full prices.  
__There are two basic types of barter:__  
(1) Personal barter and retail barter  
(2) Commercial barter    
> We only focus on the __commercial barter__ in this tutorial  
> __The trade sequence is as follows:__  
> __Step 1:__  
> `Firm A` registers on a barter exchange platform and provides some essential information, the broker of the platform will help `Firm A` to find `Firm B` that exactly needs the product of `Firm A` and that provides the product that `Firm A` exactly needs.  
> __Step 2:__  
> `Firm A` and `Firm B` can trade their product `without money`, and pay the broker a commission  that typically is about `5% - 15%` of the trade value.  
> 
> __The aim of the barter is to maintain trade volumes and balance them while maximizing the utility of the participants.__  
# __The Model__
* We consider the `single-period` inventory (newsvendor) problem with barter exchange from the retailer's perspective, in which the customer's demand is `stochastic` and characterized by a `random variable`. The retailer determines the optimal stocking policy to satisfy the customer demand at the beginning of the selling season.  
* Suppose the retailer purchases only a single product A from the supplier, and the retail price is set by the supplier or the market. This problem is to decide the optimal order quantity to `maximize its own expected profit`.  
* The retailer orders `Q units of the product A` from the supplier at a `fixed price` at the beginning of the selling season, then it sells product A to its customers at the `retail price`.  
* There are three cases of the retailer's profit:  
(1) If customer demand is `greater than` Q, then it will pay `the shortage penalty cost` for the unsatisfied demand  
(2) If customer demand is `less than` Q, the retailer will trade the unsold product A for the product it needs on a barter platform  
(3) If there are still some `unsold product A` after barter exchange, the retailer will dispose of them at a very low price  
 *  The notation used in this tutorial is as follows:    
<table>
  <tr>
    <td>Notation</td>
    <td>Description</td>
  </tr>
  <tr>
    <td>x</td>
    <td>Stochastic demand, a random variable</td>
  </tr>
  <tr>
    <td>f(x)</td>
    <td>The probability density function of x</td>
  </tr>
  <tr>
    <td>F(x)</td>
    <td>The cumulative distribution function of x</td>
  </tr>
  <tr>
    <td>c</td>
    <td>The supplier's wholesale price</td>
  </tr>
  <tr>
    <td>p</td>
    <td>The retailing price per unit (p > c)</td>
  </tr>
  <tr>
    <td>v</td>
    <td>The salvage value per unit (v < c)</td>
  </tr>
  <tr>
    <td>s</td>
    <td>The shortage penalty cost per unit</td>
  </tr>
  <tr>
    <td>Q</td>
    <td>The order quantity, a decision variable</td>
  </tr>
  <tr>
    <td>Q_0</td>
    <td>The value of the product the retailer needs on the barter platform is equal to the value of Q0 units of the product that the retailer sells</td>
  </tr>
  <tr>
    <td>Q_c*</td>
    <td>The optimal order quantity in the classical newsvendor model</td>
  </tr>
  <tr>
    <td>Q*</td>
    <td>The optimal order quantity in the newsvendor model with barter</td>
  </tr>
  <tr>
    <td>r</td>
    <td>The retailer pays r percent of retail price to the barter platform as the commission of per unit product</td>
  </tr>
  <tr>
    <td>π(Q,x)</td>
    <td>The total profit if the order size is Q units and the customer demand is x</td>
  </tr>
</table>

## __Python and Gurobi Implementation__
```python 
#Download package
import numpy as np
import matplotlib.pyplot as plt
from IPython.html.widgets import interact
%pylab inline

#probability density function
def normalpdf(x, u, v):
    return 1 / (v * np.sqrt(2 * np.pi)) * np.exp(-(x - u) ** 2 / 2 / v**2)
```
## __Parameter Setting__
```python 
#parameter
u = 200  # 均值
v = 30   # 標準差
x = np.arange(u - 1 * u, u + 1 * u, 1)
y = normalpdf(x, u, v)   #需求服從常態  
price = 50  #售價  
cost = 20   #成本
s = 10      #短缺成本
vi = 15     #殘值
```
## __The Classical Newsvendor Model with Consumption__  
In this section, we incorporate the retailer's consumption into the model.  
The __retailer's profit per period__ is  
<p style="text-align:center">
  <img src="./Formula/retailer's profit.png"/>
</p>

```python
"""典型報童利潤"""
def class_profit(Q, d, Q0):
    
    if Q <= d:
        return Q*(price - cost)- s*(d - Q) - Q0*price
    else:
        return d*price + vi*(Q - d) - cost*Q - Q0*price
```
The __retailer's expected profit__ is  
<p style="text-align:center">
  <img src="./Formula/retailer's expected profit.png"/>
</p>

```python
"""典型易貨交換最佳訂貨量(常態分布)"""
def class_optorder(Q0):
    
    profitline = [np.sum(np.array([class_profit(Q, d, Q0) for d in x]) * y)for Q in x]
    max_value = np.max(profitline)
    max_indx = np.argmax(profitline)
    
    return max_indx, max_value
```
The __retailer's optimal order quantity__ satisfies the following equation:  `F(Q_c*)=(p+s-c)/(p+s-v)` 


## __The Newsvendor Model with Barter Exchange__  
In this part, we are going to discuss the retailer's profits for the following three cases:  

__Case 1.__ Q≤x (The retailer's order quantity Q is less than the customer demand x)  
In this case, the retailer pays `the shortage penalty cost s` for `the unsatisfied demand`    
The retailer's profit `π(Q,x) = (p-c)Q-s(x-Q)-pQ_0`  

__Case 2.__ x<Q≤x+Q_0  
In this case, since the order quantity Q is greater than the customer demand x, there are Q-x units of the product are unsold. Therefore, the retailer trades Q-x units of the product A for those the retailer needs on the barter exchange platform, pays `the commission rp(Q-x)`, and buys product from the market , whose value equals to `Q_0-(Q-x)` units of the product A  
The retailer's profit `π(Q,x) = px-rp(Q-x)-p(Q_0-Q+x)-cQ`  

__Case 3.__ Q>x+Q_0    
In this case, the retailer barters its product A for all the product it needs at the cost of `the commission rpQ_0` and disposes of the rest the product at v  
The retailer's profit `π(Q,x) = px-rpQ_0+v(Q-Q_0-x)-cQ`  

Schematic diagram as shown below: `Red candlesticks` indicate `demand` and `Yellow candlesticks` indicate `order quantity`
<p style="text-align:center">
  <img src="./power point/candle plot.PNG"/>
</p>


To sum up the above three cases, we have    
<p style="text-align:center">
  <img src="./Formula/retailer's profit of the three cases.png"/>
</p>

```python
"""易貨交換利潤"""
def profit(Q, d, Q0, r):
    if Q <= d:
        return Q*(price - cost)- s*(d - Q) - Q0*price
    
    elif Q >= d and Q <= d + Q0:
        return d*price - cost*Q + r*price*(Q - d)- price*(Q0 - Q + d)
    
    else:
        return d*price - cost*Q - r*price*Q0 + vi*(Q - Q0 - d)
```

### __The Newsvendor Model with Barter Exchange Expected Order Quantity__

```python
"""易貨交換最佳訂貨量(常態分布)"""
def optorder(Q0, r):
    
    profitline = [np.sum(np.array([profit(Q, d, Q0, r) for d in x]) * y)for Q in x]
    max_value = np.max(profitline)
    max_indx = np.argmax(profitline)
    
    return max_indx, max_value
```

### __The Newsvendor Model with Barter Exchange: Demand uncertainty__

`w` ~ N(uw,σw) -> The barter supply is characterized by wQ0, w is random with mean uw and variance of σw. g(w) is the probability density function of w.

We present the retailer’s profits for the following two cases, namely the barter supply is lower than the barter demand (0 ≤ w ≤ 1) and supply is higher than the barter demand (w > 1).


__Case 1.__: 0 ≤ w ≤ 1

(1)When Q ≤ x, i.e., the retailer’s order quantity Q is less than the customer demand x, the retailer pays the shortage penalty costs for the unsatisfied demand, 
So the retailer’s profit is  `πu(Q,x) = (p-c)Q-s(x-Q)-pQ0`.

(2)When x < Q ≤ x + wQ0 since the order quantity Q is greater than the customer demand x, Q − x units of the product are unsold. The retailer trades Q − x units of the product A, pays the commission rp(Q − x), and buys Q0 − Q + x units of the product A from the market. So the retailer’s profit is  `πu(Q,x) = px-rp(Q-x)-p(Q0-Q+x)-cQ`

(3)When Q > x + wQ0, the retailer barters its product A for all the product it needs at the cost of the commission rpwQ0, buys (1 − w)Q0 units of the product A from the market, and disposes of the rest the product A at v. So the retailer’s profit is `πu(Q,x) = px-rpwQ0+v(Q-wQ0-x)-cQ-(1-w)pQ0`

__Case 2.__: w > 1

(4)When Q ≤ x, i.e., the retailer’s order quantity Q is less than the customer demand x, the retailer pays the shortage penalty costs for the unsatisfied demand, 
So the retailer’s profit is `πu(Q,x) = (p-c)Q-s(x-Q)-pQ0`

(5)When x < Q ≤ x + Q0, since the order quantity Q is greater than the customer demand x, Q − x units of products are unsold.Supply is wQ0 and all the unsold products can be traded on the platform. Then the retailer buys Q0 − Q + x units of the product A, trades Q − x units on the platform.
So the retailer’s profit is `πu(Q,x) = px-rp(Q-x)-p(Q0-Q+x)-cQ`

(6)When Q > x + Q0, since the order quantity Q is greater than the customer demand x, the supply is wQ0, then Q − x units of the product are unsold and can be traded on the platform. So the retailer’s profit is. So the retailer’s profit is `πu(Q,x) = px-rpQ0+v(Q-Q0-x)-cQ`

```python
"""不確定性易貨交換利潤計算公式 case by case"""
def uncertainbarter_profit(Q, d, Q0, r, w):

    if Q <= d:
        return Q*(price - cost)- s*(d - Q) - Q0 * price
    
    elif Q > d and Q <= d + w*Q0:
        return d*price - cost*Q - r*price*(Q - d)- price*(Q0 - Q + d)
    
    else:
        
        if w>=0 and w<1:
            return d*price - cost*Q - r*price*w*Q0 + vi*(Q - w*Q0 - d) - (1-w)*price*Q0
        else: 
            return d*price  - cost*Q - r*price*Q0 + vi*(Q - Q0 - d)
```

__The Newsvendor Model with the uncertainty (Expected Order Quantity)__

```python
"""The expected value of πu(Qu, x) gives the retailer’s expected profit"""
def u_optorder(Q0, r, wu, wv):
    
    wy = normalpdf(x, wu, wv)
    profitline = [np.sum(np.array([np.sum(np.array([uncertainbarter_profit(Q, d, Q0, r, w) for d in x]) * y)for w in x])*wy) for Q in x]
    max_value = np.max(profitline)
    max_indx = np.argmax(profitline)
    
    return max_indx, max_value
```

<p style="text-align:center">
  <center>Classical model vs Barter exchange model</center>
  <img src="./Experiment plot/Comparison.png" width="400" height="300"/>
</p>

# __Visualization__  
We conduct the __sensitivity analysis__ to examine the `demand uncertainty` on the newsvendor's decisions and profit. Taking the first derivative of `r` and `Q_0` in __Theorem 1__, the retailer's order quantity and profit `decreases` with barter commission, while the order quantity `increases` and profit `decreases` with the value of the product that the retailer will buy. In addition, the profitability of barter `increases` with barter commission and `decreases` with the value of the product that the retailer will buy. The following is the sensitivity analyses of `demand uncertainty`.  

__Theorem 1__, The retailer’s optimal order quantity `Q∗` satisfies`(rp + s)F (Q∗ ) + [(1 − r)p − v]F (Q∗ − Q0) = p + s − c`.

--------------------------------------------------------------------------------------------------------------------------------------------------------------

__Precautions: Fig 2 、 Fig 4 、 Fig 6 、 Fig 8__    
`Inventory increase` is measured by <img src="./Formula/formula 3.PNG"/>  and  `profit increase` is measured by  <img src="./Formula/formula 4.PNG"/> 

<table>
 <tr>
    <td>Notation</td>
    <td>Description</td>
  </tr>
  <tr>
    <td>Qu*</td>
    <td>The optimal order quantity in the model with uncertain barter</td>
  </tr>
  <tr>
    <td>E[πu(Qu)]</td>
    <td>The retailer’s Expected profit with uncertain barter</td>
  </tr>
</table>

--------------------------------------------------------------------------------------------------------------------------------------------------------------
Figs. 1-2 verify <img src="./Formula/fig33.PNG"/>. From __Eq. (5)__, <img src="./Formula/figure513.PNG"/> <img src="./Formula/figure514.PNG"/>
Furthermore, <img src="./Formula/figure515.PNG"/> Then, the decline rate with increasing `Q0` is faster than `E[π(Q)]`. 
Besides `E[π(Q)] > E[πc(Q)]`,therefore <img src="./Formula/figure516.PNG"/>



<p style="text-align:center">
  <img src="./Experiment plot/Fig.1.png" width="400" height="300"/>
  <center><b>Fig. 1.</b> Impact of Q_0 on the optimal inventory and profit.</center>
</p>

Shows that with `increasing Q0`, the `retailer’s order quantity increases` while the `profit decreases



<p style="text-align:center">
  <img src="./Experiment plot/Fig.2.png" width="400" height="300"/>
  <center><b>Fig. 2.</b> Impact of Q_0 on inventory and profit increase</center>
</p>

Compared with the `classical newsvendor`, `barter` can improve the `profit` and the `optimal order quantity`. 

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Figs. 3-4 verify <img src="./Formula/eq5.PNG"/>. From Eq. (5)  <img src="./Formula/eq51.PNG"/>  . 
Furthermore, the expected profit `E[πc(Qc)]` is independent with the barter commission `r` , therefore  <img src="./Formula/eq512.PNG"/>

<p style="text-align:center">
  <img src="./Experiment plot/Fig.3.png" width="400" height="300"/>
  <center><b>Fig. 3.</b> Impact of the commission on optimal inventory and profit</center>
</p>


<p style="text-align:center">
  <img src="./Experiment plot/Fig.4.png" width="400" height="300"/>
  <center><b>Fig. 4.</b> Impact of the commission on the inventory and profit increase</center>
</p>


Above plot show that with `decreasing commission`, the retailer’s `order quantity and profit increase`, and their increment rates also increase.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

From the demand perspective, with the increasing value of  `demand variance `, the retailer's  `order quantity ` increases while the `profit ` decreases(Fig.5).

Besides, the increment rate of inventory is decreasing while the increment rate of profit increasing with demand uncertainty(Fig.6), which indicates barter can effectively cope with variance in demand.  

<p style="text-align:center">
  <img src="./Experiment plot/Fig.5.png" width="400" height="300"/>
  <center><b>Fig. 5.</b> Impact of demand uncertainty on the optimal inventory and profit</center>
</p>

<p style="text-align:center">
  <img src="./Experiment plot/Fig.6.png" width="400" height="300"/>
  <center><b>Fig. 6.</b> Impact of demand uncertainty on inventory and profit increase</center>
</p>

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Different from the effect of  `demand uncertainty `, (Fig. 7) shows that with  `increasing barter supply uncertainty`, both the retailer’s order quantity and profit decrease. Compared with the classical newsvendor, barter can still improve the retailer’s profit with higher order quantity.

However, as shown in (Fig. 8), increment rates of inventory and profit are decreasing, which indicates that barter uncertainty will dampen the profitability of barter. Since with barter uncertainty, the successful barter quantity can be lower or higher than the barter demand of the retailer.


<p style="text-align:center">
  <img src="./Experiment plot/Fig.7.png" width="400" height="300"/>
  <center><b>Fig. 7.</b> Impact of barter uncertainty on the optimal inventory and profit</center>
</p>

<p style="text-align:center">
  <img src="./Experiment plot/Fig.8.png" width="400" height="300"/>
  <center><b>Fig. 8.</b> Impact of barter uncertainty on inventory and profit increase</center>
</p>


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# __Conclusion__ 
* Our work provides the guidance for the retailer on how to make inventory decision when using the barter platform. With higher demand uncertainty, the retailer should increase the order quantity, while with higher barter uncertainty the retailer should order less products.  
* Barter can be used by the retailer to cope with the demand uncertainty, especially when the value of the product is larger, and barter uncertainty is lower. In practice, the retailer should consider the joint purchasing decisions of multiple products to take full advantage of barter exchange. For instance, purchasing one product A with higher demand uncertainty and another product B that can be efficiently bartered with unsold product A will be more profitable.  
* For the barter platform, decreasing the barter uncertainty is significant to attract more barter platform users.
