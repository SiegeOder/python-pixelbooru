var music = new Audio;
music.src = "/audio/bathory.mp3";
function playMusic(){
    if(music.paused) music.play();
    else music.pause();
}
