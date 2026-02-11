// Fix cloned navbar sidebar menu - keep original theme animation
$(document).ready(function(){
    // Handle cloned menu icon trigger (same as original theme logic)
    $('#cloned-menu-icon-trigger').on("click", function(e){
        e.preventDefault();
        $('#cloned-menu-icon-wrapper').toggleClass('open');
        $('.sidebar').toggleClass('is-active');
    });
    
    // Handle hamburger menu toggle for mobile
    $('.navbar-burger').on('click', function() {
        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        $('.navbar-burger').toggleClass('is-active');
        $('.navbar-menu').toggleClass('is-active');
    });
});