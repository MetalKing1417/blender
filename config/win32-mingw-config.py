LCGDIR = '#../lib/windows'
BF_PYTHON = LCGDIR + '/python'
BF_PYTHON_VERSION = '2.4'
BF_PYTHON_INC = '${BF_PYTHON}/include/python${BF_PYTHON_VERSION}'
BF_PYTHON_BINARY = 'python'
BF_PYTHON_LIB = 'python24'
BF_PYTHON_LIBPATH = '${BF_PYTHON}/lib'

WITH_BF_OPENAL = 'true'
BF_OPENAL = LCGDIR + '/openal'
BF_OPENAL_INC = '${BF_OPENAL}/include'
BF_OPENAL_LIB = 'openal'
BF_OPENAL_LIBPATH = '${BF_OPENAL}/lib'

WITH_BF_SDL = 'true'
BF_SDL = '#../extra/SDL-1.2.9' #$(shell sdl-config --prefix)
BF_SDL_INC = '${BF_SDL}/include' #$(shell $(BF_SDL)/bin/sdl-config --cflags)
BF_SDL_LIB = 'SDLmain SDL' #$(shell $(BF_SDL)/bin/sdl-config --libs) -lSDL_mixer
BF_SDL_LIBPATH = '${BF_SDL}/lib'

WITH_BF_FMOD = 'false'
BF_FMOD = LCGDIR + '/fmod'

WITH_BF_OPENEXR = 'true'
BF_OPENEXR = LCGDIR + '/gcc/openexr'
BF_OPENEXR_INC = '${BF_OPENEXR}/include ${BF_OPENEXR}/include/OpenEXR'
BF_OPENEXR_LIB = ' Iex Half IlmImf Imath '
BF_OPENEXR_LIBPATH = LCGDIR+'/openexr/lib'

WITH_BF_JPEG = 'true'
BF_JPEG = LCGDIR + '/jpeg'
BF_JPEG_INC = '${BF_JPEG}/include'
BF_JPEG_LIB = 'jpeg'
BF_JPEG_LIBPATH = '${BF_JPEG}/lib'

WITH_BF_PNG = 'true'
BF_PNG = LCGDIR + '/png'
BF_PNG_INC = '${BF_PNG}/include'
BF_PNG_LIB = 'png'
BF_PNG_LIBPATH = '${BF_PNG}/lib'

BF_TIFF = LCGDIR + '/tiff'
BF_TIFF_INC = '${BF_TIFF}/include'

WITH_BF_ZLIB = 'true'
BF_ZLIB = LCGDIR + '/zlib'
BF_ZLIB_INC = '${BF_ZLIB}/include'
BF_ZLIB_LIB = 'z'
BF_ZLIB_LIBPATH = '${BF_ZLIB}/lib'

WITH_BF_INTERNATIONAL = 'true'

BF_GETTEXT = LCGDIR + '/gettext'
BF_GETTEXT_INC = '${BF_GETTEXT}/include'
BF_GETTEXT_LIB = 'freegettext'
BF_GETTEXT_LIBPATH = '#../extra/gettext'

WITH_BF_FTGL = 'true'
BF_FTGL = LCGDIR + '/ftgl'
BF_FTGL_INC = '${BF_FTGL}/include'
BF_FTGL_LIB = 'extern_ftgl'

WITH_BF_GAMEENGINE = 'false'

WITH_BF_ODE = 'true'
BF_ODE = LCGDIR + '/ode'
BF_ODE_INC = BF_ODE + '/include'
BF_ODE_LIB = BF_ODE + '/lib/libode.a'

WITH_BF_BULLET = 'true'
BF_BULLET = '#extern/bullet'
BF_BULLET_INC = '${BF_BULLET}/LinearMath ${BF_BULLET}/BulletDynamics ${BF_BULLET}/Bullet'
BF_BULLET_LIB = 'extern_bullet'

BF_SOLID = '#extern/solid'
BF_SOLID_INC = '${BF_SOLID}'
BF_SOLID_LIB = 'extern_solid'

#WITH_BF_NSPR = 'true'
#BF_NSPR = $(LCGDIR)/nspr
#BF_NSPR_INC = -I$(BF_NSPR)/include -I$(BF_NSPR)/include/nspr
#BF_NSPR_LIB = 

# Uncomment the following line to use Mozilla inplace of netscape
#CPPFLAGS += -DMOZ_NOT_NET
# Location of MOZILLA/Netscape header files...
#BF_MOZILLA = $(LCGDIR)/mozilla
#BF_MOZILLA_INC = -I$(BF_MOZILLA)/include/mozilla/nspr -I$(BF_MOZILLA)/include/mozilla -I$(BF_MOZILLA)/include/mozilla/xpcom -I$(BF_MOZILLA)/include/mozilla/idl
#BF_MOZILLA_LIB =
# Will fall back to look in BF_MOZILLA_INC/nspr and BF_MOZILLA_LIB
# if this is not set.
#
# Be paranoid regarding library creation (do not update archives)
#BF_PARANOID = 'true'

# enable freetype2 support for text objects
BF_FREETYPE = '#../extra/freetype'
BF_FREETYPE_INC = '${BF_FREETYPE}/include '
BF_FREETYPE_LIB = 'freetype'
BF_FREETYPE_LIBPATH = '${BF_FREETYPE}/lib'

WITH_BF_QUICKTIME = 'false' # -DWITH_QUICKTIME
BF_QUICKTIME = '/usr/local'
BF_QUICKTIME_INC = '${BF_QUICKTIME}/include'

# Mesa Libs should go here if your using them as well....
WITH_BF_OPENGL = 'true'
BF_OPENGL = 'C:\\MingW'
BF_OPENGL_INC = '${BF_OPENGL}/include'
BF_OPENGL_LIBINC = '${BF_OPENGL}/lib'
BF_OPENGL_LIB = 'opengl32 glu32'
BF_OPENGL_LIB_STATIC = [ '${BF_OPENGL}/lib/libGL.a', '${BF_OPENGL}/lib/libGLU.a',
             '${BF_OPENGL}/lib/libXmu.a', '${BF_OPENGL}/lib/libXext.a',
             '${BF_OPENGL}/lib/libX11.a', '${BF_OPENGL}/lib/libXi.a' ]
##
##CC = gcc
##CCC = g++
##ifeq ($CPU),alpha)
##   CFLAGS += -pipe -fPIC -funsigned-char -fno-strict-aliasing -mieee

CFLAGS = [ '-pipe' '-funsigned-char', '-fno-strict-aliasing' ]

CPPFLAGS = [ '-DXP_UNIX', '-DWIN32', '-DFREE_WINDOWS' ]
CCFLAGS = ['-pipe', '-mwindows', '-funsigned-char', '-fno-strict-aliasing' ]
REL_CFLAGS = [ '-O2' ]
REL_CCFLAGS = [ '-O2' ]
##BF_DEPEND = 'true'
##
##AR = ar
##ARFLAGS = ruv
##ARFLAGSQUIET = ru
##
C_WARN = [ '-Wall', '-W', '-Wshadow', '-Wpointer-arith', '-Wbad-function-cast',
        '-Wcast-qual', '-Wcast-align', '-Waggregate-return',
        '-Wstrict-prototypes', '-Wmissing-prototypes',
        '-Wmissing-declarations', '-Wnested-externs', '-Wredundant-decls' ]

CC_WARN = [ '-Wall', '-W', '-Wshadow', '-Wpointer-arith', '-Wcast-qual', '-Wcast-align',
        '-Wredundant-decls', '-Wreorder', '-Wctor-dtor-privacy', '-Wnon-virtual-dtor',
        '-Wold-style-cast', '-Woverloaded-virtual', '-Wsign-promo', '-Wsynth' ]

##FIX_STUBS_WARNINGS = -Wno-unused

LLIBS = [ '-ldxguid', '-lgdi32', '-lmsvcrt', '-lwinmm', '-lmingw32', '-lm' ] #'-lutil', '-lc', '-lm', '-ldl', '-lpthread' ]
##LOPTS = --dynamic
##DYNLDFLAGS = -shared $(LDFLAGS)

BF_DEBUG = 'false'
BF_DEBUG_FLAGS= ''

BF_BUILDDIR = '..\\build\\win32-mingw'
BF_INSTALLDIR='..\\install\\win32-mingw'
