Dias, horas, minutos e segundos desde que estamos juntos:

<div id="contador" style="font-size: 1.5em; color: #ff3366; font-weight: bold;"></div>

<script src="/js/contador.js"></script>

## Nossa Trilha Sonora 🎶  

Clique no botão para ouvir nossa música especial:  

<button id="playMusic" style="font-size: 1.2em; padding: 10px 20px; background-color: #ff3366; color: white; border: none; border-radius: 5px; cursor: pointer;">
    ▶️ Iniciar Música
</button>

<audio id="musica">
    <source src="/music/musga.mp3" type="audio/mpeg">
</audio>

<script>
document.getElementById("playMusic").addEventListener("click", function() {
    var audio = document.getElementById("musica");
    audio.play();
});
</script>

<!-- Controle de volume -->
<label for="volumeControl" style="font-size: 1.2em;">🔊 Volume:</label>
<input type="range" id="volumeControl" min="0" max="1" step="0.1" value="0.5" style="width: 150px;">

<script>
document.getElementById("playMusic").addEventListener("click", function() {
    var audio = document.getElementById("musica");
    audio.play();
});

// Ajuste de volume
document.getElementById("volumeControl").addEventListener("input", function() {
    var audio = document.getElementById("musica");
    audio.volume = this.value;
});
</script>