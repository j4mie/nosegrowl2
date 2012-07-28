# nosegrowl2

**A simple Nose plugin for Growl notifications**

Existing Growl plugins for Nose can be difficult to install, due to packaging problems and a dependency on the PyGrowl library, which is out of date on PyPI.

This extremely simple plugin uses [gntplib](http://packages.python.org/gntplib/) to send its notifications.

To use this plugin, install with `pip install nosegrowl2`, then run `nosetests --with-growl`.

You may need to remove existing Nose Growl packages first.

*Note*: prior to version 0.3, the `growlnotify` command-line tool was used to send notifications. As this is now deprecated and has been removed from Homebrew, nosegrowl2 now uses gntplib.

## (Un)license

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute this
software, either in source code form or as a compiled binary, for any purpose,
commercial or non-commercial, and by any means.

In jurisdictions that recognize copyright laws, the author or authors of this
software dedicate any and all copyright interest in the software to the public
domain. We make this dedication for the benefit of the public at large and to
the detriment of our heirs and successors. We intend this dedication to be an
overt act of relinquishment in perpetuity of all present and future rights to
this software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
