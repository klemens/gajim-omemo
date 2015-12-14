# OMEMO Plugin for Gajim

Experimental plugin that adds support for the [OMEMO Encryption](http://conversations.im/omemo) to [Gajim](https://gajim.org/).

**DO NOT rely on this plugin to protect sensitive information!** 

### Dependencies
All dependencies can be installed with ```pip```. (Depending on your setup you might want to use ```pip2``` as Gajim is using python2.7)

* python-axolotl
* pycryptodome

### Installation
Clone the git repository into Gajims plugin directory.
````
cd ~/.local/share/gajim/plugins
git clone git@github.com:kalkin/gajim-omemo.git
````

### Patching Gajim
There is a bug in gajim that prevents plugins from receiving PEP messages. Until this bug is fixed upstream this plugin provides a patch file in ```gajim_fix_pep_messages.patch``` that can be applied as follows
````
cd /path/to/gajim
patch -p1 -i /path/to/gajim_fix_pep_messages.patch
````

### Running
To see OMEMO related debug output start gajim with the parameter ```-l plugin_system.omemo=DEBUG```.

Enable *OMEMO Mult-End Message and Object Encryption* in the Plugin-Manager. Before exchanging encrypted messages with a contact you have to hit the *Get Missiing Prekeys* button. (Repeat that if you or your contact get new devices.)
