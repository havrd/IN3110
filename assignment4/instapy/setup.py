import setuptools

setuptools.setup(
    name="instapy",
    version="1.0",
    author="Håvard Bergsvik Heimli",
    author_email="haavabhe@uio.no",
    description="Can apply greyscale and sepia filter",
    packages=setuptools.find_packages(),
    scripts=['bin/instapy'],
)
