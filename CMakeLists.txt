cmake_minimum_required(VERSION 3.15)

project(OpenCL)

set(OPENCL_HEADER_DIR ${PROJECT_SOURCE_DIR}/include)
set(LIB_LOADER_DIR ${PROJECT_SOURCE_DIR}/external/lib-loader)
aux_source_directory(${PROJECT_SOURCE_DIR}/src OPENCL_SRC_DIR)

add_subdirectory(${LIB_LOADER_DIR})

if (CMAKE_PROJECT_NAME STREQUAL PROJECT_NAME)
    set(BUILD_LIBRARY ON)
else()
    set(BUILD_LIBRARY OFF)
endif()

if (BUILD_LIBRARY)
    set(LIBRARY_OUTPUT_PATH ${PROJECT_BINARY_DIR}/output)
    include_directories(${OPENCL_HEADER_DIR})
    add_library(OpenCL STATIC ${OPENCL_SRC_DIR})
    add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy_directory ${OPENCL_HEADER_DIR} ${LIBRARY_OUTPUT_PATH}/include
    )
    target_link_libraries(OpenCL PRIVATE LibLoader)
else()
    add_library(OpenCL INTERFACE)
    target_include_directories(OpenCL INTERFACE ${OPENCL_HEADER_DIR})
    target_sources(OpenCL INTERFACE ${OPENCL_SRC_DIR})
    target_link_libraries(OpenCL INTERFACE LibLoader)
    if(CMAKE_CXX_COMPILER_ID STREQUAL "Clang" OR
    CMAKE_CXX_COMPILER_ID STREQUAL "GNU"   OR
    CMAKE_CXX_COMPILER_ID STREQUAL "AppleClang")
        target_compile_options(OpenCL INTERFACE -O2 -Wall)
    endif()
endif()



