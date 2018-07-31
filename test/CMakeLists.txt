add_executable(lib_test
    main.cpp
)

target_link_libraries(lib_test lib Catch)

add_test(NAME lib_test
         COMMAND $<TARGET_FILE:lib_test>)

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