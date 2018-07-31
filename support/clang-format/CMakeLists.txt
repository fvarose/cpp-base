option(
    CHECK_CLANG_FORMAT
    "Toggle ON to run a test that verifies that all files are correctly formatted (requires Docker)"
    ON
)

if(CHECK_CLANG_FORMAT) 
    find_package(UnixCommands)
    if (${UnixCommands_FOUND})
        message(STATUS "Found bash, will run the clang-format check")
        add_test(NAME clang_format_compliance
                COMMAND ${BASH} ${CMAKE_SOURCE_DIR}/check-clang-format.sh
                WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})
    else ()
        message(WARNING "Could not find bash, not running the clang-format check")
    endif()
endif()
