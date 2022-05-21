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

function updateComments() 
{
     if(url==null)return;
       let xhr = new XMLHttpRequest();
       xhr.open("GET", url);
       xhr.setRequestHeader('X-CSRFToken', csrftoken)
       xhr.setRequestHeader("Accept", "application/json");
       xhr.setRequestHeader("Content-Type", "application/json");

       xhr.onreadystatechange = function() {
           if (xhr.readyState === 4) {
               //console.log(xhr.responseText);
              CommentSection.innerHTML = xhr.responseText;
           }
       };

       xhr.send();
   
}

async function updatePage() {
  while(true)
    {
      let p = new Promise(r => setTimeout(r, 10000));
      p.then(updateComments)
      await p
    }
}

updatePage()