// Fix cloned navbar sidebar menu - keep original theme animation
$(document).ready(function(){
    $('#cloned-menu-icon-trigger').on("click", function(e){
        e.preventDefault();
        $('#cloned-menu-icon-wrapper').toggleClass('open');
        $('.sidebar').toggleClass('is-active');
    });

    $('.navbar-burger').on('click', function() {
        $('.navbar-burger').toggleClass('is-active');
        $('.navbar-menu').toggleClass('is-active');
    });
});
