import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "NIFTY-Options-Project"
AUTHOR_USER_NAME = "Yashwanth C Reddy Gotike"
SRC_REPO = "NiftyAlgoTrading"
AUTHOR_EMAIL = "gycrgotike@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for Nifty Options Trading",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/ycrgotike/NIFTY-Options-Project",
    project_urls={
        "Bug Tracker": f"https://github.com/ycrgotike/NIFTY-Options-Project/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)