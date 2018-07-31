add_executable(lib_test
    main.cpp
)

target_link_libraries(lib_test lib Catch)

add_test(NAME lib_test
         COMMAND $<TARGET_FILE:lib_test>)

# Run the clang-format check if bash is available
# Note: docker is also required, but there is no way to check here if it's available
find_package(UnixCommands)
if (${UnixCommands_FOUND})
    message(STATUS "Found bash, will run the clang-format check")
    add_test(NAME clang_format_compliance
             COMMAND ${BASH} ${CMAKE_SOURCE_DIR}/check-clang-format.sh
             WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})
else ()
    message(WARNING "Could not find bash, not running the clang-format check")
endif()