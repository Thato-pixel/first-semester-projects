# Entry point for the MiniMart data reporting system
from dotenv import load_dotenv
import os
import psycopg2
# Assuming these are correct now
from month2_minimart_analysis.python.utils import convert_currency, apply_discount, is_large_order, calculate_order_total
from month2_minimart_analysis.python.report_generator import generate_report


def get_connection():
    """Create a PostgreSQL database connection using environment variables."""
    load_dotenv()
    dbname = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")

    return psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )


def insert_simulated_orders(connection, orders):
    """Insert simulated orders into the database (only if not already added)."""
    # ... (No changes needed here)
    cursor = connection.cursor()
    inserted = 0

    for order in orders:
        # Check if this exact order already exists
        cursor.execute("""
            SELECT 1 FROM orders 
            WHERE customer_id = %s AND product_id = %s AND quantity = %s;
        """, (order["customer_id"], order["product_id"], order["quantity"]))
        
        exists = cursor.fetchone()

        if not exists:
            cursor.execute("""
                INSERT INTO orders (customer_id, product_id, quantity, order_date)
                VALUES (%s, %s, %s, NOW());
            """, (order["customer_id"], order["product_id"], order["quantity"]))
            inserted += 1

    connection.commit()
    cursor.close()
    print(f"✅ {inserted} new simulated orders inserted into database (duplicates skipped).")


def simulate_orders(connection):
    """Simulate sample new orders and demonstrate conditional logic."""
    sample_orders = [
        {"customer_id": 1, "product_id": 1, "product": "Milk", "price": 80, "quantity": 20},
        {"customer_id": 2, "product_id": 2, "product": "Laptop", "price": 15000, "quantity": 1},
        {"customer_id": 3, "product_id": 3, "product": "Notebook", "price": 25, "quantity": 10},
    ]

    # Insert into database
    insert_simulated_orders(connection, sample_orders)

    print("\n🧾 Simulated Orders Summary:")
    for order in sample_orders:
        total = calculate_order_total(order["price"], order["quantity"])
        large_flag = is_large_order(total, threshold=1000)
        discounted_price = apply_discount(order["price"], order["quantity"])
        
        # FIX APPLIED HERE: Ensure 'total' is a float before conversion
        converted_total = convert_currency(float(total), target_currency="ZAR") 

        print(f"- Customer {order['customer_id']} | {order['product']} x {order['quantity']}")
        print(f"  Total Price: R{total:,.2f}")
        print(f"  Discounted Unit Price (if applicable): R{discounted_price:,.2f}")
        print(f"  Total in Rands (converted): R{converted_total:,.2f}")
        print(f"  Large Order: {'✅ Yes' if large_flag else '❌ No'}\n")


def main():
    """Main workflow for the MiniMart data reporting system."""
    connection = None
    try:
        connection = get_connection()
        print("✅ Connected to PostgreSQL database successfully.")

        # Generate report from live SQL data
        report = generate_report(connection)

        print("\n📊 Retail Data Summary Report:")
        print(f"Total Products Sold: {report['total_products_sold']}")
        print(f"Most Popular Product: {report['most_popular_product']}")
        print("Revenue Per Customer:")
        for customer, revenue in report['revenue_per_customer'].items():
            # FIX APPLIED HERE: Ensure 'revenue' is a float before conversion
            rand_value = convert_currency(float(revenue), target_currency='ZAR')
            print(f"  - {customer}: R{rand_value:,.2f}")

        # Simulate and insert new orders
        simulate_orders(connection)

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        if connection:
            connection.close()
            print("🔒 Database connection closed.")


if __name__ == "__main__":
    main()
