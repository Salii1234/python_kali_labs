recent_users = ["admin_alice", "user_bob", "GUEST_charlie", "admin_david", "GUEST_eve"]

for user in recent_users:
    if 'admin' in user:
        print(f'[HIGH PRIVILEGE] -> {user}')
    elif 'GUEST' in user:
        print(f'[RESTRICTED] -> {user}')
    else:
        print(f'[STANDARD] -> {user}')

