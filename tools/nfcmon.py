#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 SoloKeys, Inc. <https://solokeys.com/>
#
# This file is part of Solo.
#
# Solo is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Solo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Solo.  If not, see <https://www.gnu.org/licenses/>
#
# This code is available under licenses for commercial use.
# Please contact SoloKeys for more information.
#
import datetime, sys
from binascii import hexlify

import Chameleon


def verboseLog(text):
    formatString = "[{}] {}"
    timeString = datetime.datetime.utcnow()
    print(formatString.format(timeString, text))


chameleon = Chameleon.Device(verboseLog)

p = None
for p in Chameleon.Device.listDevices():
    break

if p:
    chameleon.connect(p)
else:
    raise RuntimeError('No chameleon mini connected')

chameleon.execCmd('LOGMODE=LIVE')

while 1:
    b = chameleon.read(1, 20)
    h = hexlify(b)
    h = h.decode()
    sys.stdout.write(h)
    sys.stdout.flush()

chameleon.execCmd('LOGMODE=NONE')
