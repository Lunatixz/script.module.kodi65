# -*- coding: utf8 -*-

# Copyright (C) 2015 - Philipp Temminghoff <phil65@kodi.tv>
# This program is Free Software see LICENSE file for details

from __future__ import absolute_import
from __future__ import unicode_literals

import xbmcgui


class WindowMixin(object):

    def __init__(self, *args, **kwargs):
        super(WindowMixin, self).__init__()
        self.cancelled = False

    def FocusedItem(self, control_id):
        try:
            control = self.getControl(control_id)
            listitem = control.getSelectedItem()
            if not listitem:
                listitem = self.getListItem(self.getCurrentListPosition())
            return listitem
        except Exception:
            return None

    def set_visible(self, control_id, condition):
        try:
            self.getControl(control_id).setVisible(bool(condition))
            return True
        except Exception:
            return False

    def check_visible(self, control_id):
        try:
            self.getControl(control_id)
            return True
        except Exception:
            return False

    def exit(self):
        self.cancelled = True
        self.close()


class WindowXML(xbmcgui.WindowXML, WindowMixin):

    def __init__(self, *args, **kwargs):
        super(WindowXML, self).__init__()
        self.window_type = "window"

    def onInit(self):
        self.window_id = xbmcgui.getCurrentWindowId()


class DialogXML(xbmcgui.WindowXMLDialog, WindowMixin):

    def __init__(self, *args, **kwargs):
        super(DialogXML, self).__init__()
        self.window_type = "dialog"

    def onInit(self):
        self.window_id = xbmcgui.getCurrentWindowDialogId()
