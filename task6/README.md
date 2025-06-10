## Task-6 Summary : Sales Trend Analysis using Aggregation. 



### Task Description

This task involves performing a time-based sales trend analysis using SQL aggregation techniques. The dataset provided is an online_sales table, specifically focusing on the orders table, which contains relevant fields such as order_date, amount, and product_id. The analysis centers on aggregating monthly revenue and order volume to identify patterns and trends in sales performance over a defined time period.
#
### Dataset
online_ssles database contains :
- orders table with columns (order_id, order_date, amount, product_id) 
- products table with columns (product_id, name, price, category_id)
- category table with columns (category_id, category)

#
### Tool

MySQL was used as the relational database management system to execute SQL queries and perform the analysis.
#

### Objective

The primary objective is to analyze monthly sales trends by calculating total revenue and order volume for each month. This involves grouping data by month and year, and applying aggregation functions to derive meaningful insights about business performance over time.

#
### Summary

The analysis was conducted by extracting the month and year from the order_date column using SQL's EXTRACT() function. The data was then grouped accordingly to observe trends on a monthly basis.

- Revenue was calculated using the SUM(amount) function to get total monthly earnings.

- Order volume was measured using COUNT(DISTINCT order_id) to ensure unique orders were counted accurately.

- The ORDER BY clause was applied to sort the data chronologically or based on revenue/order count, depending on the specific analytical requirement.

- Additionally, the use of LIMIT allowed for narrowing down the results to specific timeframes or top-performing months, enhancing the focus of the trend analysis.


All queries adhered strictly to SQL standards for compatibility and clarity. Care was taken to ensure that NULL values were inherently handled, as aggregate functions in MySQL generally ignore NULLs unless explicitly addressed.
#
### Conclusion

This task demonstrated the effective use of SQL aggregation functions in analyzing temporal sales data. By breaking down the dataset into monthly segments, it provided a clearer view of business performance trends and highlighted any seasonal patterns or fluctuations in sales and order activity.
#
### Outcome

Through this analysis, proficiency was developed in using SQL for time-series data aggregation, enhancing both technical querying skills and business interpretation capabilities. The insights obtained from this task can serve as a foundation for more advanced reporting, forecasting, or decision-making processes related to sales strategy and resource planning.

<br>

---

<br>

### Answers for Interview Questions:

<br>

**1. How do you group data by month and year?**
> Use GROUP BY YEAR(date_column), MONTH(date_column) or use DATE_FORMAT(date_column, '%Y-%m') in MySQL for better formatting.

<br>

**2. What's the difference between COUNT(*) and COUNT(DISTINCT col)?**
> COUNT(*) counts all rows including NULLs.
>
> COUNT(DISTINCT col) counts unique non-NULL values in the column.

<br>

**3. How do you calculate monthly revenue?**
> Use:
>
> SELECT YEAR(order_date), MONTH(order_date), SUM(revenue)  
> FROM sales  
> GROUP BY YEAR(order_date), MONTH(order_date);

<br> 

**4. What are aggregate functions in SQL?**
> Functions that perform calculations on a set of values and return a single result: SUM(), AVG(), MAX(), MIN(), COUNT().

<br>

**5. How to handle NULLs in aggregates?**
> Most aggregates ignore NULLs automatically. To handle explicitly, use COALESCE(column, 0) to replace NULLs with 0.

<br>

**6. What’s the role of ORDER BY and GROUP BY?**
> GROUP BY groups rows with the same values to perform aggregations.
>
> ORDER BY sorts the result set by specified columns.

<br>

**7. How do you get the top 3 months by sales?**
> Use:
>
> SELECT DATE_FORMAT(order_date, '%Y-%m') AS month, SUM(sales) AS total_sales  
> FROM sales  
> GROUP BY month  
> ORDER BY total_sales DESC  
> LIMIT 3;


