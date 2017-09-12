/* Javascript for Click2RevealXBlock. */
function C2RBlock(runtime, element, initargs) {
    /* Runtime stuff, nothing here for now */
}

function c2r(event, showText, hideText) {
    var showFinal = '<i class="fa fa-eye" aria-hidden="true"></i> ' + showText;
    var hideFinal = '<i class="fa fa-eye" aria-hidden="true"></i> ' + hideText;
    var buttonPressed = $(event.target);
    var comment = buttonPressed.nextAll('.c2r-comment');
    
    comment.slideToggle(200, function() {
        if (comment.is(":hidden")) {
            buttonPressed.html(showFinal);
            buttonPressed.attr("aria-expanded", "false");
        } else {
            buttonPressed.html(hideFinal);
            buttonPressed.attr("aria-expanded", "true");
        }
    });
}
