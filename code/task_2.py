import csv
from collections import defaultdict

# Load CSV file into a list of dictionaries
def load_csv(filepath):
    with open(filepath, mode='r') as file:
        return list(csv.DictReader(file))

# Compute results based on the SQL logic
def compute_results(transactions, users):
    # Get a set of active user IDs
    active_users = {user['user_id'] for user in users if user['is_active'] == '1'}

    # Filter for valid transactions (not blocked and by active users)
    valid_transactions = [
        txn for txn in transactions
        if txn['is_blocked'] == 'False' and txn['user_id'] in active_users
    ]

    # Aggregate data by transaction_category_id
    category_totals = defaultdict(lambda: {'sum_amount': 0, 'num_users': set()})
    for txn in valid_transactions:
        category_id = txn['transaction_category_id']
        user_id = txn['user_id']
        amount = float(txn['transaction_amount'])
        category_totals[category_id]['sum_amount'] += amount
        category_totals[category_id]['num_users'].add(user_id)

    # Format and sort results
    results = [
        {
            'transaction_category_id': category_id,
            'sum_amount': data['sum_amount'],
            'num_users': len(data['num_users']),
        }
        for category_id, data in category_totals.items()
    ]
    return sorted(results, key=lambda x: x['sum_amount'], reverse=True)

# Print results
def print_results(results):
    print("transaction_category_id,sum_amount,num_users")
    for result in results:
        print(f"{result['transaction_category_id']},{result['sum_amount']},{result['num_users']}")

# Main function to load data and compute results
def main():
    transactions = load_csv('transactions.csv')
    users = load_csv('users.csv')
    results = compute_results(transactions, users)
    print_results(results)

if __name__ == "__main__":
    main()
