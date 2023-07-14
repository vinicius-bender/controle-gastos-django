let btnEntrada = document.getElementById("btn-entrada");
let btnSaida = document.getElementById("btn-saida");
let tipo = document.getElementById("tipo");

btnEntrada.addEventListener("click", () => {
    btnEntrada.style.backgroundColor = "black";
    btnSaida.style.backgroundColor = "#363636";
    tipo.value = 1;
    
});

btnSaida.addEventListener("click", () => {
    btnSaida.style.backgroundColor = "black";
    btnEntrada.style.backgroundColor = "#363636";
    tipo.value = 2;
});