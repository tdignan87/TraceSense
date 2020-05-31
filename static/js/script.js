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

$("#pricing-link").click(function() {
    $('html, body').animate({
        scrollTop: $("#pricing-area").offset().top
    }, 1000)
})