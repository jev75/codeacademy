// Funkcija, kuri rodo pranešimą, kai puslapis yra pilnai įkeltas
window.onload = function() {
    alert("Admin puslapis pilnai įkeltas!");
}

// Funkcija, kuri keičia spalvą paspaudus mygtuką
function changeColor() {
    document.body.style.backgroundColor = "lightblue";
}

// Funkcija, kuri rodo arba slepia elementą paspaudus mygtuką
function toggleElement(id) {
    var element = document.getElementById(id);
    if (element.style.display === "none") {
        element.style.display = "block";
    } else {
        element.style.display = "none";
    }
}
