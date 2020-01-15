import setuptools
import re
import os
import ast

# parse version from locust/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')
_init_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "pacswg", "__init__.py")
with open(_init_file, 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

# Read the contents of requirements.txt
with open('requirements.txt') as content_file:
    content = content_file.read()

content = content.replace('\r', '')
reqs = content.split("\n")
reqs = [i for i in reqs if len(i) > 0]

setuptools.setup(
    name="pacswg",
    version=version,
    url="https://github.com/nimamahmoudi/pacswg",
    author="Nima Mahmoudi",
    author_email="nima_mahmoudi@live.com",
    description="A workload generator made in PACS lab in York University.",
    long_description=open('README.rst').read(),
    packages=setuptools.find_packages(),
    install_requires=reqs,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={},

)