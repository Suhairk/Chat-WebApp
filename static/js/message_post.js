
const messageButton = document.getElementById("button")

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
messageButton.onclick=(e)=>{
    const message = document.getElementById('messages');
    const username = document.getElementById('username');
    const group_id = document.getElementById('group_id');
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]');
    // console.log(message.value)
    // console.log(username.value)
    // console.log(group_id.value)   
    // console.log(csrftoken.value) 
    e.preventDefault()

    fetch(
        "/user/send",
        {
            method:"POST",
            headers:{
                'Content-Type':'application/json',
                "X-CSRFToken": getCookie("csrftoken")
            },
            body:JSON.stringify({
                username : username.value,
                group_id : group_id.value,
                message : message.value,
                // csrftoken:csrftoken.value                     
            }),
        }
    )           
                .then((res)=>res.json())
 
                .then((data)=>{
                    //console.log(data)
                    console.log(data)
                })
                .catch((error) => {
                    console.error('Error:', error);
                  });
                  message.value = ''
                  //console.log("data fetched")
                
};



