# Code to generate dictionary summary reports
def generate_report(connection):
    """Generate a sales report from the database."""
    cursor = connection.cursor()

    # Total products sold
    cursor.execute("SELECT SUM(quantity) FROM orders;")
    total_products_sold = cursor.fetchone()[0] or 0

    # Most popular product
    cursor.execute("""
        SELECT p.product_name, SUM(o.quantity) AS total_sold
        FROM orders o
        JOIN products p ON o.product_id = p.product_id 
        GROUP BY p.product_name                         
        ORDER BY total_sold DESC
        LIMIT 1;
    """)
    popular_product_row = cursor.fetchone()
    most_popular_product = popular_product_row[0] if popular_product_row else "None"

    # Revenue per customer
    cursor.execute("""
        SELECT c.name, SUM(o.quantity * p.price) AS total_revenue
        FROM orders o
        JOIN customer c ON o.customer_id = c.customer_id  
        JOIN products p ON o.product_id = p.product_id    
        GROUP BY c.name;
    """)
    revenue_rows = cursor.fetchall()

    revenue_per_customer = {row[0]: row[1] for row in revenue_rows}

    cursor.close()
    return {
        "total_products_sold": total_products_sold,
        "most_popular_product": most_popular_product,
        "revenue_per_customer": revenue_per_customer
    }