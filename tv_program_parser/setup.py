from setuptools import find_packages, setup

setup(
    name='tvprogramlib',
    packages=find_packages(include=['tvprogramlib']),
    version='0.1.0',
    description='Library with tv program parser',
    author='Pavel Nikulin',
    install_requires=['requests', 'pydantic']
)

# https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f
# https://towardsdatascience.com/deep-dive-create-and-publish-your-first-python-library-f7f618719e14
# https://realpython.com/python-modules-packages/
# https://realpython.com/pypi-publish-python-package/
