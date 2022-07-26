import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

    name="nordvpn_switcher_plus", # Replace with your username

    version="0.3.1",

    author="andreferraro",

    author_email="aferrarobr@gmail.com",

    description="Rotate between different NordVPN servers with ease. Works both on Linux and Windows without any required changes to your code!",

    long_description=long_description,

    long_description_content_type="text/markdown",

    url="https://github.com/andreferraro/NordVPN-switcher",

    packages=setuptools.find_packages(),

    classifiers=[

        "Programming Language :: Python :: 3",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",

    ],

    python_requires='>=3.6',

)
