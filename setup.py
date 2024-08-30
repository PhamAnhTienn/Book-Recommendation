from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

REPO_NAME = "Book-Recommendation"
AUTHOR_USER_NAME = "Tien"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="Tien",
    description="A small local packages for ML based books recommendations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PhamAnhTienn/Book-Recommendation",
    author_email="",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.8",
    install_requires=LIST_OF_REQUIREMENTS
)