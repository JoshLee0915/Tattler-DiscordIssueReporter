from setuptools import setup

setup(
    name='Tattler-DiscordIssueReporter',
    version='0.0.1-alpha',
    packages=['TattlerDIR'],
    url='https://github.com/JoshLee0915/Tattler-DiscordIssueReporter',
    license='MIT',
    author='Josh Lee',
    author_email='',
    description='',
    install_requires=['youtrack-rest-python-library'],
    dependency_links=['git+https://github.com/JoshLee0915/youtrack-rest-python-library.git#egg=youtrack-rest-python-library']
)
