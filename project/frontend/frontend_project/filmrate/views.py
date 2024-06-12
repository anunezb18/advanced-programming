from django.shortcuts import render

def index(request):
    films_list = [
        {
            "film_title": "Inception",
            "username": "DreamMaster007",
            "stars": "5",
            "review": "Inception is a mind-bending masterpiece that keeps you guessing till the very end. The visuals are stunning, the plot is intricately woven, and Leonardo DiCaprio delivers a stellar performance. A must-watch!",
            "image": "https://th.bing.com/th/id/R.be7248985232d46128041023c99fad7d?rik=m%2fYm13OWgvgEMQ&riu=http%3a%2f%2fwww.nolanfans.com%2fimages%2fposters%2finception%2fp4xfull.jpg&ehk=fTBnrxgKiU4dJQxZMWXrFmdjr5dpguBG6osjjkLxxPA%3d&risl=1&pid=ImgRaw&r=0"
        },
        {
            "film_title": "The Shawshank Redemption",
            "username": "MovieManiac22",
            "stars": "5",
            "review": "Shawshank Redemption is a timeless classic. The story of hope and friendship in the face of adversity is beautifully portrayed. Morgan Freeman's narration is impeccable, and the climax is deeply satisfying.",
            "image": "https://th.bing.com/th/id/R.ca86e305130c75e910bd9c061de79b2a?rik=ykKcDajgJ36i%2fQ&pid=ImgRaw&r=0"
        },
        {
            "film_title": "Pulp Fiction",
            "username": "VincentVega89",
            "stars": "4",
            "review": "Pulp Fiction is a bold and unconventional film that showcases Tarantino's genius. The nonlinear narrative and eclectic characters make it a cult favorite. Though complex, it's a must-see for cinephiles.",
            "image": "https://www.themoviedb.org/t/p/original/pbWgQPC6l9pkpEpi3WNRSfWYNP6.jpg"
        },
        {
            "film_title": "The Dark Knight",
            "username": "GothamCitizen",
            "stars": "5",
            "review": "The Dark Knight is not just a superhero movie; it's a crime drama masterpiece. Heath Ledger's Joker is iconic, and Christian Bale's Batman is broodingly intense. The action sequences are gripping, and the moral dilemmas are thought-provoking.",
            "image": "https://th.bing.com/th/id/OIP.rvxkm3ZswfeGymXwjT686wHaLG?rs=1&pid=ImgDetMain"
        },
        {
            "film_title": "Interstellar",
            "username": "SpaceExplorer99",
            "stars": "4",
            "review": "Interstellar blends science fiction with emotional depth. Christopher Nolan's direction is ambitious, and the visual effects are breathtaking. While the plot can be dense, the exploration of love and humanity resonates deeply.",
            "image": "https://th.bing.com/th/id/OIP.s5tfuwOgumzCl5XtUezX6gAAAA?rs=1&pid=ImgDetMain"
        },
        {
            "film_title": "La La Land",
            "username": "JazzLover23",
            "stars": "5",
            "review": "La La Land is a delightful homage to classic musicals, with stunning performances by Emma Stone and Ryan Gosling. The cinematography is breathtaking, and the music is unforgettable. It's a charming and heartwarming film that captures the magic of dreams and love.",
            "image": "https://lh3.googleusercontent.com/drive-viewer/AKGpihbn4qcPWxlwm0r0x5mvAOQKf4H35jFNNu47LKnVTyioF025SpyLqwC_ULLVCCW85nWAwRoErV4-QWNMoUeHmnN6mTnyBhkWrg=w1868-h942-rw-v1"
        },
        {
            "film_title": "Iron Man",
            "username": "TechGeek45",
            "stars": "5",
            "review": "Iron Man is the perfect blend of action, humor, and heart. Robert Downey Jr.'s portrayal of Tony Stark is charismatic and compelling, setting the stage for the Marvel Cinematic Universe. The special effects and action sequences are top-notch, making it a thrilling watch from start to finish.",
            "image": "https://th.bing.com/th/id/OIP.OGVZpS7cGCeeXGEyPkJhaAHaLH?rs=1&pid=ImgDetMain"
        },
        {
            "film_title": "Django Unchained",
            "username": "WesternFan88",
            "stars": "4",
            "review": "Django Unchained is a bold and gritty take on the Western genre, with Quentin Tarantino's signature style. Jamie Foxx and Christoph Waltz deliver powerful performances, and the film's blend of dark humor and intense action is captivating. It's a revenge tale that's both brutal and exhilarating.",
            "image": "https://lh3.googleusercontent.com/drive-viewer/AKGpihZvNa7hNMJ5m91_I2mnbUo_SwaVaRfQ2bCjbrTNGc4X3xOk9FRscN8t3kUddpN-aJI2q4cPwzqxy_cAehF8wEH8EeHA6crI0kY=w1868-h942-rw-v1"
        },
        {
            "film_title": "Titanic",
            "username": "RoseDawson98",
            "stars": "4",
            "review": "Titanic is an epic romance set against the tragic backdrop of the ship's sinking. Leonardo DiCaprio and Kate Winslet's chemistry is palpable, and James Cameron's direction captures the grandeur and heartbreak of the disaster. A captivating story of love and loss.",
            "image": "https://lh3.googleusercontent.com/drive-viewer/AKGpihZvNa7hNMJ5m91_I2mnbUo_SwaVaRfQ2bCjbrTNGc4X3xOk9FRscN8t3kUddpN-aJI2q4cPwzqxy_cAehF8wEH8EeHA6crI0kY=w1868-h942-rw-v1"
        },
        {
            "film_title": "The Godfather",
            "username": "DonCorleone55",
            "stars": "5",
            "review": "The Godfather is a cinematic masterpiece that defines the gangster genre. Marlon Brando's performance as Vito Corleone is iconic, and the storytelling is rich with tension and drama. A timeless classic.",
            "image": "https://th.bing.com/th/id/OIP.3C9P6X2vrW-EGjNpsSMgyQHaK9?rs=1&pid=ImgDetMain"
        },

    ]
    return render(request, 'index.html', {"films": films_list})


def home(request):
    films_list = [
        {
            "film_title": "Inception",
            "username": "DreamMaster007",
            "stars": "5",
            "review": "Inception is a mind-bending masterpiece that keeps you guessing till the very end. The visuals are stunning, the plot is intricately woven, and Leonardo DiCaprio delivers a stellar performance. A must-watch!",
            "image": "https://th.bing.com/th/id/R.be7248985232d46128041023c99fad7d?rik=m%2fYm13OWgvgEMQ&riu=http%3a%2f%2fwww.nolanfans.com%2fimages%2fposters%2finception%2fp4xfull.jpg&ehk=fTBnrxgKiU4dJQxZMWXrFmdjr5dpguBG6osjjkLxxPA%3d&risl=1&pid=ImgRaw&r=0"
        },
        {
            "film_title": "The Shawshank Redemption",
            "username": "MovieManiac22",
            "stars": "5",
            "review": "Shawshank Redemption is a timeless classic. The story of hope and friendship in the face of adversity is beautifully portrayed. Morgan Freeman's narration is impeccable, and the climax is deeply satisfying.",
            "image": "https://th.bing.com/th/id/R.ca86e305130c75e910bd9c061de79b2a?rik=ykKcDajgJ36i%2fQ&pid=ImgRaw&r=0"
        },
        {
            "film_title": "Pulp Fiction",
            "username": "VincentVega89",
            "stars": "4",
            "review": "Pulp Fiction is a bold and unconventional film that showcases Tarantino's genius. The nonlinear narrative and eclectic characters make it a cult favorite. Though complex, it's a must-see for cinephiles.",
            "image": "https://www.themoviedb.org/t/p/original/pbWgQPC6l9pkpEpi3WNRSfWYNP6.jpg"
        },
        {
            "film_title": "The Dark Knight",
            "username": "GothamCitizen",
            "stars": "5",
            "review": "The Dark Knight is not just a superhero movie; it's a crime drama masterpiece. Heath Ledger's Joker is iconic, and Christian Bale's Batman is broodingly intense. The action sequences are gripping, and the moral dilemmas are thought-provoking.",
            "image": "https://th.bing.com/th/id/OIP.rvxkm3ZswfeGymXwjT686wHaLG?rs=1&pid=ImgDetMain"
        },
        {
            "film_title": "Interstellar",
            "username": "SpaceExplorer99",
            "stars": "4",
            "review": "Interstellar blends science fiction with emotional depth. Christopher Nolan's direction is ambitious, and the visual effects are breathtaking. While the plot can be dense, the exploration of love and humanity resonates deeply.",
            "image": "https://th.bing.com/th/id/OIP.s5tfuwOgumzCl5XtUezX6gAAAA?rs=1&pid=ImgDetMain"
        },
        {
            "film_title": "La La Land",
            "username": "JazzLover23",
            "stars": "5",
            "review": "La La Land is a delightful homage to classic musicals, with stunning performances by Emma Stone and Ryan Gosling. The cinematography is breathtaking, and the music is unforgettable. It's a charming and heartwarming film that captures the magic of dreams and love.",
            "image": "https://lh3.googleusercontent.com/drive-viewer/AKGpihbn4qcPWxlwm0r0x5mvAOQKf4H35jFNNu47LKnVTyioF025SpyLqwC_ULLVCCW85nWAwRoErV4-QWNMoUeHmnN6mTnyBhkWrg=w1868-h942-rw-v1"
        },
        {
            "film_title": "Iron Man",
            "username": "TechGeek45",
            "stars": "5",
            "review": "Iron Man is the perfect blend of action, humor, and heart. Robert Downey Jr.'s portrayal of Tony Stark is charismatic and compelling, setting the stage for the Marvel Cinematic Universe. The special effects and action sequences are top-notch, making it a thrilling watch from start to finish.",
            "image": "https://th.bing.com/th/id/OIP.OGVZpS7cGCeeXGEyPkJhaAHaLH?rs=1&pid=ImgDetMain"
        },
        {
            "film_title": "Django Unchained",
            "username": "WesternFan88",
            "stars": "4",
            "review": "Django Unchained is a bold and gritty take on the Western genre, with Quentin Tarantino's signature style. Jamie Foxx and Christoph Waltz deliver powerful performances, and the film's blend of dark humor and intense action is captivating. It's a revenge tale that's both brutal and exhilarating.",
            "image": "images/django_unchained.png"
        },
        {
            "film_title": "Titanic",
            "username": "RoseDawson98",
            "stars": "4",
            "review": "Titanic is an epic romance set against the tragic backdrop of the ship's sinking. Leonardo DiCaprio and Kate Winslet's chemistry is palpable, and James Cameron's direction captures the grandeur and heartbreak of the disaster. A captivating story of love and loss.",
            "image": "https://lh3.googleusercontent.com/drive-viewer/AKGpihZvNa7hNMJ5m91_I2mnbUo_SwaVaRfQ2bCjbrTNGc4X3xOk9FRscN8t3kUddpN-aJI2q4cPwzqxy_cAehF8wEH8EeHA6crI0kY=w1868-h942-rw-v1"
        },
        {
            "film_title": "The Godfather",
            "username": "DonCorleone55",
            "stars": "5",
            "review": "The Godfather is a cinematic masterpiece that defines the gangster genre. Marlon Brando's performance as Vito Corleone is iconic, and the storytelling is rich with tension and drama. A timeless classic.",
            "image": "https://th.bing.com/th/id/OIP.3C9P6X2vrW-EGjNpsSMgyQHaK9?rs=1&pid=ImgDetMain"
        },

    ]

    return render(request, 'home.html', {'films': films_list})

def sign_in(request):
    return render(request, 'sign_in.html')

def create_account(request):
    return render(request, 'create_account.html')

def films(request):
    return render(request, 'films.html')

def details_film(request):
    return render(request, 'film_template.html')

def films_user(request):
    return render(request, 'films_user.html')


def my_watchlist(request):
    watchlist = [
        {
            "name": "Her",
            "description": "It's a movie of marvel studios",
            "stars": "5",
            "image": "images/1.png"
        },
        {
            "name": "Joker",
            "description": "It's a movie of marvel studios",
            "stars": "4",
            "image": "images/2.png"
        },
        {
            "name": "Infinity war",
            "description": "It's a movie of marvel studios",
            "stars": "1",
            "image": "images/1.png"
        },
        {
            "name": "Infinity war",
            "description": "It's a movie of marvel studios",
            "stars": "3",
            "image": "images/1.png"
        },
        {
            "name": "Infinity war",
            "description": "It's a movie of marvel studios",
            "stars": "2",
            "image": "images/1.png"
        },
        {
            "name": "Infinity war",
            "description": "It's a movie of marvel studios",
            "stars": "5",
            "image": "images/1.png"
        }
    ]
    return render(request, 'my_watchlist.html', {"watchlist": watchlist})

def user(request):
    return render(request, 'user.html')

