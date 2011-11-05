import sublime_plugin
import sublime


class DefaultFileTypeCommand(sublime_plugin.WindowCommand):

    def run(self):
        w = self.window
        settings = sublime.load_settings("default_file_type.sublime-settings")

        if settings.get('use_current_file_syntax') and w.active_view():
            syntax = w.active_view().settings().get('syntax')
        else:
            syntax = settings.get('default_new_file_syntax')

        view = w.new_file()
        # sublime.error_message("%s" % syntax)
        view.set_syntax_file(syntax)
