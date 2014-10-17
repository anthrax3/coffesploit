# -*- coding: utf-8 -*-
from target import Target
from help import Help
from pluginmanager import PluginManager

__Version__ = "0.1test"


class Coffesploit(object):
    """Main Class"""
    def __init__(self, basepath):
        self.target = Target()
        self.tool = None
        self.pluginmanager = PluginManager()
        self.helper = Help()
        self.basepath = basepath
        
    def set_target(self,rhost=None,url=None):
        if url is not None:
            self.target.seturl(url)
        if rhost is not None:
            self.target.setrhost(rhost)
    def set(self, arg1, arg2):
        self.pluginmanager.current_plugin.set_arg(arg1,arg2)
    def show(self,arg):
        if arg == "target":
            print "ip:",self.target.getrhost(),"url:",self.target.geturl()
        if arg == "status":
            if self.pluginmanager.current_plugin is not None:
                self.pluginmanager.plugin_status()
        if arg == "version":
            print "Currnt Version:",self.version()
                
    def use(self,arg):
        self.pluginmanager.load_plugin(arg)
        
    def run(self):
        self.pluginmanager.plugin_run()
        self.pluginmanager.plugin_result()

    def main_help (self):
        return self.helper.main_help()
    def main_list (self):
        return self.pluginmanager.importer.get_plugins_list()
    def help(self,arg):
        """show help info of t"""
        if arg == "target":
            self.helper.help_set_tartget()
        if arg == "show":
            self.helper.help_show()
        if arg == "use":
            self.helper.help_use()
    def exit(self):
        exit(0)
    def version(self):
        return __Version__
