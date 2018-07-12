from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


def version():
    import re
    for line in open('egbis/__init__.py'):
        match = re.match("__version__ *= *'(.*)'", line)
        if match:
            return match.groups()[0]
    raise RuntimeError('__version__ is not found')


def long_description():
    with open('README.md') as fp:
        content = fp.read()
    return content


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        raise SystemExit(errno)


install_requires = [
    'numpy'
]

tests_require = [
    'pytest'
]

setup(
    name='egbis',
    version=version(),
    author='devforfu',
    maintainer='devforfu',
    description='Efficient Graph-Based Image Segmentation Algorithm in Python',
    long_description=long_description(),
    packages=find_packages(),
    install_requires=install_requires,
    tests_require=tests_require,
    keywords=['numpy', 'image-segmentation', 'disjoint-set'],
    cmdclass={'test': PyTest})
