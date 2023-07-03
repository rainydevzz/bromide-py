import setuptools

with open("readme.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='bromide.py',
    version='0.1',
    author='Ryan S',
    description='A Sync/Async API Wrapper for SodiumDB.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/sodium-db/bromide-py',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)