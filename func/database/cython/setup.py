from distutils.core import setup
from Cython.Distutils import build_ext
from distutils.extension import Extension
setup(
    ext_modules=[Extension("abc", sources = ["abc.pyx"])],
    cmdclass = {'build_ext': build_ext}
    )