$(function () {
  var shown_ctxtnav = false;
  $(window).scroll(function () {
    var scroll_top = $(this).scrollTop();

    if (scroll_top > 200) {
      if (!shown_ctxtnav) {
        shown_ctxtnav = true;
        $(".contents-header").has("#pagepath,#ctxtnav > ul").addClass("fixed");
      }
    } else {
      if (shown_ctxtnav) {
        shown_ctxtnav = false;
        $(".contents-header").has("#pagepath,#ctxtnav > ul").removeClass("fixed");
      }
    }
  });
});
