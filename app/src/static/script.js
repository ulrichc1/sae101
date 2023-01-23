  // JavaScript pour ajouter la classe "show" pour déclencher l'animation
  window.onload = function() {
    window.scrollTo(0, 0);
    var textSlide = document.querySelector('header');
    textSlide.classList.add('show');
  };

//JS pour affecter la date maximale possible au jour d'aujourd'hui et envoyer la requête émise par le formulaire sur le serveur Flask (Python)
 document.getElementById('value').max = new Date(new Date().getTime() - new Date().getTimezoneOffset() * 60000).toISOString().split("T")[0];
 document.getElementById("form").addEventListener("submit", function(event) {event.preventDefault();
// Récupération de la valeur transmise par le formulaire
 var value = document.getElementById("value").value;
 console.log(value);
// Requête HTTP au serveur Flask
 fetch("{{ url_for('submit_form') }}", {
 method: "GET",
 body: JSON.stringify({value: value}),
 headers: {
 "Content-Type": "application/json"
}
})
.then(function(response) {
return response.json();
})
.then(function(data) {
// Réponse du serveur Flask
console.log(data);
});
});



