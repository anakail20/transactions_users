# Task 1 SQL Query: Transactions in the Last 7 Days

This SQL script computes the number of transactions a user made in the 7 days preceding each transaction, without including the current transaction itself.

## How It Works

1. **Input Schema:**
   - `transactions` table:
     - `transaction_id`: Unique identifier for each transaction.
     - `user_id`: ID of the user making the transaction.
     - `date`: The date of the transaction.

2. **Logic:**
   - A **CTE** (`trx_last_7days`) is used to identify all transactions that occurred in the 7 days before each transaction for the same user - using BigQuery's logic
   - A `LEFT JOIN` ensures that if there are no transactions in the 7-day window, the result will still include the current transaction with a count of `0`.
   - The main query aggregates the results from the CTE to calculate the number of transactions within the 7-day window for each user transaction.

3. **Output:**
   The result is a table with the following columns:
   - `transaction_id`: Current transaction ID.
   - `user_id`: ID of the user performing the transaction.
   - `date`: Date of the current transaction.
   - `no_txn_last_7days`: Number of transactions the user made in the last 7 days.

# Task 2 Python Code: Replicating SQL query

This Python script processes two CSV files (`transactions.csv` and `users.csv`) to compute aggregated results.

## Features

- Filters transactions to include only:
  - Non-blocked transactions (`is_blocked = False`).
  - Transactions by active users (`is_active = 1`).
- Aggregates:
  - Total transaction amount (`sum_amount`) for each category.
  - Unique user count (`num_users`) for each category.
- Outputs the results in CSV-like format.

## Usage

1. **Prepare the Data**:
   - Place `transactions.csv` and `users.csv` in the same directory as the script.

2. **Run the Script**:
   ```bash
   python compute_query.py
