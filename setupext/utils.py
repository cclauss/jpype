# -*- coding: utf-8 -*-
# *****************************************************************************
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
#   See NOTICE file for details.
#
# *****************************************************************************
import os
import codecs
import glob


def read_utf8(path, *parts):
    filename = os.path.join(os.path.dirname(path), *parts)
    return codecs.open(filename, encoding='utf-8').read()


def find_sources(roots=None):
    if not roots:
        roots = []
    cpp_files = []
    for root in roots:
        for filename in glob.iglob(str(root)):
            cpp_files.append(filename)
    return cpp_files

def getLogger(name):
    import logging
    if not getLogger._configure_called:
        from setuptools.logging import configure
        configure()
        getLogger._configure_called = True

    return logging.getLogger(name)


getLogger._configure_called = False
