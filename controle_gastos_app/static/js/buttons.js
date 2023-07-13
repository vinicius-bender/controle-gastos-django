let btnEntrada = document.getElementById("btn-entrada");
let btnSaida = document.getElementById("btn-saida");

btnEntrada.addEventListener("click", () => {

    btnEntrada.style.backgroundColor = "black";
    btnSaida.style.backgroundColor = "#363636";

});

btnSaida.addEventListener("click", () => {

    btnSaida.style.backgroundColor = "black";
    btnEntrada.style.backgroundColor = "#363636";
});
