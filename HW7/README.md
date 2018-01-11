date : 20090101-20180101

RETURNS
429.69%
 
ALPHA
0.13
 
BETA
0.51
 
SHARPE
0.99
 
DRAWDOWN
-39.26%

code

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

             if current_price > (1.01*average_price):
                 order_target_percent(stock, 1)
                 log.info("Buying %s" % (stock.symbol))

             elif current_price < (1.07*average_price):
                 order_target_percent(stock, 0)
                 log.info("Selling %s" % (stock.symbol))
        record(current_price=current_price, average_price=average_price)
