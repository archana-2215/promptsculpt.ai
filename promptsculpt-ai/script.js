let progress = 0;
const progressBar = document.getElementById("progress-bar");
const loadingText = document.getElementById("loading-text");
const splashScreen = document.getElementById("splash-screen");

window.addEventListener("load", () => {
    const interval = setInterval(() => {
        progress++;
        progressBar.style.width = progress + "%";
        loadingText.innerText = "Loading... " + progress + "%";

        if (progress >= 100) {
            clearInterval(interval);
            setTimeout(() => {
                splashScreen.style.opacity = "0";
                setTimeout(() => {
                    splashScreen.style.display = "none";
                }, 1000);
            }, 500);
        }
    }, 30);
});