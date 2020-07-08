# Copyright (c) Microsoft Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import http.server
import os

class Server:
  def __init__(self):
    self.PORT = 8907
    self.EMPTY_PAGE = f'http://localhost:{self.PORT}/empty.html'
    self.PREFIX = f'http://localhost:{self.PORT}'
    self.CROSS_PROCESS_PREFIX = f'http://127.0.0.1:{self.PORT}'

server = Server()

class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, directory=os.path.join(os.path.dirname(__file__), 'assets'), **kwargs)

  def log_message(self, *args):
    return

  def log_error(self, *args):
    return