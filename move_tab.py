"""
Move Tab

Plugin for Sublime Text to move tabs around

Copyright (c) 2012 Frédéric Massart - FMCorz.net

Licensed under The MIT License
Redistributions of files must retain the above copyright notice.

http://github.com/FMCorz/MoveTab
"""
import sublime_plugin


class MoveTabCommand(sublime_plugin.WindowCommand):

    def run(self, position):
        view = self.window.active_view()
        group, index = self.window.get_view_index(view)
        if index < 0:
            return
        count = len(self.window.views_in_group(group))

        if isinstance(position, str) and position[0] in '-+':
            position = (index + int(position)) % count
        else:
            position = min(count - 1, max(0, int(position)))

        # Avoid flashing tab when moving to same index
        if position != index:
            self.window.set_view_index(view, group, position)
            self.window.focus_view(view)

    def is_enabled(self):
        (group, index) = self.window.get_view_index(self.window.active_view())
        return -1 not in (group, index) and len(self.window.views_in_group(group)) > 1
