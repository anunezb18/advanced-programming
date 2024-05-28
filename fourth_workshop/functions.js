async function callMessage() {
    try {
        const response = await fetch('http://localhost:8002/hello_ud'); // Se incluyó el puerto
        const data = await response.text();
        document.getElementById('result').textContent = data;
    } catch (error) {
        console.error('Error:', error);
    }
}

async function callTable() {
    try {
        const response = await fetch('http://localhost:8002/get_products'); // Se incluyó el puerto
        const data = await response.json();
        
        if (data.length === 0) {
            document.getElementById('result').innerHTML = "No products found";
        } else {
            let table = '<table>';
            table += '<tr><th>ID</th><th>Name</th><th>Description</th></tr>';
            
            data.forEach(item => {
                table += `<tr><td>${item.id}</td><td>${item.name}</td><td>${item.description}</td></tr>`;
            });
            
            table += '</table>';
            
            document.getElementById('result').innerHTML = table;
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

async function showForm() {
    // Obtén el div que contiene el formulario
    const formDiv = document.getElementById('form');

    // Cambia el estilo para mostrar el div
    formDiv.style.display = 'block';
}

async function addProduct() {
    // Obtén los valores del formulario
    const productIdElement = document.getElementById('productId');
    const nameElement = document.getElementById('name');
    const descriptionElement = document.getElementById('description');

    const id = productIdElement.value;
    const name = nameElement.value;
    const description = descriptionElement.value;

    // Crea un objeto con los datos del producto
    const product = { id, name, description };

    try {
        // Envía una solicitud POST al servidor
        const response = await fetch('http://localhost:8002/create_products', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(product),
        });

        // Verifica si la solicitud fue exitosa
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Borra los valores del formulario
        productIdElement.value = '';
        nameElement.value = '';
        descriptionElement.value = '';

        // Actualiza la página o haz algo con la respuesta
        console.log('Product added successfully');
    } catch (error) {
        console.error('Error:', error);
    }

    // Borra los valores del formulario
    productIdElement.value = '';
    nameElement.value = '';
    descriptionElement.value = '';
}