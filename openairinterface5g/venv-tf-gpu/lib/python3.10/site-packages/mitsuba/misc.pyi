

def core_count() -> int:
    """Determine the number of available CPU cores (including virtual cores)"""

def time_string(time: float, precise: bool = False) -> str:
    """
    Convert a time difference (in seconds) to a string representation

    Parameter ``time``:
        Time difference in (fractional) sections

    Parameter ``precise``:
        When set to true, a higher-precision string representation is
        generated.
    """

def mem_string(size: int, precise: bool = False) -> str:
    """Turn a memory size into a human-readable string"""

def trap_debugger() -> None:
    """
    Generate a trap instruction if running in a debugger; otherwise,
    return.
    """
