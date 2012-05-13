$(document).ready(function(){
    // suggestion text in inputs
    $('.clean').focus(function(){
        $(this).val('').removeClass('clean').unbind('focus');
    });
});
