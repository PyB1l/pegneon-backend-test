/*
*  A sample authentication JS Service for
*  dashboard app
*
 */

function pegneonService(authLink, gameLink) {

    var modal = window.Swal || {};

    // immutable object factory
    return Object.freeze({
        play: play
    });

    // play facade
    function play(serial) {
        return $.ajax({
            url: authLink,
            method: 'post',
            data: JSON.stringify({serial: serial}),
            contentType: 'application/json'
        }).then(onSuccess).fail(onError)
    }

    // service success authentication callback
    function onSuccess() {
        return $.getJSON(gameLink).then(function (resp) {

            // Log API response
            console.log(resp);

            return modal.fire(
                `${resp.greetings}`,
                `Start gaming for ${resp.department} department at ${resp.company} `,
                'success'
                )
        })
    }

    // service error authentication callback
    function onError() {
        return modal.fire(
            'Login failed',
            'Unable to login with provided credentials',
            'warning'
        )
    }
}