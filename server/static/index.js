$(document).ready(function(){
    $('#dataForm').submit(function(event){
        // Prevent default form submission
        event.preventDefault();

        // Get form data
        var formData = {
            'data': $('#data').val()
        };

        // Send AJAX POST request to Flask server
        $.ajax({
            type: 'POST',
            url: '/send_data',
            data: formData,
            success: function(response){
                // Display response from server (for demonstration)
                alert(response);
            },
            error: function(xhr, status, error){
                // Display error message if request fails
                console.error(xhr.responseText);
            }
        });
    });
});

function openP() {

    document.getElementById("viaParameters").style.width = "250px";
    document.getElementById("viaTuning").style.width = "0px";
    document.getElementById("viaOpenLoop").style.width = "0px";

}

function openK() {

    document.getElementById("viaParameters").style.width = "0px";
    document.getElementById("viaTuning").style.width = "250px";
    document.getElementById("viaOpenLoop").style.width = "0px";

}

function openL() {

    document.getElementById("viaParameters").style.width = "0px";
    document.getElementById("viaTuning").style.width = "0px";
    document.getElementById("viaOpenLoop").style.width = "250px";

}
