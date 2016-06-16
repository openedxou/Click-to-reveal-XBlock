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

        html = self.resource_string("static/html/c2r.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/c2r.css"))
        frag.add_javascript(self.resource_string("static/js/src/c2r.js"))
        frag.initialize_js('Click2Reveal')
        return frag

    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("Click to reveal", "<c2r/>"),
        ]