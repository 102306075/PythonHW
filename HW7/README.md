DATE : 20090101-20180101</B> <br/>
策略績效 :
RETURNS
429.69%</B> <br/>
ALPHA
0.13 </B> <br/>
BETA
0.51</B> <br/>
SHARPE
0.99</B> <br/>
DRAWDOWN
-39.26%

```   
def initialize(context):
    #IBM GOOG AAPL
    context.securities = [sid(3766),sid(46631),sid(24)]
    schedule_function(rebalance, date_rule=date_rules.every_day())

def rebalance(context, data):
    for stock in context.securities:
        price_history = data.history(
             stock,
             fields='price',
             bar_count=7,
             frequency='1d'
         )

        average_price = price_history.mean()
        
        current_price = data.current(stock, 'price') 
         
        if data.can_trade(stock):
#買入:目前價>1.01均價
             if current_price > (1.01*average_price):
                 order_target_percent(stock, 1)
                 log.info("Buying %s" % (stock.symbol))
#賣出:目前價<1.07均價
             elif current_price < (1.07*average_price):
                 order_target_percent(stock, 0)
                 log.info("Selling %s" % (stock.symbol))
        record(current_price=current_price, average_price=average_price)
```
