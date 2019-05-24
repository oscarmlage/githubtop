from setuptools import setup

requires = [
    'requests',
]

# Being too optimistic here
tests_require = []

setup(
    name='githubtop',
    version='0.0.1',
    description='List of Github users by Location',
    author='oscarmlage',
    url='https://oscarmlage.com',
    install_requires=requires
)
