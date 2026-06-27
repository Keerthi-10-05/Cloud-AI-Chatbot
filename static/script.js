document.addEventListener("DOMContentLoaded", function () {

    document.getElementById("user-input")
        .addEventListener("keypress", function(event){

        if(event.key === "Enter"){
            sendMessage();
        }

    });

});

async function sendMessage() {

    let input = document.getElementById("user-input");
    let message = input.value.trim();

    if(message==="")
        return;

    let chat = document.getElementById("chat-box");

    chat.innerHTML +=
    `<div class="user-message">${message}</div>`;

    input.value="";

    let response = await fetch("/get_response",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            message:message
        })
    });

    let data=await response.json();

    chat.innerHTML +=
    `<div class="bot-message">${data.response}</div>`;

    chat.scrollTop=chat.scrollHeight;

}
