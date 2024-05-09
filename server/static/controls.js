// Funcion que abre el panel de los parametros
function openP() {

    document.getElementById("viaParameters").style.width = "350px";
    document.getElementById("viaTuning").style.width = "0px";
    document.getElementById("viaOpenLoop").style.width = "0px";

}

// Funcion que abre el panel de las constantes
function openK() {

    document.getElementById("viaParameters").style.width = "0px";
    document.getElementById("viaTuning").style.width = "350px";
    document.getElementById("viaOpenLoop").style.width = "0px";

}

// Funcion que abre el panel del control manual
function openL() {

    document.getElementById("viaParameters").style.width = "0px";
    document.getElementById("viaTuning").style.width = "0px";
    document.getElementById("viaOpenLoop").style.width = "350px";

}