from datetime import datetime, timezone


def get_current_time() -> datetime:
    """Return the current date and time in UTC."""
    return datetime.now(timezone.utc)


def get_greeting() -> str:
    """Return a greeting message."""
    return "Hello, welcome to my automation project!"


def save_output(message: str) -> None:
    """Add the message to the automation output file."""
    with open("automation_output.txt", "a", encoding="utf-8") as file:
        file.write(message + "\n")


def main() -> None:
    current_time = get_current_time()
    greeting = get_greeting()

    output = (
        f"Current date and time: {current_time:%Y-%m-%d %H:%M:%S} UTC\n"
        f"{greeting}"
    )

    print(output)
    save_output(output)


if __name__ == "__main__":
    main()