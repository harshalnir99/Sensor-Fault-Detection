from setuptools import find_packages,setup

setup(
    name="sensor",
    version="0.0.1",
    author="Harshal",
    author_email="harshalnir99@gmail.com",
    packages=find_packages(),
    install_requires=["pymongo==4.2.0"],
)