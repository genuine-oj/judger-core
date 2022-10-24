cmake_minimum_required(VERSION 2.5)
project(judger C)

set(CMAKE_C_FLAGS "-g -Wall -Werror -O3 -std=c99")

file(GLOB SOURCE "src/*.c" "src/rules/*.c")
add_library(judger SHARED ${SOURCE})
target_link_libraries(judger pthread seccomp)

install(FILES build/libjudger.so
    PERMISSIONS OWNER_READ
    DESTINATION /usr/lib/judger)
