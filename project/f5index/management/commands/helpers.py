from sys import stdout

def print_colored(message, color):
        """
        Prints a message in the specified color using self.stdout.write.

        Args:
        - message (str): The message to print.
        - color (str): The color to print the message in. Options: 'red', 'green', 'blue', etc.

        Returns:
        - None
        """

        colors = {
            "black": "\033[30m",
            "red": "\033[31m",
            "green": "\033[32m",
            "yellow": "\033[33m",
            "blue": "\033[34m",
            "magenta": "\033[35m",
            "cyan": "\033[36m",
            "white": "\033[37m",
            "reset": "\033[0m"
        }

        color_code = colors.get(color.lower(), colors["reset"])
        stdout.write(f"{color_code}{message}\033[0m\n")  # \033[0m resets the color to default

def print_creation_status(obj, created, obj_name):
    """
    Prints a message indicating whether an object was created or already existed.

    Args:
        obj: The object that was created or retrieved.
        created (bool): Whether the object was created.
        obj_name (str): A human-readable name for the object type.
        action (function): A function to run if object was created.
    """
    if created:
        print_colored(f'\t- [x] helpers/check::{obj_name} was created', 'cyan')
    else:
        print_colored(f'\t- [ ] helpers/check::{obj_name} already exists', 'yellow')
