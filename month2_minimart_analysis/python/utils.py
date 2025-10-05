# Utility functions for data conversion and filtering
def calculate_order_total(price, quantity):
    """Calculate total cost of an order."""
    return price * quantity


def is_large_order(total, threshold=1000):
    """Check if an order is considered large based on a threshold."""
    return total > threshold


def apply_discount(price, quantity):
    """Apply a 10% discount for bulk purchases (more than 10 items)."""
    if quantity > 10:
        return price * 0.9
    return price


def convert_currency(amount, target_currency="ZAR"):
    """Convert currency from a base (USD assumed) to Rands (ZAR)."""
    exchange_rates = {
        "ZAR": 18.5,   # Example: 1 USD = 18.5 R
        "USD": 1
    }

    rate = exchange_rates.get(target_currency.upper(), 1)
    return amount * rate