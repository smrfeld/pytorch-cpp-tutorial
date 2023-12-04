from torch.utils.cpp_extension import CppExtension, BuildExtension
from setuptools import setup

setup(
    name='my_extension',
    version='0.1',
    packages=['my_extension'],
    ext_modules=[
        CppExtension(
            'my_extension',
            ['my_extension/cpp_extension.cpp'],
        ),
    ],
    cmdclass={'build_ext': BuildExtension},
)