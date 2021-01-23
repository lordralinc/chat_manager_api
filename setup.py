import setuptools

try:
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()
except UnicodeDecodeError:
    with open("README.md", "r") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ""

setuptools.setup(
    name="chat_manager_api",
    version="1.0.0",
    author="lordralinc",
    description="Chat Manager API wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/lordralinc/chat_manager_api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests", "pydantic", "aiohttp"],
    include_package_data=True,
)
