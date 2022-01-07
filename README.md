# Operations-Research-Applications-and-Implementation
## The newsvendor problem with barter exchange  

* We consider the single-period inventory (newsvendor) problem with barter exchange from the retailer's perspective, in which the customer's demand is `stochastic` and characterized by a `random variable`. The retailer determines the optimal stocking policy to satisfy the customer demand at the beginning of the selling season.  
* Suppose the retailer purchases only a single product A from the supplier, and the retail price is set by the supplier or the market. This problem is to decide the optimal order quantity to `maximize its own expected profit`.  
 
 * The notation used in the paper is as follows:  
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
