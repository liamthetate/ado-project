
var stripe_public_key = $('#id_stripe_publick_key').text().slice(1,-1); /* gets the name and slices of quotatiosn marks */
var client_secret = $('#id_client_secret').text().slice(1,-1); 
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var style = {
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
var card = elements.create('card', {style:style});
card.mount('#card-element');

// handle realtime errors, displays a relevant message to user about the error
card.addEventListener('change', function(event) {
    var errorDiv = document.getElementById('card-errors')
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span> 
        `
        ${errorDiv}.html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// step1: checkout view create stripe 'paymentIntent'
// step2: stripe gives 'client_secret' to the template
// step3: template thens uses confirmCardPayment()