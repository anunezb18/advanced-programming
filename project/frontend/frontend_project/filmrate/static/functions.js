const URL_BASE = 'http://localhost:8000'; // URL del contenedor FastAPI

async function createUser() {
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

async function c() {
    let data = {
        email: document.getElementById('email').value,
        username: document.getElementById('username').value,
        password: document.getElementById('password').value
    };
    console.log(data)

    let url_post = URL_BASE + '/users/register'

    try {
        const response = await fetch(url_post, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': 'http://localhost:5500',
                "Access-Control-Allow-Methods": "POST"
            },
            body: JSON.stringify(data)
        });
        const result = await response.json();
        alert(result.message)
    } catch (error) {
        console.error('Error:', error);
    }
}