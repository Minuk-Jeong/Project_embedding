#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "drjit-core" for configuration "Release"
set_property(TARGET drjit-core APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(drjit-core PROPERTIES
  IMPORTED_LINK_DEPENDENT_LIBRARIES_RELEASE "nanothread"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/drjit/libdrjit-core.so"
  IMPORTED_SONAME_RELEASE "libdrjit-core.so"
  )

list(APPEND _cmake_import_check_targets drjit-core )
list(APPEND _cmake_import_check_files_for_drjit-core "${_IMPORT_PREFIX}/drjit/libdrjit-core.so" )

# Import target "drjit-extra" for configuration "Release"
set_property(TARGET drjit-extra APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(drjit-extra PROPERTIES
  IMPORTED_LINK_DEPENDENT_LIBRARIES_RELEASE "drjit-core;nanothread"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/drjit/libdrjit-extra.so"
  IMPORTED_SONAME_RELEASE "libdrjit-extra.so"
  )

list(APPEND _cmake_import_check_targets drjit-extra )
list(APPEND _cmake_import_check_files_for_drjit-extra "${_IMPORT_PREFIX}/drjit/libdrjit-extra.so" )

# Import target "nanothread" for configuration "Release"
set_property(TARGET nanothread APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(nanothread PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/drjit/libnanothread.so"
  IMPORTED_SONAME_RELEASE "libnanothread.so"
  )

list(APPEND _cmake_import_check_targets nanothread )
list(APPEND _cmake_import_check_files_for_nanothread "${_IMPORT_PREFIX}/drjit/libnanothread.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
