#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "OpenEXR::IlmImf" for configuration "Release"
set_property(TARGET OpenEXR::IlmImf APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenEXR::IlmImf PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/mitsuba/libIlmImf-mitsuba.so"
  IMPORTED_SONAME_RELEASE "libIlmImf-mitsuba.so"
  )

list(APPEND _cmake_import_check_targets OpenEXR::IlmImf )
list(APPEND _cmake_import_check_files_for_OpenEXR::IlmImf "${_IMPORT_PREFIX}/mitsuba/libIlmImf-mitsuba.so" )

# Import target "OpenEXR::IlmImfUtil" for configuration "Release"
set_property(TARGET OpenEXR::IlmImfUtil APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(OpenEXR::IlmImfUtil PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/mitsuba/libIlmImfUtil-mitsuba.so"
  IMPORTED_SONAME_RELEASE "libIlmImfUtil-mitsuba.so"
  )

list(APPEND _cmake_import_check_targets OpenEXR::IlmImfUtil )
list(APPEND _cmake_import_check_files_for_OpenEXR::IlmImfUtil "${_IMPORT_PREFIX}/mitsuba/libIlmImfUtil-mitsuba.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
