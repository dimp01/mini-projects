## Task - 7 Summary: Get Basiscs Sales Summary from a Tiny SQLite Database using Python.

### Task Description
The objective of this task was to extract and summarize key sales information from a small SQLite database using Python.

#

### Dataset Overview
- **Type:** SQLite database
- **Content:**
   - A custom SQLite database: sales_data.db
   - A single table: sales
   - Key columns: product, quantity, price

#

### Tools & Technologies used
- **Python:** For scripting and data extraction.
- **SQLite:** As the database engine to store and retrieve sales data.
- **pandas:** For additional data manipulation and summarization
- **matplotlib:** For data visualization

#

### Objective:
The objective of this task was to extract and summarize sales data from a small SQLite database using SQL queries within Python, and to visualize the results with a simple bar chart. This project helped bridge the gap between database operations and Python-based data analysis.

#

### Project Workflow:

**1. Database Connection:**
Established a connection to the sales_data.db using Python’s built-in sqlite3 module.

**2. SQL Query Execution:**
Executed a query to compute:
- Total quantity sold
- Total revenue per product

Example query:

  SELECT product, SUM(quantity) AS total_qty, SUM(quantity * price) AS revenue 
  FROM sales 
  GROUP BY product;


3. Data Import into Python:
Used pandas.read_sql_query() to load the SQL results into a DataFrame for further analysis and display.


4. Output Display:
Printed the DataFrame to show the product-wise summary of quantity and revenue.


5. Data Visualization:
Created a simple bar chart using matplotlib to represent revenue per product.
Optional: The chart was saved as an image file (sales_chart.png).



Key Outcomes:

Practiced writing and running SQL queries within a Python environment.

Learned how to connect to SQLite and extract data using pandas.

Gained hands-on experience in visualizing database results using Python plotting tools.

Produced a basic, yet functional, sales dashboard summary for quick insights.


Conclusion:
This task demonstrated the practical use of Python + SQL for lightweight data analysis. It emphasized how easy it is to extract, manipulate, and visualize data from a database without the need for heavy tools or setup. The workflow is ideal for quick reports, data exploration, and prototyping business analytics solutions.



Interview Question's Answers:

1. How did you connect Python to a database?
I used the sqlite3 library in Python to connect to an SQLite database. The connection is established using:

import sqlite3  
conn = sqlite3.connect('database_name.db')  
cursor = conn.cursor()


---

2. What SQL query did you run?
An example query I ran:

SELECT Category, SUM(Sales) AS Total_Revenue  
FROM SalesData  
GROUP BY Category;


---

3. What does GROUP BY do?
GROUP BY is used to aggregate data based on one or more columns. It groups rows with the same values and allows functions like SUM(), COUNT(), AVG() to be applied to each group.


---

4. How did you calculate revenue?
Revenue was calculated using the SUM() function in SQL or with df['Revenue'].sum() in pandas, depending on whether I was using SQL or Python.


---

**5. How did you visualize the result?**
> I used Python libraries such as Matplotlib and Seaborn to create bar charts and line graphs. For example:

  > import matplotlib.pyplot as plt  
  > df.plot(kind='bar', x='Category', y='Total_Revenue')

<br>

**6. What does pandas do in your code?**
> pandas is used to read, clean, manipulate, and analyze data in a structured format. It allows for operations like filtering, grouping, merging datasets, and running descriptive statistics.


<br>

**7. What’s the benefit of using SQL inside Python?**
> Combining SQL with Python offers flexibility:

> SQL handles complex data retrieval and aggregation.

> Python processes, visualizes, and integrates the results with other tools.

> This makes the workflow more powerful and automated.

<br>

**8. Could you run the same SQL query directly in DB Browser for SQLite?**
> Yes, the same SQL query can be executed directly in DB Browser for SQLite. Python simply allows running the query programmatically.
