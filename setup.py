from setuptools import setup, find_packages

setup(
    name='sample_pkg',
    version='0.0.1',
    author='Your Name',
    author_email='your.email@example.com',
    description='A sample Python package for Nexus upload',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/python-nexus-sample',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
