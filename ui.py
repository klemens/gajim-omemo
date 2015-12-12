import gtk

# from plugins.helpers import log


class PreKeyButton(gtk.Button):
    def __init__(self, plugin, contact):
        super(PreKeyButton, self).__init__(label='Get Prekey')
        self.plugin = plugin
        self.contact = contact
        self.connect('clicked', self.on_click)

    def on_click(self, widget):
        self.plugin.query_prekey(self.contact)


class ClearDevicesButton(gtk.Button):
    def __init__(self, plugin, contact):
        super(ClearDevicesButton, self).__init__(label='Clear Devices')
        self.plugin = plugin
        self.contact = contact
        self.connect('clicked', self.on_click)

    def on_click(self, widget):
        self.plugin.clear_device_list(self.contact)


class PublishButton(gtk.Button):
    def __init__(self, plugin, contact):
        super(PublishButton, self).__init__(label='Publish Bundle')
        self.plugin = plugin
        self.contact = contact
        self.connect('clicked', self.on_click)

    def on_click(self, widget):
        self.plugin.publish_bundle(self.contact.account)


def make_ui(plugin, chat_control):
    button = PreKeyButton(plugin, chat_control.contact)
    _add_widget(button, chat_control)
    button = PublishButton(plugin, chat_control.contact)
    _add_widget(button, chat_control)
    button = ClearDevicesButton(plugin, chat_control.contact)
    _add_widget(button, chat_control)


def _add_widget(widget, chat_control):
    actions_hbox = chat_control.xml.get_object('actions_hbox')
    send_button = chat_control.xml.get_object('send_button')
    send_button_pos = actions_hbox.child_get_property(send_button, 'position')
    actions_hbox.add_with_properties(widget, 'position', send_button_pos - 2,
                                     'expand', False)