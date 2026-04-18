from typing import overload


class path:
    """
    Represents a path to a filesystem resource. On construction, the path
    is parsed and stored in a system-agnostic representation. The path can
    be converted back to the system-specific string using ``native()`` or
    ``string()``.
    """

    @overload
    def __init__(self) -> None:
        """
        Default constructor. Constructs an empty path. An empty path is
        considered relative.
        """

    @overload
    def __init__(self, arg: path) -> None:
        """Copy constructor."""

    @overload
    def __init__(self, arg: str, /) -> None:
        r"""
        Construct a path from a string view with native type. On Windows, the
        path can use both '/' or '\\' as a delimiter.
        """

    def clear(self) -> None:
        """Makes the path an empty path. An empty path is considered relative."""

    def empty(self) -> bool:
        """Checks if the path is empty"""

    def is_absolute(self) -> bool:
        """Checks if the path is absolute."""

    def is_relative(self) -> bool:
        """Checks if the path is relative."""

    def parent_path(self) -> path:
        """
        Returns the path to the parent directory. Returns an empty path if it
        is already empty or if it has only one element.
        """

    def extension(self) -> path:
        """
        Returns the extension of the filename component of the path (the
        substring starting at the rightmost period, including the period).
        Special paths '.' and '..' have an empty extension.
        """

    def replace_extension(self, arg: path, /) -> path:
        """
        Replaces the substring starting at the rightmost '.' symbol by the
        provided string.

        A '.' symbol is automatically inserted if the replacement does not
        start with a dot. Removes the extension altogether if the empty path
        is passed. If there is no extension, appends a '.' followed by the
        replacement. If the path is empty, '.' or '..', the method does
        nothing.

        Returns *this.
        """

    def filename(self) -> path:
        """Returns the filename component of the path, including the extension."""

    def native(self) -> str:
        """
        Returns the path in the form of a native string, so that it can be
        passed directly to system APIs. The path is constructed using the
        system's preferred separator and the native string type.
        """

    def __truediv__(self, arg: path, /) -> path:
        """Concatenates two paths with a directory separator."""

    def __eq__(self, arg: path, /) -> bool:
        """
        Equality operator. Warning: this only checks for lexicographic
        equivalence. To check whether two paths point to the same filesystem
        resource, use ``equivalent``.
        """

    def __ne__(self, arg: path, /) -> bool:
        """Inequality operator."""

    def __repr__(self) -> str:
        """
        Returns the path in the form of a native string, so that it can be
        passed directly to system APIs. The path is constructed using the
        system's preferred separator and the native string type.
        """

preferred_separator: str = '/'

def current_path() -> path:
    """Returns the current working directory (equivalent to getcwd)"""

def absolute(arg: path, /) -> path:
    """
    Returns an absolute path to the same location pointed by ``p``,
    relative to ``base``.

    See also:
        http ://en.cppreference.com/w/cpp/experimental/fs/absolute)
    """

def is_regular_file(arg: path, /) -> bool:
    """
    Checks if ``p`` points to a regular file, as opposed to a directory or
    symlink.
    """

def is_directory(arg: path, /) -> bool:
    """Checks if ``p`` points to a directory."""

def exists(arg: path, /) -> bool:
    """Checks if ``p`` points to an existing filesystem object."""

def file_size(arg: path, /) -> int:
    """
    Returns the size (in bytes) of a regular file at ``p``. Attempting to
    determine the size of a directory (as well as any other file that is
    not a regular file or a symlink) is treated as an error.
    """

def equivalent(arg0: path, arg1: path, /) -> bool:
    """
    Checks whether two paths refer to the same file system object. Both
    must refer to an existing file or directory. Symlinks are followed to
    determine equivalence.
    """

def create_directory(arg: path, /) -> bool:
    """
    Creates a directory at ``p`` as if ``mkdir`` was used. Returns true if
    directory creation was successful, false otherwise. If ``p`` already
    exists and is already a directory, the function does nothing (this
    condition is not treated as an error).
    """

def resize_file(arg0: path, arg1: int, /) -> bool:
    """
    Changes the size of the regular file named by ``p`` as if ``truncate``
    was called. If the file was larger than ``target_length``, the
    remainder is discarded. The file must exist.
    """

def remove(arg: path, /) -> bool:
    """
    Removes a file or empty directory. Returns true if removal was
    successful, false if there was an error (e.g. the file did not exist).
    """

def copy_file(arg0: path, arg1: path, /) -> bool:
    """Copy a file from source to destination"""
