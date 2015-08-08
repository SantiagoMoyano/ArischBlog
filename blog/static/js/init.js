$(document).ready(function(){
    $('.parallax').parallax();
    $('.button-collapse').sideNav();
    $('select').material_select();
    $('.datepicker').pickadate({selectMonths: true, selectYears: 15});
    $('.slider').slider({full_with: true});
    $('.materialboxed').materialbox();
    $('.modal-trigger').leanModal();
});