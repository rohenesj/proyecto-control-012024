let zitaEnabled = document.getElementById('zitaEnabled');
let tpEnabled = document.getElementById('tpEnabled');
let teEnabled = document.getElementById('teEnabled');
let trEnabled = document.getElementById('trEnabled');

let zita = document.getElementById('zitaValue');
let tr = document.getElementById('trValue');
let tp = document.getElementById('tpValue');
let te = document.getElementById('teValue');

// Controla comportamiento de las cajas de texto y checkboxes en javascript
document.addEventListener('DOMContentLoaded', function() {
    var maxCheckboxes = 2;
    $('input[type="checkbox"]').change(function() {
      var checkedCheckboxes = $('input[type="checkbox"]:checked');
      if (checkedCheckboxes.length > maxCheckboxes) {
        $(this).prop('checked', false);
      }
    });
    zitaEnabled.addEventListener('change', function() { 
        if (zitaEnabled.checked) {
            zita.disabled = false;
        } else {
            zita.disabled = true;
            zita.value = "";
        }
    });
    tpEnabled.addEventListener('change',function() {
        if (tpEnabled.checked) {
            tp.disabled = false;
        } else {
            tp.disabled = true;
            tp.value = "";
        }
    });
    teEnabled.addEventListener('change', function() {
        if (teEnabled.checked) {
            te.disabled = false;
        } else {
            te.disabled = true;
            te.value = "";
        }
    });
    trEnabled.addEventListener('change', function() {
        if (trEnabled.checked) {
            tr.disabled = false;
        } else {
            tr.disabled = true;
            tr.value = "";
        }
    });

});

// Mandar datos al servidor (TODO)
function sendParams() {
    let mode = modeSelection()
    if (mode == -1) {
        alert("Se debe escoger dos variables");
    } else {
        $.ajax({
            type: 'POST',
            url: '/send_data',
            data: {
                mode: mode,
                zita: zita.value,
                tr: tr.value,
                tp: tp.value,
                te: te.value,
            },
            success: function(response){
                // Display response from server (for demonstration)
                alert(response);
            },
            error: function(xhr, status, error){
                // Display error message if request fails
                console.error(xhr.responseText);
            }
        });
    }
}

function modeSelection() {
    if (zitaEnabled.checked && trEnabled.checked) {return 2;}
    else if (zitaEnabled.checked && tpEnabled.checked) {return 3;}
    else if (zitaEnabled.checked && teEnabled.checked) {return 4;}
    else if (trEnabled.checked && tpEnabled.checked) {return 5;}
    else if (trEnabled.checked && teEnabled.checked) {return 6;}
    else if (tpEnabled.checked && teEnabled.checked) {return 7;}
    else {return -1;}
}