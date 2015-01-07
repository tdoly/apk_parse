# This file is part of Androguard.
#
# Copyright 2014 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import hashlib


def read(filename, binary=True):
    with open(filename, 'rb' if binary else 'r') as f:
        return f.read()


def get_md5(buf):
    m = hashlib.md5()
    m.update(buf)
    return m.hexdigest().lower()