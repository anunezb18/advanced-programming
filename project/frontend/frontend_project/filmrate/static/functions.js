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
    window.location.href = 'http://localhost:8000';
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
                            <h3 class="text_film" onclick="filmID(${data.code})"><a href="http://localhost:8000/details_film" class="name_film">${data.title}</a></h3>
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
async function searchFilmUser() {

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
        window.location.href = 'http://localhost:8000/films_user/#found_films';

        // Parse the response JSON data.
        const data = await response.json();
        let film = "";

        // Iterate over each film data and create HTML elements for each film.
        data.forEach(data => {
            console.log(data.title); // Log the title of each film for verification.
            film += `<div class="container_film">
                        <img src="${data.cover}" alt="pelicula">
                        <div class="info_film">
                            <h3 class="text_film" onclick="filmID(${data.code})"><a href="http://localhost:8000/details_film" class="name_film">${data.title}</a></h3>
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
async function searchFilmWatchlist() {

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
        window.location.href = 'http://localhost:8000/my_watchlist/#found_films';

        // Parse the response JSON data.
        const data = await response.json();
        let film = "";
        rate = "";

        // Iterate over each film data and create HTML elements for each film.
        data.forEach(data => {
            score = data.score
            if (score === 1){
                rate = `<i class="fa-solid fa-star"></i>`;
            }else if(score === 2){
                rate = `<i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>`;
            }else if(score === 3){
                rate = `<i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>`;
            }else if(score === 4){
                rate = `<i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>`;
            }else if(score === 5){
                rate = `<i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>`;
            }

            console.log(data.title); // Log the title of each film for verification.
            film += `<div class="container_film">
                        <img src="${data.cover}" alt="pelicula">
                        <div class="info_film">
                            <h3 class="text_film" onclick="filmID(${data.code})"><a href="http://localhost:8000/details_film" class="name_film">${data.title}</a></h3>
                            <div class="rating">${rate}</div>
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
async function searchFilmIndex() {

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
        window.location.href = 'http://localhost:8000/#found_films';

        // Parse the response JSON data.
        const data = await response.json();
        let film = "";

        let rate;

        // Iterate over each film data and create HTML elements for each film.
        data.forEach(data => {
            console.log(data.title); // Log the title of each film for verification.

            score = data.score
            if (score === 1){
                rate = `<i class="fa-solid fa-star"></i>`;
            }else if(score === 2){
                rate = `<i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>`;
            }else if(score === 3){
                rate = `<i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>`;
            }else if(score === 4){
                rate = `<i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>`;
            }else if(score === 5){
                rate = `<i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>`;
            }

            film += `<div class="container_film">
                        <img src="${data.cover}" alt="pelicula">
                        <div class="info_film">
                            <h3 class="text_film" onclick="filmID(${data.code})"><a href="http://localhost:8000/details_film" class="name_film">${data.title}</a></h3>
                            <p class="p_film">${rate}</p>
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
        let rate = "";

        // Iterate over each film data and create HTML elements for each film.
        data.forEach(data => {
            console.log(data.title); // Log the title of each film for verification.
            score = data.score
            
            if (score === 1){
                rate += `<i class="fa-solid fa-star"></i>`;
            }else if(score === 2){
                rate += `<i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>`;
            }else if(score === 3){
                rate += `<i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>`;
            }else if(score === 4){
                rate += `<i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>`;
            }else if(score === 5){
                rate += `<i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>`;
            }

            film += `<div class="container_film">
                        <img src="${data.cover}" alt="pelicula">
                        <div class="info_film">
                            <h3 class="text_film" onclick="filmID(${data.code})"><a href="http://localhost:8000/details_film" class="name_film">${data.title}</a></h3>
                           <div class="rating">${rate}</div>
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

//Show films
async function films() {
    
    try {
        // Send an HTTP POST request to the server to search for films by title.
        const response = await fetch(URL_BASE + '/films', {
            method: 'GET', 
            headers: {
                'Content-Type': 'application/json' 
            },
            body: JSON.stringify() 
        });

        // Check if the response status is not OK (successful).
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText); // Throw an error if the response is not OK.
        }

        // Parse the response JSON data.
        const data = await response.json();
        let film = "";
        
        let rate = "";
        let score;

        // Iterate over each film data and create HTML elements for each film.
        data.forEach(data => {
            console.log(data.title); // Log the title of each film for verification.
            score = data.score
            if (score === 1){
                rate = `<i class="fa-solid fa-star"></i>`;
            }else if(score === 2){
                rate = `<i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>`;
            }else if(score === 3){
                rate = `<i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>`;
            }else if(score === 4){
                rate = `<i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>`;
            }else if(score === 5){
                rate = `<i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>`;
            }

            film += `<div class="container_film">
                        <img src="${data.cover}" alt="pelicula">
                        <div class="info_film">
                            <h3 class="text_film" onclick="filmID(${data.code})"><a href="http://localhost:8000/details_film" class="name_film">${data.title}</a></h3>
                            <div class="rating">${rate}</div>
                        </div>
                    </div>`;

            rate = "";
        });

        // Update the inner HTML of the element with id 'peliculas' with the film elements.
        document.getElementById('container_films').innerHTML = film;
        
    } catch (error) {
        // Log any errors that occur during the fetch process.
        console.error('Error:', error);
    }
}

// Store the film code
async function filmID(filmId) {
    localStorage.setItem('filmId', filmId);
}


// Show the film info
async function detailsFilm(film_code){
    try{
        const response = await fetch(URL_BASE + `/films/${film_code}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });
    
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
    
        const filmData = await response.json();
        const score = filmData.score;
        console.log(score)
        
        let rate = "";

        if (score === 1){
            rate += `<i class="fa-solid fa-star"></i>`;
        }else if(score === 2){
            rate += `<i class="fa-solid fa-star"></i>
                    <i class="fa-solid fa-star"></i>`;
        }else if(score === 3){
            rate += `<i class="fa-solid fa-star"></i>
                    <i class="fa-solid fa-star"></i>
                    <i class="fa-solid fa-star"></i>`;
        }else if(score === 4){
            rate += `<i class="fa-solid fa-star"></i>
                    <i class="fa-solid fa-star"></i>
                    <i class="fa-solid fa-star"></i>
                    <i class="fa-solid fa-star"></i>`;
        }else if(score === 5){
            rate += `<i class="fa-solid fa-star"></i>
                    <i class="fa-solid fa-star"></i>
                    <i class="fa-solid fa-star"></i>
                    <i class="fa-solid fa-star"></i>
                    <i class="fa-solid fa-star"></i>`;
        }

        let info = "";
        let img = "";

        img += `<div class="film_img">
                    <img src="${filmData.cover}" alt="poster film">
                </div>`

        info += `<div class="film_info">
                    <div class="film_title">
                        <h3>${filmData.title}</h3>
                    </div>
                    <div class="rating">${rate}</div>
                    <p class="film_descrition"><b>Director: </b>${filmData.director}</p>
                    <p class="film_descrition"><b>Year: </b>${filmData.year}</p>
                    <p class="film_descrition"><b>Lenght: </b>${filmData.lenght}</p>
                    <p class="film_descrition"><b>Crew: </b>${filmData.crew}</p>
                    <p class="film_descrition">${filmData.synopsis}</p>
                </div>`;

        document.getElementById('details_img').innerHTML = img;
        document.getElementById('details_info').innerHTML = info;

    }catch (error) {
        console.error('Error:', error);
    }
}


async function infoUser(){
    const username = localStorage.getItem('username');
    document.getElementById('username_header').textContent = username;
}

// Show watchlist
async function getWatchlist(username) {
    try {
        const response = await fetch(URL_BASE + '/users/watchlist', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username: username })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const watchlist = await response.json();
        console.log(watchlist)
        
        let film = "";

        // Iterate over each film data and create HTML elements for each film.
        watchlist.forEach(data => {
            console.log(data.title); // Log the title of each film for verification.
            film += `<div class="container_film">
                        <img src="${data.cover}" alt="pelicula">
                        <div class="info_film">
                            <h3 class="text_film" onclick="filmID(${data.code})"><a href="http://localhost:8000/details_film" class="name_film">${data.title}</a></h3>
                            <p class="p_film"></p>
                        </div>
                    </div>`;
        });

        // Update the inner HTML of the element with id 'container_watchlist' with the film elements.
        document.getElementById('container_watchlist').innerHTML = film;
        
    } catch (error) {
        alert(error.message);
    }
}

async function addWatchlist(username, filmId){
    try {
        const response = await fetch(URL_BASE + `/users/add_to_watchlist`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username: username, film_id: filmId })
        });

        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }

        const data = await response.json();
        console.log(data.message);  // Muestra el mensaje de éxito en la consola
        alert(data.message);  // Muestra el mensaje de éxito en una alerta

    } catch (error) {
        console.error('Error:', error);
        alert('Could not add to watchlist');
    }

}

// Show the user info
async function getInfoUser(username){
    try {
        const response = await fetch(`http://localhost:8080/users/${username}`, {
            method: 'GET', 
            headers: {
                'Content-Type': 'application/json' 
            },
            body: JSON.stringify()
        });
                
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        
        const data = await response.json();
        const watchlist_user = data.watchlist;

        let info = "";

        info += `<h2>Infomation: </h2>
                <p><b>Username: </b>${data.username}</p>
                <p><b>Gmail: </b>${data.email}</p>`;
    

        document.getElementById('info').innerHTML = info;
        
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
    }
}

// async function getReviews(film_code){
//     try {
//         const response = await fetch(URL_BASE + `/films/${film_code}/reviews`, {
//             method: 'GET',
//             headers: {
//                 'Content-Type': 'application/json'
//             }
//         });

//         if (!response.ok) {
//             throw new Error('Network response was not ok ' + response.statusText);
//         }

//         const data = await response.json();
//         console.log(data);  // Verificar la estructura de la respuesta aquí

        

//         // let reviews_info = "";

//         // if (reviews.length === 0) {
//         //     reviewsHTML += `<p>No hay reseñas para esta película.</p>`;
//         // } else {

//         // }

//         // let reviews_info = "";
//         // reviews.forEach(review => {
//         //     reviews_info += `<div class="review">
//         //                         <div class="username">
//         //                             <div><img src="${review.cover}" alt="poster film"></div>
//         //                             <div><i class="fa-solid fa-circle-user"></i></div>
//         //                             <div><p><b>${review.username}</b></p></div>
//         //                         </div>
//         //                         <div class="rating"></div>
//         //                         <p>${review.text}</p>
//         //                     </div>`;
//         // });

//         // document.getElementById('reviews').innerHTML = reviews_info;

//     } catch (error) {
//         console.error('Error:', error);
//     }
// }