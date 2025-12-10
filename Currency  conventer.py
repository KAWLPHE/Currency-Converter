"""
Currency Converter by Isomiddin

Features:
- Convert between multiple currencies using a base table
- Clean menu-based interface
- Input validation
- Easy to extend with new currencies or real API later

NOTE:
Exchange rates in this script are EXAMPLES only.
They are NOT real-time and NOT guaranteed to be accurate.
"""

from typing import Dict

# Example exchange rates: value of 1 unit of currency in USD
RATES_TO_USD: Dict[str, float] = {
    "USD": 1.00,      # US Dollar
    "EUR": 1.08,      # Euro
    "GBP": 1.27,      # British Pound
    "JPY": 0.0067,    # Japanese Yen
    "UZS": 0.000079,  # Uzbekistani So'm
    "RUB": 0.010,     # Russian Ruble
    "KZT": 0.0022     # Kazakhstani Tenge
}


def show_supported_currencies() -> None:
    """
    Print all supported currency codes
    """
    print("\nSupported currencies:")
    for code in RATES_TO_USD.keys():
        print(f" - {code}")
    print()


def read_currency(prompt: str) -> str:
    """
    Ask user for a currency code and validate it
    """
    while true := True:
        code = input(prompt).strip().upper()
        if code in RATES_TO_USD:
            return code
        print("Unknown currency code. Type one of:", ", ".join(RATES_TO_USD.keys()))


def read_amount(prompt: str) -> float:
    """
    Ask user for an amount and make sure it's a valid positive number
    """
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
            if value < 0:
                print("Amount must be non-negative.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")


def convert(amount: float, from_currency: str, to_currency: str) -> float:
    """
    Convert amount from one currency to another using USD as base
    """
    if from_currency == to_currency:
        return amount

    # Convert FROM currency to USD
    usd_value = amount * RATES_TO_USD[from_currency]

    # Convert USD to TO currency
    result = usd_value / RATES_TO_USD[to_currency]
    return result


def print_menu() -> None:
    print("\n========== CURRENCY CONVERTER ==========")
    print("1) Convert currency")
    print("2) Show supported currencies")
    print("3) Exit")
    print("========================================")


def main() -> None:
    print("Welcome to the Currency Converter by Isomiddin!")
    print("Note: Exchange rates are example values (static, not real-time).")

    while True:
        print_menu()
        choice = input("Choose an option (1–3): ").strip()

        if choice == "1":
            # Convert currency
            show_supported_currencies()
            from_cur = read_currency("From currency code: ")
            to_cur = read_currency("To currency code: ")
            amount = read_amount(f"Amount in {from_cur}: ")

            result = convert(amount, from_cur, to_cur)
            print(f"\n{amount:.2f} {from_cur} ≈ {result:.2f} {to_cur}")

        elif choice == "2":
            # Show list of supported currencies
            show_supported_currencies()

        elif choice == "3":
            print("Goodbye! 👋")
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
