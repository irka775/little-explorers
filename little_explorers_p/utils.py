"""
Custom print function with color support.

This module overrides the built-in `print` function to add color to output text,
using Django's `colorize` utility. It ensures the original `print` function 
remains accessible to prevent infinite recursion.
"""

import builtins
from django.utils.termcolors import colorize

# Save a reference to the original print function
original_print = builtins.print


def colored_print(*args, color="white", **kwargs):
    """
    Overrides the built-in print() function to add color to output text.

    - Uses Django's `colorize()` to apply the specified foreground color.
    - Ensures the original `print()` function is used to prevent infinite loops.

    Args:
        *args: The values to print.
        color (str): The foreground color to apply (default is "white").
        **kwargs: Additional keyword arguments for the original print function.

    Example:
        print("Hello, World!", color="red")  # Prints "Hello, World!" in red.
    """
    colored_args = [colorize(str(arg), fg=color) for arg in args]
    original_print(
        *colored_args, **kwargs
    )  # Use the original print function


# Apply the modification globally
builtins.print = colored_print
