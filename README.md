# Click-to-reveal-XBlock
A basic, slightly wonky XBlock to reveal some text when a button element is clicked.

Four fields: 
- 'Show' action name (such as 'Reveal', 'Click to' or 'Show')
- 'Hide' action name (such as 'Close', 'Click to' or 'Hide')
- Text Label (such as 'Comment', 'Description' or 'Text') - This displays both on the button and as a heading in the text
- Heading level (for the text label in the revealed text)
- Reveal text (the text to reveal)

This is to try and make the way the button displays as customisable as possible. It defaults to 'Reveal Comment' and 'Hide Comment'.
Contains ARIA tags in an attempt at making the functionality accessible to screen readers.
