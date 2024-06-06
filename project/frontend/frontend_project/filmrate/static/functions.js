let URL_BASE = "http://localhost:8080"

async function registerUser() {
    const form = document.getElementById('registerForm');
    const formData = new FormData(form);
    const data = {
        username: formData.get('username'),
        password: formData.get('password'),
        email: formData.get('email')
    };

    try {
        const response = await fetch('http://127.0.0.1:8000/users/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        alert(result.message);
    } catch (error) {
        console.error('Error:', error);
        alert('Error registering user');
    }
}




async function callMessage() {
    try {
        const response = await fetch(URL_BASE + '/user/login');
        const data = await response.text();
        document.getElementById('result').textContent = data;
    } catch (error) {
        console.error('Error:', error);
    }
}

async function callTable() {
    try {
        const response = await fetch(URL_BASE + '/products');
        const data = await response.json();
        
        let table = '<table>';
        table += '<tr><th>ID</th><th>Name</th><th>Description</th></tr>';
        
        data.forEach(item => {
            table += `<tr><td>${item.id}</td><td>${item.name}</td><td>${item.description}</td></tr>`;
        });
        
        table += '</table>';
        
        document.getElementById('result').innerHTML = table;
    } catch (error) {
        console.error('Error:', error);
    }
}
