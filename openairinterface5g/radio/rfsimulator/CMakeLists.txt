add_library(rfsimulator MODULE
            simulator.c
            apply_channelmod.c
            ../../openair1/PHY/TOOLS/signal_energy.c
)
target_link_libraries(rfsimulator PRIVATE SIMU log_headers)
set_target_properties(rfsimulator PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})

# Optional: embed Python inside rfsimulator (apply Sionna channel directly to IQ samples)
if(OAI_PYTHON_EMBED)
  find_package(Python3 REQUIRED COMPONENTS Development)
  target_link_libraries(rfsimulator PRIVATE Python3::Python)
  target_compile_definitions(rfsimulator PRIVATE OAI_PYTHON_EMBED=1)
endif()

add_executable(replay_node stored_node.c)
target_link_libraries (replay_node minimal_lib)
