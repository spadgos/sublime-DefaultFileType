import sublime
import sublime_plugin


class DefaultFileTypeCommand(sublime_plugin.WindowCommand):

    def run(self):
        w = self.window
        settings = sublime.load_settings("default_file_type.sublime-settings")
        if settings.get('use_current_syntax') and w.active_view():
            syntax = w.active_view().settings().get('syntax')
        else:
            syntax = 'Packages/DefaultFileType/Syntaxes/' + settings.get('default_new_syntax')

        view = w.new_file()
        # sublime.error_message("%s" % syntax)
        view.set_syntax_file(syntax)
