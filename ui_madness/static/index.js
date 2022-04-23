function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');


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
