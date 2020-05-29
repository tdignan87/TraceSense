let featuresSection = document.getElementById("features-area");

/**
 * Learn more btn click event go to relevant section of page that shows more 
 * information.
 */

$("#learn-more-btn").click(function() {
    console.log("clicked btn");
    $('html, body').animate({
        scrollTop: $("#features-area").offset().top
    }, 1000);

})