const URL_BASE = 'http://localhost:8080'; // URL del contenedor FastAPI

// It collects the user data, saves it in the local storage, and sends a POST request to a server 
// to register the new user.
async function createAccount() {

    // Retrieve user input values from the HTML document
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const email = document.getElementById('email').value;

    // Create an object containing the user data
    let data = {
        username: username,
        password: password,
        email: email
    };
    console.log(data);

    // Store the username and password in the browser's local storage
    localStorage.setItem('username', username);
    localStorage.setItem('password', password);

    // Define the URL for the POST request
    let url_post = URL_BASE + '/users/register';

    // Send a POST request to the server to register the new user
    fetch(url_post, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json()) // Parse the JSON response
    .then(data => {
        console.log(data);
        
        // Define possible responses for comparison
        const aux1 = data;
        const aux2 = {"message": "Username is already in use. Please choose another one."};
        const aux3 = {"message": "User registered successfully"};

        // Handle server response
        if (aux1.message === aux2.message) {
            alert(aux2.message); // Alert if username is already in use
        } else if (aux1.message === aux3.message) {
            alert(aux3.message); // Alert if registration is successful
            window.location.href = 'http://localhost:8000/home'; // Redirect to home page
        }
        
    })
    .catch((error) => {
        alert("Error:", error); // Alert if there's an error during the fetch
    });
}


async function signIn() {

    // Retrieves the value of the inputs from the HTML document.
    const username = document.getElementById('username_user').value;
    const password = document.getElementById('password_user').value;

    // Store the username and password in the browser's local storage
    localStorage.setItem('username', username);
    localStorage.setItem('password', password);

    // Creates an object containing the user data.
    let data = {
        username: username,
        password: password,
    };
    console.log(data); // Logs the collected data for verification.

    // Defines the URL for the POST request, combining a base URL with the login endpoint.
    let url_post = URL_BASE + '/users/login';

    // Sends an HTTP POST request to the server with the user data.
    fetch(url_post, {
        method: "POST", 
        headers: {
            "Content-Type": "application/json" 
        },
        body: JSON.stringify(data) // Converts the data object to a JSON string for sending.
    })
    .then(response => response.json()) // Converts the server's response to JSON format.
    .then(data => {
        console.log(data); 

        // Stores the server's response in a variable for comparison.
        let aux1 = data;
        let aux2 = { "message": "User logged in successfully" };

        // Compares the server's response with the expected message.
        if (aux1.message === aux2.message) {
            alert(aux2.message); // Alerts if login was successful.
            window.location.href = 'http://localhost:8000/home'; // Redirects the user to the home page.
        } else {
            alert("Invalid username or password"); // Alerts if login fails.
        }
        
    })
    .catch((error) => {
        alert("Error:", error); // Alerts if there's an error during the fetch.
    });
}

async function signOut(){
    localStorage.removeItem('username');
    localStorage.removeItem('password');
    document.getElementById('username_header').innerText = "Username";
    document.getElementById('username_banner').innerText = '';
}

// Search for the films
async function searchFilmHome() {

    // Retrieve the value of the input field with the id 'title' from the HTML document.
    const title = document.getElementById('title').value;
    
    // Check if the title is empty or only whitespace.
    if (!title.trim()) {
        alert("Title must not be empty or only whitespace");
        return; 
    }
    
    try {
        // Send an HTTP POST request to the server to search for films by title.
        const response = await fetch(URL_BASE + '/films/search', {
            method: 'POST', 
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ title: title }) 
        });

        // Check if the response status is not OK (successful).
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText); 
        }

        // Update the page content to indicate that films are being searched.
        document.getElementById('found_films').textContent = 'Found films ...';
        
        // Redirect the user to the section where the films are displayed.
        window.location.href = 'http://localhost:8000/home/#found_films';

        // Parse the response JSON data.
        const data = await response.json();
        let film = "";

        // Iterate over each film data and create HTML elements for each film.
        data.forEach(data => {
            console.log(data.title); // Log the title of each film for verification.
            film += `<div class="container_film">
                        <img src="${data.cover}" alt="pelicula">
                        <div class="info_film">
                            <h3 class="text_film"><a href="#" onclick="detailsFilm(${data.code})">${data.title}</a></h3>
                            <p class="p_film"></p>
                        </div>
                    </div>`;
        });

        // Update the inner HTML of the element with id 'peliculas' with the film elements.
        document.getElementById('peliculas').innerHTML = film;
        
    } catch (error) {
        // Log any errors that occur during the fetch process.
        console.error('Error:', error);
    }
}

// Search for the films
async function searchFilm() {

    // Retrieve the value of the input field with the id 'title' from the HTML document.
    const title = document.getElementById('title').value;
    
    // Check if the title is empty or only whitespace.
    if (!title.trim()) {
        alert("Title must not be empty or only whitespace");
        return; // Exit the function if the title is invalid.
    }
    
    try {
        // Send an HTTP POST request to the server to search for films by title.
        const response = await fetch(URL_BASE + '/films/search', {
            method: 'POST', // Define the HTTP method as POST.
            headers: {
                'Content-Type': 'application/json' // Specify that the request content is JSON.
            },
            body: JSON.stringify({ title: title }) // Convert the title to a JSON string for sending.
        });

        // Check if the response status is not OK (successful).
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText); // Throw an error if the response is not OK.
        }

        // Update the page content to indicate that films are being searched.
        document.getElementById('found_films').textContent = 'Found films ...';
        
        // Redirect the user to the section where the films are displayed.
        window.location.href = 'http://localhost:8000/films/#found_films';

        // Parse the response JSON data.
        const data = await response.json();
        let film = "";

        // Iterate over each film data and create HTML elements for each film.
        data.forEach(data => {
            console.log(data.title); // Log the title of each film for verification.
            film += `<div class="container_film">
                        <img src="${data.cover}" alt="pelicula">
                        <div class="info_film">
                            <h3 class="text_film"><a href="#" onclick="detailsFilm(${data.code})">${data.title}</a></h3>
                            <p class="p_film"></p>
                        </div>
                    </div>`;
        });

        // Update the inner HTML of the element with id 'peliculas' with the film elements.
        document.getElementById('peliculas').innerHTML = film;
        
    } catch (error) {
        // Log any errors that occur during the fetch process.
        console.error('Error:', error);
    }
}

// Show the films
async function films() {
    // Send a GET request to the server to fetch the list of films.
    fetch(URL_BASE + '/films')
        .then(response => {

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json(); // Convert the response to JSON format.
        })
        .then(films => {
            let film = "";

            // Iterate through each film data and create HTML elements for each film.
            films.forEach(film => {
                console.log(film.title); // Log the title of each film for verification.
                film += `<div class="container_film">
                            <img src="${film.cover}" alt="poster film">
                            <div class="info_film">
                                <h3 class="text_film"><a href="">${film.title}</a></h3>
                                <p class="p_film"></p>
                            </div>
                        </div>`;
            });

            // Update the inner HTML of the element with id 'container_films' with the film elements.
            document.getElementById('container_films').textContent = film;
        })
        .catch(error => {
            // Log any errors that occur during the fetch process.
            console.error('Error fetching films:', error);
        });
}


// Show the films
// async function films() {
//     try {
//         // Send an HTTP GET request to fetch the list of films from the server.
//         const response = await fetch(URL_BASE + '/films', {
//             method: 'GET', 
//             headers: {
//                 'Content-Type': 'application/json' 
//             },
//             // body: JSON.stringify() // No need for a body in a GET request, but included for consistency.
//         });

//         // Parse the response JSON data.
//         const data = await response.json();
//         let film = "";

//         // Iterate through each film data and create HTML elements for each film.
//         data.forEach(film => {
//             console.log(film.title); // Log the title of each film for verification.
//             film += `<div class="container_film">
//                         <img src="${film.cover}" alt="poster film">
//                         <div class="info_film">
//                             <h3 class="text_film"><a href="">${film.title}</a></h3>
//                             <p class="p_film"></p>
//                         </div>
//                     </div>`;
//         });

//         // Update the inner HTML of the element with id 'container_films' with the film elements.
//         document.getElementById('container_films').innerHTML = film;
        
//     } catch (error) {
//         // Log any errors that occur during the fetch process.
//         console.error('Error:', error);
//     }
// }

async function infoUser(){
    const username = localStorage.getItem('username');
    document.getElementById('username_header').textContent = username;
}


// async function getUserInfo(username) {
//     try {
//         const response = await fetch(`http://localhost:8080/users/${username}`, {
//             method: 'GET', 
//             headers: {
//                 'Content-Type': 'application/json' 
//             },
//             body: JSON.stringify()
//         });
        
//         if (!response.ok) {
//             throw new Error('Network response was not ok ' + response.statusText);
//         }

//         const data = await response.json();
        
//         if (data.message) {
//             console.error(data.message);
//             return;
//         }

//         console.log(`Username: ${data.username}`);
//         console.log(`Email: ${data.email}`);
//         console.log(`Watchlist: ${data.watchlist}`);
        
        
//         document.getElementById('email_info').textContent = data.email;
//         document.getElementById('username_info').textContent = data.username;

//     } catch (error) {
//         console.error('There was a problem with the fetch operation:', error);
//     }
// }


async function detailsFilm(codigo){
    try{
        const response = await fetch(URL_BASE + '/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify()
        });

        const data = await response.json();
        let film = "";

        data.forEach(data => {
            console.log(data.title)
            film += `<div class="container_film">
                        <img src="${data.poster}" alt="poster film">
                        <div class="info_film">
                            <h3 class="text_film"><a href="">${data.title}</a></h3>
                            <p class="p_film"></p>
                        </div>
                    </div>`;
        });

        document.getElementById('container_films').innerHTML = film;
        
    } catch (error) {
        console.error('Error:', error);
    }
}