"""A simple xblock to reveal html on click."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment
#from xblockutils.studio_editable import StudioEditableXBlockMixin


class Click2RevealXBlock(XBlock):
    """
    A simple xblock to reveal html on click.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.
    showActionLabel= String(default="Reveal ", scope=Scope.settings, 
        help="The name of the action to show the text to the student.")
    hideActionLabel= String(default="Hide ", scope=Scope.settings, 
        help="The name of the action to show the text to the student.")

    textLabel= String(default="Comment", scope=Scope.settings,
        help="The name of the text that is revealed, for example 'comment' or 'answer'.")

    revealText = String(
        default="Here is some revealed text.", scope=Scope.settings,
        help="The text to reveal.",
    )
    # Make fields editable in studio?
    #editable_fields=('showActionLabel, hideActionLabel, textLabel, revealText')

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        html_str = pkg_resources.resource_string(__name__, "static/html/c2r.html")
        frag = Fragment(unicode(html_str).format(self=self))

        # Load the CSS and JavaScript fragments from within the package
        css_str = pkg_resources.resource_string(__name__, "static/css/c2r.css")
        frag.add_css(unicode(css_str))

        js_str = pkg_resources.resource_string(__name__,
                                               "static/js/src/c2r.js")
        frag.add_javascript(unicode(js_str))

        frag.initialize_js('C2RBlock')
        return frag


    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("Click to reveal", """\
                <vertical_demo>
                    <c2r/>
                    <c2r/>
                    <c2r/>
                </vertical_demo>
             """),
        ]
class C2RBlock(Click2RevealXBlock, XBlock):
    """
    A simple xblock to reveal html on click.
    """
    pass