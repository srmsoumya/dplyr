from setuptools import find_packages, setup

test_packages = ["black", "pytest", "flake8"]
dev_packages = ["jupyterlab", "pre-commit"] + test_packages

setup(
    name="dplyr",
    version="0.1.2",
    packages=find_packages(),
    extras_require={"test": test_packages, "dev": dev_packages},
)
