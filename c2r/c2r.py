"""A simple xblock to reveal html on click."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment
from xblockutils.studio_editable import StudioEditableXBlockMixin


class Click2RevealXBlock(StudioEditableXBlockMixin, XBlock):
    """
    A simple xblock to reveal html on click.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.
    display_name = String(display_name="Display name", default='Click to reveal')
    showActionLabel = String(display_name="'Show' Action label", default="Reveal ", scope=Scope.settings,
        help="The name of the action to show the text to the student.")
    hideActionLabel = String(display_name="'Hide' Action label", default="Hide ", scope=Scope.settings,
        help="The name of the action to hide the text from the student.")

    textLabel = String(display_name="Text label", default="Comment", scope=Scope.settings,
        help="The name of the text that is revealed, for example 'comment' or 'answer'. This will appear as a heading.")
    headingLevel = Integer(display_name="Heading level", values=('2', '3', '4', '5'),
        default="3", scope=Scope.settings,
        help="Heading level (if this sits under another heading, pick one number lower)")
    revealText = String(display_name="Text to reveal", multiline_editor='html', resettable_editor=False,
        default="Here is some revealed text.", scope=Scope.settings,
        help="The text to reveal.")
    bgColour = String(display_name="Background colour", default = "#eef6ff", scope=Scope.settings, help="Background colour for the content.")

    # Make fields editable in studio?
<<<<<<< HEAD
    editable_fields = ('showActionLabel', 'hideActionLabel', 'textLabel', 'headingLevel', 'revealText', 'bgColour' )
=======
    editable_fields = ('display_name', 'showActionLabel', 'hideActionLabel', 'textLabel', 'headingLevel', 'revealText', )
>>>>>>> origin/master

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
