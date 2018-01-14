import sublime
import sublime_plugin

class Listener(sublime_plugin.EventListener):

    def on_new( self, view ):
        settings = sublime.load_settings("default_file_type.sublime-settings")

        if settings.get('use_current_syntax') and view:
            syntax = view.settings().get('syntax')
        else:
            syntax = settings.get('default_new_syntax')

        # sublime.error_message("%s" % syntax)
        view.set_syntax_file(syntax)