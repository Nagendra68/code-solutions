SELECT date,
ticker,
close,
close - LAG(close) OVER (
  PARTITION BY ticker
  ORDER BY date) AS difference_consecutive_month,
close - LAG(close, 3) OVER (
  PARTITION BY ticker
  ORDER BY date) AS difference_3month
FROM stock_prices
WHERE ticker = 'GOOG';