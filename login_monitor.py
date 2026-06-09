from datetime import datetime

MAX_FAILED_ATTEMPTS = 3

failed_attempts = {}

# Simulated user database
users = {
    "admin": "admin123",
    "shoheb": "physics123"
}

# Log Function
def log_attempt(username, status):

    with open(
        "login_logs.txt",
        "a"
    ) as file:

        file.write(
            f"{datetime.now()} | "
            f"{username} | "
            f"{status}\n"
        )


while True:

    print("\n===== Login Attempt Monitor =====")

    username = input(
        "Username: "
    )

    password = input(
        "Password: "
    )

    if (
        username in users
        and
        users[username] == password
    ):

        print("Login Successful!")

        log_attempt(
            username,
            "SUCCESS"
        )

        failed_attempts[
            username
        ] = 0

    else:

        print(
            "Invalid Credentials!"
        )

        log_attempt(
            username,
            "FAILED"
        )

        failed_attempts[
            username
        ] = (
            failed_attempts.get(
                username,
                0
            ) + 1
        )

        if (
            failed_attempts[
                username
            ] >= MAX_FAILED_ATTEMPTS
        ):

            print(
                "⚠ Suspicious Activity Detected!"
            )

    choice = input(
        "\nContinue? (y/n): "
    )

    if choice.lower() != "y":

        break
