## Task-4 Summary: SQL for Data Analysis

In Task-4, the objective was to apply SQL techniques for structured data analysis using a self-created ecommerce database. The database included multiple related tables: customers, orders, products, sales, and category.

The task focused on the following key areas:

- **Data Retrieval and Filtering:**
Practiced the use of SELECT, WHERE, ORDER BY, and GROUP BY clauses to retrieve and organize data based on specific conditions and grouping criteria.

- **Joins:**
Implemented INNER JOIN, LEFT JOIN, and RIGHT JOIN to combine data from multiple tables and gain insights across related datasets.

- **Subqueries:**
Used subqueries to perform nested operations, enabling more advanced filtering and comparison within the dataset.

- **Aggregate Functions:**
Applied functions such as SUM() and AVG() to perform numerical analysis and calculate metrics like total revenue and average order value.

- **Views:**
Created SQL views to simplify frequently used queries and support reusable, consistent data analysis without rewriting complex joins or aggregations.

- **Index Optimization:**
Explored performance tuning by creating indexes on commonly searched columns to enhance query speed and efficiency.



#### Outcome:
The task strengthened the understanding of SQL as a fundamental tool for querying, analyzing, and optimizing structured data in a relational database system. It also provided hands-on experience with key concepts essential for real-world data analysis.


------


### Interview Question's Answers:

**1. What is the difference between WHERE and HAVING?**
> The WHERE clause filters rows before any grouping is done, while the HAVING clause filters groups after the GROUP BY operation. Use WHERE with individual rows and HAVING with aggregate functions like SUM(), COUNT(), etc.

**2. What are different types of joins?**
> INNER JOIN: Returns matching rows from both tables.
>
> LEFT JOIN (or LEFT OUTER JOIN): All rows from the left table, and matching rows from the right.
>
> RIGHT JOIN (or RIGHT OUTER JOIN): All rows from the right table, and matching rows from the left.
>
> FULL JOIN (or FULL OUTER JOIN): All rows when there is a match in either table.
>
> CROSS JOIN: Returns the Cartesian product of both tables.
> 
> SELF JOIN: Joins a table with itself.



**3. How to calculate Average Revenue Per User (ARPU) in SQL?**

> SELECT SUM(revenue) / COUNT(DISTINCT user_id) AS ARPU FROM sales;
> 
> This divides total revenue by the number of unique users.



**4. What are subqueries?**
> Subqueries are nested queries inside a main query. They are used to perform operations that require multiple steps, like filtering results based on the output of another query.


**5. How to optimize a SQL query?**
> Use indexes on frequently searched columns
> 
> Avoid SELECT *, select only required columns
> 
> Use joins efficiently and avoid unnecessary subqueries
> 
> Use WHERE to filter early
> 
> Use EXPLAIN to analyze query execution plans



**6. What is a view in SQL?**
> A view is a virtual table based on a SQL query. It doesn't store data itself but presents data from one or more tables. It's used for simplifying complex queries, security, and reusability.



**7. How to handle null values in SQL?**
> Use IS NULL or IS NOT NULL to filter nulls
> 
> Use COALESCE() or IFNULL() to replace nulls with a default value
> 
> Use NULLIF() to return null if two expressions are equal
