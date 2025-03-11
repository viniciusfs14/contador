document.addEventListener("DOMContentLoaded", function () {
    function atualizarContador() {
        const dataInicio = new Date("2025-01-17T00:00:00").getTime(); // Data inicial
        const agora = new Date().getTime();
        const diferenca = agora - dataInicio;

        const dias = Math.floor(diferenca / (1000 * 60 * 60 * 24));
        const horas = Math.floor((diferenca % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutos = Math.floor((diferenca % (1000 * 60 * 60)) / (1000 * 60));
        const segundos = Math.floor((diferenca % (1000 * 60)) / 1000);

        document.getElementById("contador").innerHTML = `
            <p><span> Estou sendo o cara mais feliz do mundo ao seu lado faz
            <p><span>${dias}</span> dias <span>${horas}</span>h <span>${minutos}</span>m <span>${segundos}</span>s
        `;
    }

    atualizarContador();
    setInterval(atualizarContador, 1000);
});
