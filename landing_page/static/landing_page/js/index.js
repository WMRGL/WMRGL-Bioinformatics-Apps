$(document).ready(function() {
    $('.ui.modal')
        .modal();
})

$('#add-new-app-card').click(function(e) {
    e.preventDefault();
    $('#add-new-app-modal')
        .modal('show');
});

$('#close-new-app-modal').click(function(e) {
    e.preventDefault();
    $('#add-new-app-modal')
        .modal('hide');
});

$('#remove-app-button').click(function(e) {
    e.preventDefault();
    $('#remove-app-modal')
        .modal('show');
})
