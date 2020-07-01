var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

let style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
let card = elements.create('card', { style: style });
card.mount('#card-element');

// Handle realtime validation errors on the card element. Review if best method for displaying error

card.addEventListener('change', function(event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});


let form = document.getElementById('payment-form');

/*
/ When user clicks submit button the event listener stops the form from being submitted and instead disables the card element and triggers loading overlay.
*/

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true });
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

    //let saveInfo = Boolean($('#id-save-info').attr('checked'));
    let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    let postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    let url = '/purchase/cache_checkout_data/';

    /*
    / Confirm card payment from stripe is ok, if is then submit the form. If error in form then loading element will be hidden and card element re-enabled
    / and error displayed for user.
    */

    $.post(url, postData).done(function() {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address: {
                        line1: $.trim(form.street_address.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                    }
                }
            }
        }).then(function(result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                $('#payment-form').fadeToggle(100);
                $('#loading-overlay').fadeToggle(100);
                card.update({ 'disabled': false });
                $('#submit-button').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function() {
        // just reload the page, the error will be in django messages
        location.reload();
    })
});