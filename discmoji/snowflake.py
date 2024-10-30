"""MIT License

Copyright (c) 2024 mojidev-py

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import datetime


class Snowflake(int):
    """Represents a discord resource id. It is recommended to use the builtin `int` object instead of this. \n
    Inherits from `int`
    ## Methods
    `find_date()`
      - Finds the date of a given snowflake."""
    def find_date(self):
        DISCORD_EPOCH = 1420070400000
        """Finds when the provided snowflake was created.
        ### Returns
          - `datetime.datetime` - The converted date."""
        binary = bytes(bin(self).strip("0b"))
        unixdate = (binary >> 22) + DISCORD_EPOCH
        return datetime.datetime.fromtimestamp(unixdate)
