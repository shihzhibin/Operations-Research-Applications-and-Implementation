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
      <a href="#problem-description">Problem Description</a>
    </li>
    <li>
      <a href="#model">The Model</a>
      <ul>
        <li><a href="#biased-random-key-enetic-lgorithmn">Biased Random-Key Genetic Algorithmn</a></li>
        <li><a href="#placement-strategy">Placement Strategy</a></li>
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
>> There are two basic types of barter:
* Personal barter and retail barter
* Commercial barter
> We only focus on the commercial barter in this tutorial  
# __The Model__
* We consider the single-period inventory (newsvendor) problem with barter exchange from the retailer's perspective, in which the customer's demand is `stochastic` and characterized by a `random variable`. The retailer determines the optimal stocking policy to satisfy the customer demand at the beginning of the selling season.  
* Suppose the retailer purchases only a single product A from the supplier, and the retail price is set by the supplier or the market. This problem is to decide the optimal order quantity to `maximize its own expected profit`.  
* The retailer orders `Q units of the product A` from the supplier at a `fixed price` at the beginning of the selling season, then it sells product A to its customers at the `retail price`.
 *  The notation used in the paper is as follows:  
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
