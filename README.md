Parse humanized strings like 128M to 16K to something a machine can understand

## Installation

    pip install dehumanizer

## Usage

    >>> dehumanizer.parse_string('128k')
    128000

 You can also try millions:

     >>> dehumanizer.parse_string('128m')
    128000000
