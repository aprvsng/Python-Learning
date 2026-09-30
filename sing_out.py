queue = [
    ("Annie", "Dancing Queen"),
    ("Bob", "Happy Birthday")
]


def show_queue(queue):
    """Print the current queue of songs."""

    print()

    if len(queue) == 0:
        print("The queue is empty. No singers are waiting.")
        return

    print("[The current queue of songs:]")
    print()

    for i, singer in enumerate(queue):
        name, song = singer
        print(f"{i + 1}. {name} will sing '{song}'")


def add_singer(queue):
    """Add a singer to the queue."""

    print()
    print("Enter the singer's name and the song they will sing.")
    print()

    try:
        name = input("Enter the singer's name: ").strip().title()
        song = input("Enter the song they will sing: ").strip().title()

    except (KeyboardInterrupt, EOFError):
        print("\nInput cancelled.")
        return

    if name == "" or song == "":
        print()
        print("Invalid input. Please enter both a name and a song.")
        return

    # Check whether the singer is already in the queue
    for singer in queue:
        if singer[0].lower() == name.lower():
            print()
            print(f"{name} is already in the queue.")
            return

    queue.append((name, song))

    print()
    print(f"Added {name} singing '{song}' to the queue.")


def next_singer(queue):
    """Show and remove the next singer from the queue."""

    if len(queue) == 0:
        print()
        print("The queue is empty. No singers are waiting.")
        return

    name, song = queue.pop(0)

    print()
    print(f"The next singer is {name}, who will sing '{song}'.")


def move_to_top(queue):
    """Move a singer to the top of the queue."""

    if len(queue) <= 1:
        print()
        print("The queue is empty or has only one singer.")
        print("No need to move anyone.")
        return

    print()

    try:
        position = int(
            input("Enter the position of the singer to move to the top: ")
        )

    except ValueError:
        print()
        print("Invalid input. Please enter a number.")
        return

    except (KeyboardInterrupt, EOFError):
        print("\nInput cancelled.")
        return

    # User enters positions starting from 1
    if position < 1 or position > len(queue):
        print()
        print("Invalid position. Please try again.")
        return

    # Convert user's position to Python's zero-based index
    position -= 1

    singer = queue.pop(position)
    queue.insert(0, singer)

    name, song = singer

    print()
    print(f"Moved {name} singing '{song}' to the top of the queue.")


def remove_singer(queue):
    """Remove a singer from the queue."""

    if len(queue) == 0:
        print()
        print("The queue is empty. No singers are waiting.")
        return

    print()

    try:
        name = input("Enter the singer's name to remove: ").strip().title()

    except (KeyboardInterrupt, EOFError):
        print("\nInput cancelled.")
        return

    if name == "":
        print()
        print("Invalid input. Please enter a singer's name.")
        return

    for singer in queue:

        if singer[0].lower() == name.lower():
            queue.remove(singer)

            print()
            print(f"Removed {singer[0]} from the queue.")
            return

    print()
    print(f"{name} is not in the queue.")


def run_app(queue):
    """Run the Sing Out application."""

    print("=" * 40)
    print(" " * 9 + "Welcome to Sing Out!")
    print("=" * 40)

    is_running = True

    while is_running:

        show_queue(queue)

        print()
        print("Options: Add, Next, Top, Remove, Quit")
        print()

        try:
            command = input("> ").strip().lower()

        except (KeyboardInterrupt, EOFError):
            print()
            print("Input cancelled.")
            print()
            print("Thank you for using Sing Out!")
            break

        if command == "quit":

            is_running = False

            print()
            print("Thank you for using Sing Out!")
            print()

        elif command == "add":
            add_singer(queue)

        elif command == "next":
            next_singer(queue)

        elif command == "top":
            move_to_top(queue)

        elif command == "remove":
            remove_singer(queue)

        elif command == "":
            print()
            print("Please enter a command.")

        else:
            print()
            print("Invalid command. Please try again.")


run_app(queue)
