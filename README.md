# Operations-Research-Applications-and-Implementation
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
      <a href="#model">The Model</a>
      <ul>
        <li><a href="#biased-random-key-enetic-lgorithmn">The Classical Newsvendor Model with Consumption</a></li>
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
> The aim of the barter is to maintain trade volumes and balance them while maximizing the utility of the participants.  
# __The Model__
* We consider the `single-period` inventory (newsvendor) problem with barter exchange from the retailer's perspective, in which the customer's demand is `stochastic` and characterized by a `random variable`. The retailer determines the optimal stocking policy to satisfy the customer demand at the beginning of the selling season.  
* Suppose the retailer purchases only a single product A from the supplier, and the retail price is set by the supplier or the market. This problem is to decide the optimal order quantity to `maximize its own expected profit`.  
* The retailer orders `Q units of the product A` from the supplier at a `fixed price` at the beginning of the selling season, then it sells product A to its customers at the `retail price`.  
* There are three cases of the retailer's profit:  
(1) If customer demand is `greater than` Q, then it will pay `the shortage penalty cost` for the unsatisfied demand  
(2) If customer demand is `less than` Q, the retailer will trade the unsold product A for the product it needs on a barter platform  
(3) If there are still some `unsold product A` after barter exchange, the retailer will dispose of them at a very low price  
 *  The notation used in this tutorial is as follows:  
x: Stochastic demand, a random variable  
f(x): The probability density function of x  
F(x): The cumulative distribution function of x  
c: The supplier's wholesale price  
p: The retailing price per unit (p > c)  
v: The salvage value per unit (v < c)  
s: The shortage penalty cost per unit  
Q: The order quantity, a decision variable  
Q_0: The value of the product the retailer needs on the barter platform is equal to the value of Q0 units of the product that the retailer sells  
Q_c*: The optimal order quantity in the classical newsvendor model   
Q*: The optimal order quantity in the newsvendor model with barter  
r: The retailer pays r percent of retail price to the barter platform as the commission of per unit product  
π(Q,x): The total profit if the order size is Q units and the customer demand is x
## __The classical newsvendor model with consumption__
# __Visualization__  
With the increasing value of Q_0, the retailer's order quantity increases while the profit decreases (Fig. 1).
<p style="text-align:center">
  <img src="./Fig.1.png" width="100" height="50"/>
  <center><b>Fig. 1.</b> Impact of Q_0 on the optimal inventory and profit</center>
</p>


