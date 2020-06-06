let featuresSection = document.getElementById("features-area");

/**
 * Learn more btn click event go to relevant section of page that shows more 
 * information.
 */

$("#learn-more-btn").click(function() {
    $('html, body').animate({
        scrollTop: $("#features-area").offset().top
    }, 1000);

})

$("#support-link").click(function() {
    $('html, body').animate({
        scrollTop: $("#support-section").offset().top
    }, 1000);

})

$("#pricing-link").click(function() {
    $('html, body').animate({
        scrollTop: $("#pricing-area").offset().top
    }, 1000)
})

/**
 * Side navigation toggle.
 */

$("#menu-toggle").click(function(e) {
    e.preventDefault();
    $("#sidebar-wrapper").toggle("sidebar-nav");
    console.log("test click");
});