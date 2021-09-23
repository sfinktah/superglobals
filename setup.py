from setuptools import setup, find_packages
VERSION="0.0.15"
with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name='superglobals',
    version=VERSION,
    url='https://github.com/sfinktah/superglobals',
    long_description=long_description,
    long_description_content_type="text/x-rst",
    license='MIT',
    author='Christopher Anderson',
    author_email='sfinktah@github.spamtrak.org',
    description='globals() access anywhere. "We Do Anything, Anytime"',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=2.7",
    # package_dir={"": "src"},
    packages=find_packages(),
)
