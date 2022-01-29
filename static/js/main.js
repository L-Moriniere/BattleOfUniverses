$(document).ready(function() {
    $('#selectAll').click(function (event) {
        $('input').not(this).prop('checked', this.checked);
    });
});