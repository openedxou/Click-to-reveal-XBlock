/* Javascript for Click2RevealXBlock. */
function C2RBlock(runtime, element, initargs) {
    /* Runtime stuff, nothing here for now */
}

function revealDescription(e, showText, hideText) {
    var comment = $(e.target).parents('.c2r-container').find('.c2r-comment')[0];
    var button = $(e.target).parents('.c2r-container').find('.c2r-button')[0];
    var showFinal = '<i class="fa fa-eye" aria-hidden="true"></i> ' + showText;
    var hideFinal = '<i class="fa fa-eye" aria-hidden="true"></i> ' + hideText;
    
    if (comment.style.display == 'block') {
        comment.style.display = 'none';
        comment.setAttribute('aria-hidden', 'true');
        button.innerHTML = showFinal;
        button.setAttribute('aria-expanded', 'false');
    } else {
        comment.style.display = 'block';
        comment.removeAttribute('aria-hidden');
        button.innerHTML = hideFinal;
        button.setAttribute('aria-expanded', 'true');
    }
}
