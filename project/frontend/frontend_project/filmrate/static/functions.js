const URL_BASE = 'http://localhost:8080'; // URL del contenedor FastAPI

async function hello_ud() {
    try {
        const response = await fetch(URL_BASE + '/hello_ud');
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        const data = await response.text();
        document.getElementById('result').textContent = data;
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('result').textContent = 'Error fetching data';
    }
}

async function createUser() {
    let data = {
        username: document.getElementById('username').value,
        password: document.getElementById('password').value,
        email: document.getElementById('email').value
    };
    console.log(data)

    let url_post = URL_BASE + '/users/register'

    fetch(url_post, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log("Success:", data);
    })
    .catch((error) => {
        console.error("Error:", error);
    });
}