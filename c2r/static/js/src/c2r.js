/* Javascript for Click2RevealXBlock. */
function C2RBlock(runtime, element, initargs) {
    /* Runtime stuff, nothing here for now */
}

function showDesc(event, showText, hideText) {
    var showFinal = '<i class="fa fa-eye" aria-hidden="true"></i> ' + showText;
    var hideFinal = '<i class="fa fa-eye" aria-hidden="true"></i> ' + hideText;
    var buttonPressed = $(event.target);
    var comment = buttonPressed.nextAll('.c2r-comment');
    
    comment.slideToggle(200, function() {
        if (comment.is(":hidden")) {
            buttonPressed.text(showFinal);
            buttonPressed.attr("aria-expanded", "false");
        } else {
            buttonPressed.text(hideFinal);
            buttonPressed.attr("aria-expanded", "true");
        }
    });
}
