cmake_minimum_required(VERSION 3.15)

set(LIB_LOADER_DIR external/lib_loader)
add_subdirectory(${PROJECT_SOURCE_DIR}/${LIB_LOADER_DIR})
include_directories(
    ${PROJECT_BINARY_DIR}/${LIB_LOADER_DIR}/output
)
link_directories(
    ${PROJECT_BINARY_DIR}/${LIB_LOADER_DIR}/output
)

add_library(OpenCL STATIC src/libopencl.c)
target_include_directories(OpenCL PRIVATE "include")

target_link_libraries(OpenCL LibLoader)

if(CMAKE_CXX_COMPILER_ID STREQUAL "Clang" OR
   CMAKE_CXX_COMPILER_ID STREQUAL "GNU"   OR
   CMAKE_CXX_COMPILER_ID STREQUAL "AppleClang")
  target_compile_options(OpenCL PRIVATE -O2 -Wall)
endif()

