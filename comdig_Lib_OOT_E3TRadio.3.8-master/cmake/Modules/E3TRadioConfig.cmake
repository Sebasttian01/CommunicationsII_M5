INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_E3TRADIO E3TRadio)

FIND_PATH(
    E3TRADIO_INCLUDE_DIRS
    NAMES E3TRadio/api.h
    HINTS $ENV{E3TRADIO_DIR}/include
        ${PC_E3TRADIO_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    E3TRADIO_LIBRARIES
    NAMES gnuradio-E3TRadio
    HINTS $ENV{E3TRADIO_DIR}/lib
        ${PC_E3TRADIO_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/E3TRadioTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(E3TRADIO DEFAULT_MSG E3TRADIO_LIBRARIES E3TRADIO_INCLUDE_DIRS)
MARK_AS_ADVANCED(E3TRADIO_LIBRARIES E3TRADIO_INCLUDE_DIRS)
