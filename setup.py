from setuptools import setup, find_packages

setup(
    name='chochaq-portscanner',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'portscanner=portscanner:main',
        ],
    },
    install_requires=[],
    author='ExploitX',
    description='Simple Python Port Scanner CLI tool',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ],
)
