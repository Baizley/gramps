#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2000-2007  Donald N. Allingham
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

import unittest

from gramps.gen.display.name import NameDisplay


class NameTest(unittest.TestCase):

    def setUp(self):
        self.name_display = NameDisplay()

    def test_get_name_format_for_all_without_default_format(self):
        self.add_custom_name_format('Surname, Name|Common Suffix')
        self.add_inactive_custom_name_format('SURNAME, Given Suffix (Call)')

        actual_name_format = self.name_display.get_name_format(also_default=False, only_custom=False, only_active=False)

        expected_name_format = [
            (1, 'Surname, Given Suffix', '%l, %f %s', True),
            (2, 'Given Surname Suffix', '%f %l %s', True),
            (3, 'Patronymic, Given', '%y, %s %f', False),
            (4, 'Given', '%f', True),
            (5, 'Main Surnames, Given Patronymic Suffix Prefix', '%1m %2m %o, %f %1y %s %0m', True),
            (-2, 'SURNAME, Given Suffix (Call)', 'SURNAME, Given Suffix (Call)', False),
            (-1, 'Surname, Name|Common Suffix', 'Surname, Name|Common Suffix', True)
        ]
        self.assertEqual(expected_name_format, actual_name_format)

    def test_get_name_format_for_all_active_without_default_format(self):

        self.add_custom_name_format('Surname, Name|Common Suffix')
        self.add_inactive_custom_name_format('SURNAME, Given Suffix (Call)')

        actual_name_format = self.name_display.get_name_format(also_default=False, only_custom=False, only_active=True)

        expected_name_format = [
            (1, 'Surname, Given Suffix', '%l, %f %s', True),
            (2, 'Given Surname Suffix', '%f %l %s', True),
            (4, 'Given', '%f', True),
            (5, 'Main Surnames, Given Patronymic Suffix Prefix', '%1m %2m %o, %f %1y %s %0m', True),
            (-1, 'Surname, Name|Common Suffix', 'Surname, Name|Common Suffix', True)
        ]
        self.assertEqual(expected_name_format, actual_name_format)

    def test_get_name_format_for_all_custom_formats_without_default_format(self):

        self.add_custom_name_format('Surname, Name|Common Suffix')
        self.add_inactive_custom_name_format('SURNAME, Given Suffix (Call)')

        actual_name_format = self.name_display.get_name_format(also_default=False, only_custom=True, only_active=False)

        expected_name_format = [
            (-2, 'SURNAME, Given Suffix (Call)', 'SURNAME, Given Suffix (Call)', False),
            (-1, 'Surname, Name|Common Suffix', 'Surname, Name|Common Suffix', True)
        ]
        self.assertEqual(expected_name_format, actual_name_format)

    def test_get_name_format_for_active_custom_formats_without_default_format(self):
        self.add_custom_name_format('Surname, Name|Common Suffix')
        self.add_inactive_custom_name_format('SURNAME, Given Suffix (Call)')

        actual_name_format = self.name_display.get_name_format(also_default=False, only_custom=True, only_active=True)

        expected_name_format = [
            (-1, 'Surname, Name|Common Suffix', 'Surname, Name|Common Suffix', True)
        ]
        self.assertEqual(expected_name_format, actual_name_format)

    def test_get_name_format_for_all(self):
        self.add_custom_name_format('Surname, Name|Common Suffix')
        self.add_inactive_custom_name_format('SURNAME, Given Suffix (Call)')

        actual_name_format = self.name_display.get_name_format(also_default=True, only_custom=False, only_active=False)

        expected_name_format = [
            (0, 'Default format (defined by Gramps preferences)', '', True),
            (1, 'Surname, Given Suffix', '%l, %f %s', True),
            (2, 'Given Surname Suffix', '%f %l %s', True),
            (3, 'Patronymic, Given', '%y, %s %f', False),
            (4, 'Given', '%f', True),
            (5, 'Main Surnames, Given Patronymic Suffix Prefix', '%1m %2m %o, %f %1y %s %0m', True),
            (-2, 'SURNAME, Given Suffix (Call)', 'SURNAME, Given Suffix (Call)', False),
            (-1, 'Surname, Name|Common Suffix', 'Surname, Name|Common Suffix', True)
        ]
        self.assertEqual(expected_name_format, actual_name_format)

    def test_get_name_format_for_all_active(self):
        self.add_custom_name_format('Surname, Name|Common Suffix')
        self.add_inactive_custom_name_format('SURNAME, Given Suffix (Call)')

        actual_name_format = self.name_display.get_name_format(also_default=True, only_custom=False, only_active=True)

        expected_name_format = [
            (0, 'Default format (defined by Gramps preferences)', '', True),
            (1, 'Surname, Given Suffix', '%l, %f %s', True),
            (2, 'Given Surname Suffix', '%f %l %s', True),
            (4, 'Given', '%f', True),
            (5, 'Main Surnames, Given Patronymic Suffix Prefix', '%1m %2m %o, %f %1y %s %0m', True),
            (-1, 'Surname, Name|Common Suffix', 'Surname, Name|Common Suffix', True)
        ]
        self.assertEqual(expected_name_format, actual_name_format)

    def test_get_name_format_for_all_custom_formats(self):
        self.add_custom_name_format('Surname, Name|Common Suffix')
        self.add_inactive_custom_name_format('SURNAME, Given Suffix (Call)')

        actual_name_format = self.name_display.get_name_format(also_default=True, only_custom=True, only_active=False)

        expected_name_format = [
            (-2, 'SURNAME, Given Suffix (Call)', 'SURNAME, Given Suffix (Call)', False),
            (-1, 'Surname, Name|Common Suffix', 'Surname, Name|Common Suffix', True)
        ]
        self.assertEqual(expected_name_format, actual_name_format)

    def test_get_name_format_for_active_custom_formats(self):
        self.add_custom_name_format('Surname, Name|Common Suffix')
        self.add_inactive_custom_name_format('SURNAME, Given Suffix (Call)')

        actual_name_format = self.name_display.get_name_format(also_default=True, only_custom=True, only_active=True)

        expected_name_format = [
            (-1, 'Surname, Name|Common Suffix', 'Surname, Name|Common Suffix', True)
        ]
        self.assertEqual(expected_name_format, actual_name_format)

    def add_custom_name_format(self, name_format):
        self.name_display.add_name_format(name_format, name_format)

    def add_inactive_custom_name_format(self, name_format):
        index = self.name_display.add_name_format(name_format, name_format)
        self.name_display.set_format_inactive(index)


if __name__ == '__main__':
    unittest.main()
