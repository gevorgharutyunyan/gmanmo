$(function () {
    $('#scrollToBottom').bind("click", function () {
        $('html, body').animate({ scrollTop: $(document).height() }, 900);
        return false;
    });
    $('#scrollToTop').bind("click", function () {
        $('html, body').animate({ scrollTop: 0 }, 900);
        return false;
    });
});