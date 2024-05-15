let tpEnabled = document.getElementById('tpEnabled');
let teEnabled = document.getElementById('teEnabled');
let trEnabled = document.getElementById('trEnabled');

let pCheck = document.getElementById('pCheck');
let iCheck = document.getElementById('iCheck');
let dCheck = document.getElementById('dCheck');


let mp = document.getElementById('mpValue');
let tr = document.getElementById('trValue');
let tp = document.getElementById('tpValue');
let te = document.getElementById('teValue');

let mode = 0;
let kp = 0;
let ki = 0;
let kd = 0;
let pwm = 0;
let controllerType = "";

// Controla comportamiento de las cajas de texto y checkboxes en javascript
document.addEventListener('DOMContentLoaded', function() {
    tpEnabled.addEventListener('change',function() {
        if (tpEnabled.checked) {
            tp.disabled = false;
            te.disabled = true;
            tr.disabled = true;
            te.value = "";
            tr.value = "";
        } else {
            tp.disabled = true;
            tp.value = "";
        }
    });
    teEnabled.addEventListener('change', function() {
        if (teEnabled.checked) {
            te.disabled = false;
            tr.disabled = true;
            tp.disabled = true;
            tr.value = "";
            tp.value = "";
        } else {
            te.disabled = true;
            te.value = "";
        }
    });
    trEnabled.addEventListener('change', function() {
        if (trEnabled.checked) {
            tr.disabled = false;
            te.disabled = true;
            tp.disabled = true;
            te.value = "";
            tp.value = "";
        } else {
            tr.disabled = true;
            tr.value = "";
        }
    });

});

// Mandar datos al servidor (TODO)
function sendParams() {
    let mode = modeSelection()
    controllerType = controllerCheck();
    if (controllerType == "") {
        alert("Porfavor escoger un controlador");
        return;
    }
    if (mode == -1) {
        alert("Se debe escoger dos variables");
    } else if (mode == -2) {
        alert("Porfavor entregue valores validos");
    } else {
        $.ajax({
            type: 'POST',
            url: '/send_data',
            data: {
                mode: mode,
                mp: mp.value,
                tr: tr.value,
                tp: tp.value,
                te: te.value,
                kp: kp,
                ki: ki,
                kd: kd,
                c: controllerType,
                pwm: pwm,
            },
            success: function(response){
                // Display response from server (for demonstration)
                let timestamp = new Date().getTime();
                let imgUpdate = 'static/respuestaActual.png' + '?timestamp=' + timestamp;
                let imgElement = $('<img>');
                $("#zita").text("ζ: " + response.zita);
                $("#omega").text("ω: " + response.omega);
                $("#tr").text("tr: " + response.tr);
                $("#tp").text("tp: " + response.tp);
                $("#te").text("te: " + response.te);
                $("#Kp").text("Kp: " + response.kp);
                $("#Ki").text("Ki: " + response.ki);
                $("#Kd").text("Kd: " + response.kd);
                imgElement.attr('src', imgUpdate);
                $('#PIDimage').empty();
                $('#PIDimage').append(imgElement);
                $('#PIDimage').addClass('PIDgraph');
            },
            error: function(xhr, status, error){
                // Display error message if request fails
                console.error(xhr.responseText);
            }
        });
    }
}

function modeSelection() {
    if (mp.value < 1 || mp.value > 100) {return -2}
    else if (trEnabled.checked) {return 2;}
    else if (tpEnabled.checked) {return 3;}
    else if (teEnabled.checked) {return 4;}
    else {return -1;}
}

function controllerCheck() {
    if (pCheck.checked && iCheck.checked && dCheck.checked) {return "PID";}
    else if (pCheck.checked && iCheck.checked) {return "PI";}
    else if (pCheck.checked && dCheck.checked) {return "PD";}
    else if (iCheck.checked && dCheck.checked) {return "ID";}
    else if (pCheck.checked) {return "P";}
    else if (iCheck.checked) {return "I";}
    else if (dCheck.checked) {return "D";}
    else {return "";}
}