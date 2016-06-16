/* Javascript for Click2RevealXBlock. */
function Click2RevealXBlock(runtime, element) {

    function revealComment(e) {
  var comment = $(e.target).parents('.c2r-container').find('.c2r-comment')[0];
  
  if (comment.style.display == 'block') {
   comment.style.display = 'none';
   comment.setAttribute('aria-hidden', 'true');
   e.target.textContent = self.showActionLabel.concat(self.textLabel);
   e.target.setAttribute('aria-expanded', 'false');
  }
  else {
   comment.style.display = 'block';
   comment.removeAttribute('aria-hidden');
   e.target.textContent = self.hideActionLabel.concat(self.textLabel);
   e.target.setAttribute('aria-expanded', 'true');
  }
 }


    $(function ($) {
        /* Here's where you'd do things on page load. */
    });
}
