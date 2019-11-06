from setuptools import setup, find_packages

VERSION = "0.0.2"

with open("requirements.txt", "r") as req:
    install_reqs = req.read().splitlines()

setup(
    name="fairflake",
    version=VERSION,
    author="Marcin Szymanski",
    description="Make Snowflake greater than great",
    install_requires=install_reqs,
    python_requires=">= 3.7",
    packages=find_packages(),
    entry_points={"console_scripts": ["fairflake=fairflake.cli:cli"]},
)
