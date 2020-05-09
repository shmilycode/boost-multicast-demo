cmake_minimum_required (VERSION 3.4)

project ("sdl_player")

#include_directories(${PROJECT_SOURCE_DIR}/../../broadcast/src/out/android/gen/third_party/boost/include/boost-1_70)
#link_directories(${PROJECT_SOURCE_DIR}../../broadcast/src/out/android/gen/third_party/boost/lib)
include_directories(${PROJECT_SOURCE_DIR}/../../broadcast/src/out/win/gen/third_party/boost/include/boost-1_70)
link_directories(${PROJECT_SOURCE_DIR}/../../broadcast/src/out/win/gen/third_party/boost/lib)
ADD_DEFINITIONS(-D_WIN32_WINNT=0x0601)
set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} /MD")
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} /MDd")

set(CMAKE_BUILD_TYPE "Debug")
set (BASE_SOURCE_FILE
  receiver.cpp
)

add_executable(receiver ${BASE_SOURCE_FILE})
