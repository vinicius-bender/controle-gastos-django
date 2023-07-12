let btnEntrada = document.getElementById("btn-entrada");
let btnSaida = document.getElementById("btn-saida");
let entradaSelected = false;
let saidaSelected = false;

btnEntrada.addEventListener("click", () => {

    btnEntrada.style.backgroundColor = "black";
    btnSaida.style.backgroundColor = "#363636";
    entradaSelected = true;
    saidaSelected = false;

});

btnSaida.addEventListener("click", () => {

    btnSaida.style.backgroundColor = "black";
    btnEntrada.style.backgroundColor = "#363636";
    entradaSelected = false;
    saidaSelected = true;
});
