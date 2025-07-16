# 12. Bank Account Simulation

accounts = {
    101: {"name": "Amit", "balance": 1200},
    102: {"name": "Sara", "balance": 900},
}

# Deposit
accounts[101]["balance"] += 500

# Withdraw
if accounts.get(102):
    accounts[102]["balance"] -= 200

# Low balance alert
low_accounts = {k: v for k, v in accounts.items() if v["balance"] < 1000}
print("Low Balance Accounts:", low_accounts)
