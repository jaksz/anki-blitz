# -*- coding: utf-8 -*-

# Blitz speed reading trainer add-on for Anki
#
# Copyright (C) 2016  Jakub Szypulka <jakub AT szypulka.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from aqt.reviewer import Reviewer
import time


def myShow(self):                  # Customize the show() function by...
    origShow(self)                 # executing the function as usual (1/2),...
    self.start_time = time.time()  # but starting a timer.

origShow = Reviewer.show           # Execute the function as usual (2/2)
Reviewer.show = myShow             # Execute the function as usual (3/3)

def myDefaultEase(self):
    elapsed_time = time.time() - self.start_time  # How much time elapsed?
    if elapsed_time < 1:                          # If less than 1s...
        return 3                                  # suggest "Easy"/"Normal".
    if elapsed_time < 3:                          # If less than 3s...
        return 2                                  # suggest "Hard".
    else:                                         # If more than 3s...
        return 1                                  # suggest "Again".

Reviewer._defaultEase = myDefaultEase             # Replace default ease function
