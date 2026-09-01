import pandas as pd
import sqlite3

with sqlite3.connect("../db/lesson.db") as conn:
    sql_statement = """
    SELECT l.line_item_id, l.quantity, p.product_id, p.product_name, p.price
    FROM line_items l
    JOIN products p
    ON l.product_id = p.product_id;
    """

    df = pd.read_sql_query(sql_statement, conn)
    print(df.head())

# Add a column "total"
df['total'] = df['quantity'] * df['price']
print(df.head())

# Add groupby() code to group by the product_id
grouped = df.groupby('product_id').agg({'line_item_id':'count', 'total':'sum', 'product_name':'first'})
print(grouped.head())

# Sort the DataFrame by the product_name column
sorted_df = grouped.sort_values(by = 'product_name').reset_index()
print(sorted_df.head())

# Create CSV file
sorted_df.to_csv("order_summary.csv", index = False)
print("Dataframe saved to order_summary.csv")