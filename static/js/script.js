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
});


/**
 * Hide sections on form load event.
 */

$(window).ready(function() {
    $("#department-area").hide();
    $("#production-area").hide();
    $("#alert-area").hide();
    $("#audit-area").hide();

});
/**
 * Dashboard hide and display control elements on the page.
 */


$("#department-nav").click(function(e) {
    e.preventDefault();
    $("#department-area").toggle("sidebar-nav");
    $('html, body').animate({
        scrollTop: $("#department-area").offset().top
    }, 1000)
    $("#dash-items").hide();
    $("#production-area").hide();
    $("#alert-area").hide();
    $("#audit-area").hide();
});

$("#production-nav").click(function(e) {
    e.preventDefault();
    $("#production-area").toggle("sidebar-nav");
    $('html, body').animate({
        scrollTop: $("#production-area").offset().top
    }, 1000)
    $("#dash-items").hide();
    $("#department-area").hide();
    $("#alert-area").hide();
    $("#audit-area").hide();
});

$("#alert-nav").click(function(e) {
    e.preventDefault();
    $("#alert-area").toggle("sidebar-nav");
    $('html, body').animate({
        scrollTop: $("#alert-area").offset().top
    }, 1000)
    $("#dash-items").hide();
    $("#department-area").hide();
    $("#production-area").hide();
    $("#audit-area").hide();
});

$("#questions-nav").click(function(e) {
    e.preventDefault();
    $("#audit-area").toggle("sidebar-nav");
    $('html, body').animate({
        scrollTop: $("#audit-area").offset().top
    }, 1000)
    $("#dash-items").hide();
    $("#department-area").hide();
    $("#production-area").hide();
    $("#alert-area").hide();
});