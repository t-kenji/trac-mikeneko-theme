var warning_offset = null;
var notice_offset = null;

$(function () {
    var mainnav_offset = $('#mainnav').offset();
    var floatnav = $('#floatnav');
    floatnav.hide();

    var warning = $('#warning');
    var floatwarn = null;
    if (warning) {
        warning_offset = warning.offset();
        floatwarn = $('#floatwarn');
        floatwarn.hide();
    }

    var notice = $('#notice');
    var floatnotice = null;
    if (notice) {
        notice_offset = notice.offset();
        floatnotice = $('#floatnotice');
        floatnotice.hide();
    }

    $(window).scroll(function () {
        scroll_top = $(this).scrollTop();

        if (scroll_top > mainnav_offset.top) {
            floatnav.show();
        } else {
            floatnav.hide();
        }

        if (warning_offset) {
            if (scroll_top + floatnav.height() > warning_offset.top) {
                floatwarn.css('top', floatnav.height());
                floatwarn.show();
            } else {
                floatwarn.hide();
            }
        }

        if (notice_offset) {
            if (scroll_top + floatnav.height() > notice_offset.top) {
                floatnotice.css('top', floatnav.height());
                floatnotice.show();
            } else {
                floatnotice.hide();
            }
        }
    });
});

$(document).ready(function ($) {
    $('.trac-close-msg').click(function () {
        if (warning_offset) {
            warning_offset = null;
            $('#warning').hide();
        }
        if (notice_offset) {
            notice_offset = null;
            $('#nitoce').hide();
        }
    });
});
