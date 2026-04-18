from collections.abc import Iterable, Iterator, Sequence
from typing import overload

import mitsuba
import mitsuba.filesystem


class ParserConfig:
    def __init__(self, variant: str) -> None:
        """Constructor that takes variant name"""

    @property
    def unused_parameters(self) -> mitsuba.LogLevel:
        """
        How to handle unused "$key" -> "value" substitution parameters: Error (default), Warn, or Debug
        """

    @unused_parameters.setter
    def unused_parameters(self, arg: mitsuba.LogLevel, /) -> None: ...

    @property
    def unused_properties(self) -> mitsuba.LogLevel:
        """
        How to handle unused properties during instantiation: Error (default), Warn, or Debug
        """

    @unused_properties.setter
    def unused_properties(self, arg: mitsuba.LogLevel, /) -> None: ...

    @property
    def max_include_depth(self) -> int:
        """Maximum include depth to prevent infinite recursion (default: 15)"""

    @max_include_depth.setter
    def max_include_depth(self, arg: int, /) -> None: ...

    @property
    def variant(self) -> str:
        """Target variant for instantiation (e.g., "scalar_rgb", "cuda_spectral")"""

    @variant.setter
    def variant(self, arg: str, /) -> None: ...

    @property
    def parallel(self) -> bool:
        """Enable parallel instantiation for better performance (default: true)"""

    @parallel.setter
    def parallel(self, arg: bool, /) -> None: ...

    @property
    def merge_equivalent(self) -> bool:
        """Enable merging of equivalent nodes (deduplication) (default: true)"""

    @merge_equivalent.setter
    def merge_equivalent(self, arg: bool, /) -> None: ...

    @property
    def merge_meshes(self) -> bool:
        """Enable merging of meshes into a single merge shape (default: true)"""

    @merge_meshes.setter
    def merge_meshes(self, arg: bool, /) -> None: ...

class SceneNode:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, arg: SceneNode) -> None:
        """Copy constructor"""

    @property
    def type(self) -> mitsuba.ObjectType:
        """Object type"""

    @type.setter
    def type(self, arg: mitsuba.ObjectType, /) -> None: ...

    @property
    def file_index(self) -> int:
        """File index in ParserState::files"""

    @file_index.setter
    def file_index(self, arg: int, /) -> None: ...

    @property
    def offset(self) -> int:
        """Byte offset of the node within the parsed file/string"""

    @offset.setter
    def offset(self, arg: int, /) -> None: ...

    @property
    def props(self) -> mitsuba.Properties:
        """Properties of this node"""

    @props.setter
    def props(self, arg: mitsuba.Properties, /) -> None: ...

    def __eq__(self, arg: SceneNode, /) -> bool: ...

    def __ne__(self, arg: SceneNode, /) -> bool: ...

class SceneNodeList:
    @overload
    def __init__(self) -> None:
        """Default constructor"""

    @overload
    def __init__(self, arg: SceneNodeList) -> None:
        """Copy constructor"""

    @overload
    def __init__(self, arg: Iterable[SceneNode], /) -> None:
        """Construct from an iterable object"""

    def __len__(self) -> int: ...

    def __bool__(self) -> bool:
        """Check whether the vector is nonempty"""

    def __repr__(self) -> str: ...

    def __iter__(self) -> Iterator[SceneNode]: ...

    @overload
    def __getitem__(self, arg: int, /) -> SceneNode: ...

    @overload
    def __getitem__(self, arg: slice, /) -> SceneNodeList: ...

    def clear(self) -> None:
        """Remove all items from list."""

    def append(self, arg: SceneNode, /) -> None:
        """Append `arg` to the end of the list."""

    def insert(self, arg0: int, arg1: SceneNode, /) -> None:
        """Insert object `arg1` before index `arg0`."""

    def pop(self, index: int = -1) -> SceneNode:
        """Remove and return item at `index` (default last)."""

    def extend(self, arg: SceneNodeList, /) -> None:
        """Extend `self` by appending elements from `arg`."""

    @overload
    def __setitem__(self, arg0: int, arg1: SceneNode, /) -> None: ...

    @overload
    def __setitem__(self, arg0: slice, arg1: SceneNodeList, /) -> None: ...

    @overload
    def __delitem__(self, arg: int, /) -> None: ...

    @overload
    def __delitem__(self, arg: slice, /) -> None: ...

    def __eq__(self, arg: object, /) -> bool: ...

    def __ne__(self, arg: object, /) -> bool: ...

    @overload
    def __contains__(self, arg: SceneNode, /) -> bool: ...

    @overload
    def __contains__(self, arg: object, /) -> bool: ...

    def count(self, arg: SceneNode, /) -> int:
        """Return number of occurrences of `arg`."""

    def remove(self, arg: SceneNode, /) -> None:
        """Remove first occurrence of `arg`."""

class ParserState:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, arg: ParserState) -> None:
        """Copy constructor"""

    @property
    def nodes(self) -> SceneNodeList:
        """List of all scene nodes"""

    @nodes.setter
    def nodes(self, arg: SceneNodeList, /) -> None: ...

    @property
    def node_paths(self) -> list[str]:
        """Node paths for dictionary parsing"""

    @node_paths.setter
    def node_paths(self, arg: Sequence[str], /) -> None: ...

    @property
    def files(self) -> list[mitsuba.str]:
        """List of parsed files"""

    @files.setter
    def files(self, arg: Sequence[mitsuba.str], /) -> None: ...

    @property
    def id_to_index(self) -> dict:
        """Map from IDs to node indices"""

    @id_to_index.setter
    def id_to_index(self, arg: dict, /) -> None: ...

    @property
    def versions(self) -> list[mitsuba.Version]:
        """Version number for each file"""

    @versions.setter
    def versions(self, arg: Sequence[mitsuba.Version], /) -> None: ...

    @property
    def root(self) -> SceneNode:
        """Access the root node"""

    def __eq__(self, arg: ParserState, /) -> bool: ...

    def __ne__(self, arg: ParserState, /) -> bool: ...

def parse_file(config: ParserConfig, filename: str, **kwargs) -> ParserState:
    """Parse a scene from an XML file"""

def parse_string(config: ParserConfig, string: str, **kwargs) -> ParserState:
    """Parse a scene from an XML string"""

def parse_dict(config: ParserConfig, dict: dict) -> ParserState:
    """Parse a scene from a Python dictionary"""

def transform_upgrade(config: ParserConfig, state: ParserState) -> None:
    """Upgrade scene data to latest version"""

def transform_resolve_references(config: ParserConfig, state: ParserState) -> None:
    """
    Resolve named references and raise an error when detecting broken links
    """

def transform_resolve(config: ParserConfig, state: ParserState) -> None:
    """
    Resolve named references and raise an error when detecting broken links
    """

def transform_merge_equivalent(config: ParserConfig, state: ParserState) -> None:
    """Merge equivalent nodes to reduce memory usage and improve performance"""

def transform_merge_meshes(config: ParserConfig, state: ParserState) -> None:
    """Combine meshes with identical materials"""

def transform_reorder(config: ParserConfig, state: ParserState) -> None:
    """Reorder immediate children of scene nodes for better readability"""

def transform_relocate(config: ParserConfig, state: ParserState, output_directory: mitsuba.str) -> None:
    """Relocate scene files to organized subfolders"""

def transform_all(config: ParserConfig, state: ParserState) -> None:
    """Apply all transformations in the correct order"""

def file_location(state: ParserState, node: SceneNode) -> str:
    """Get human-readable file location for a node"""

def instantiate(config: ParserConfig, state: ParserState) -> object:
    """Instantiate the parsed representation into concrete Mitsuba objects"""

def write_file(state: ParserState, filename: mitsuba.str, add_section_headers: bool = False) -> None:
    """Write scene data to an XML file"""

def write_string(state: ParserState, add_section_headers: bool = False) -> str:
    """Convert scene data to an XML string"""
