![PyPI](https://img.shields.io/pypi/v/pacswg.svg)
![PyPI - Status](https://img.shields.io/pypi/status/pacswg.svg)
![Travis (.com)](https://img.shields.io/travis/com/nimamahmoudi/pacswg.svg)
![Libraries.io dependency status for latest release](https://img.shields.io/librariesio/release/pypi/pacswg.svg)
![GitHub](https://img.shields.io/github/license/nimamahmoudi/pacswg.svg)


# PACS Workload Generator

This is a workload generator designed especifically to perform load testing for several applications. The internal use case of this workload generator is for load testing AWS Lambda functions, but it can be used for other purposes. All you have to do is give it a `worker` function and the number of requests per second you want to achieve on average and it will do the rest for you.

Pypi: https://pypi.org/project/pacswg/

Github Repository: https://github.com/nimamahmoudi/pacswg

Documentation: https://pacswg.readthedocs.io/

## Usage

Check out the [usage section in our documentations](https://pacswg.readthedocs.io/en/latest/usage.html).

## Installation

Install using pip:
```bash
$ pip install pacswg
```

Upgrading:
```bash
pip install pacswg --upgrade
```

For installation in development mode:

```
git clone https://github.com/nimamahmoudi/pacswg
cd pacswg
pip install -e .
```

## Development

`Note:` README.rst will be overwritten from time to time using converters that convert markdown to rst format. Don't modify it since the changes might be overwritten.
