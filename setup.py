"""Setup configuration for todo-cli."""

from setuptools import find_packages, setup

setup(
    name="todo-cli",
    version="0.1.0",
    description="A simple command-line todo manager",
    packages=find_packages(),
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "todo=src.cli:main",
        ],
    },
)
