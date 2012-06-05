$(document).ready(function(){
    // suggestion text in inputs
    $('.clean').focus(function(){
        $(this).val('').removeClass('clean').unbind('focus');
    });
});

// model logic
var books = {
    views: {
        add: {
            textSelect: function(form) {
                var data = $(form).serialize();
                alert(data);
            },
        },
    },
}
