MenuButton.onclick = function() {
    document.getElementById("SidePanel").style.width = "250px";
}


closebtn.onclick = function() {

    document.getElementById("SidePanel").style.width = "0";
    stopPlayingSound()
}

var sound = null

function stopPlayingSound() {
    if (sound) {
        sound.pause();
        sound = null
    }
}

function play(path) {
    stopPlayingSound()
    sound = new Audio(path);
    sound.play();
}
