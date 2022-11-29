from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

__version__ = "0.0.1"

ext_modules = [
    Pybind11Extension("heng",
    ["src/main.cpp"],
    define_macros = [('VERSION_INFO', __version__)],
    ),
]

setup(
    name="heng",
    version=__version__,
    author="Eddie_Wang",
    author_email="wangjinheng1120@163.com",
    description="A simplified AI framework",
    long_description="",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.7",
)