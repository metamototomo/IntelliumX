// Fix cloned navbar sidebar menu
$(document).ready(function(){
    let sidebarOpen = false;
    
    // Handle both original and cloned menu icon triggers
    $('.menu-icon-trigger, #cloned-menu-icon-trigger').on("click", function(e){
        e.preventDefault();
        console.log('Hamburger clicked');
        
        $('.menu-icon-wrapper').toggleClass('open');
        $('#cloned-menu-icon-wrapper').toggleClass('open');
        
        // Direct class manipulation instead of toggleClass
        if (sidebarOpen) {
            $('.sidebar').removeClass('is-active');
            sidebarOpen = false;
        } else {
            $('.sidebar').addClass('is-active');
            sidebarOpen = true;
        }
        
        console.log('Sidebar toggled, now open:', sidebarOpen);
        console.log('Sidebar has is-active class:', $('.sidebar').hasClass('is-active'));
    });
    
    // Debug: Check if sidebar exists
    console.log('Sidebar elements found:', $('.sidebar').length);
});