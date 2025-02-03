import builtins
from django.utils.termcolors import colorize

# Salvăm referința la print() original
original_print = builtins.print


def colored_print(*args, color="white", **kwargs):
    """
    Suprascrie funcția print() pentru a adăuga culoare implicită,
    fără a crea o buclă infinită.
    """
    colored_args = [colorize(str(arg), fg=color) for arg in args]
    original_print(*colored_args, **kwargs)  # Folosește print() original


# Aplicăm modificarea globală
builtins.print = colored_print
