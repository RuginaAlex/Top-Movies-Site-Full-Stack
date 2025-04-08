# 🎬 My Top Movies


🚀 **Try it out here → [my-top-movies-cf1r.onrender.com](https://my-top-movies-cf1r.onrender.com)**  


**My Top Movies** is a full-stack Flask web application that lets users search for films via the [TMDB API](https://www.themoviedb.org/), crate a personalized top movie list, and manage reviews and ratings in a clean and responsive UI.

Deployed with [Render](https://render.com/), this project also features user authentication, API integration, dark mode styling, and custom UI animations.

[![Built with Flask](https://img.shields.io/badge/Built%20With-Flask-orange)](https://flask.palletsprojects.com/) [![TMDB API](https://img.shields.io/badge/API-TMDB-brightgreen)](https://www.themoviedb.org/documentation/api)

---

## 🌟 Features

- 🔐 **User Registration & Login** – Secure authentication system with password hashing.
- 🔍 **Movie Search** – Find movies using the TMDB API and select them from search results.
- ⭐ **Rate & Review** – Assign a score out of 10 and leave a custom review.
- 📋 **Top Movies** – Manage your personalized list, sorted by rating.
- 🖊️ **Edit & Delete** – Modify your ratings or remove a movie anytime.
- 🧠 **Smart Duplicate Check** – Prevent adding the same movie twice.
- 🎨 **Responsive UI** – Bootstrap 5 + custom styles, mobile-friendly design.
- 🍿 **Interactive Effects** – Custom JavaScript animations (like popcorn burst 🎉).
- 🧪 **API-Driven Content** – Live trending and Oscar-predicted movies from TMDB.
- 🌍 **Deployed on Render** – With a `/ping` route for UptimeRobot integration.

---

## 🖼️ Screenshots  
*Click any image to view it in full size.*


| 🏠 Home Page (Not Logged In) | 🏆 Oscar & Trending Movies |
|-----------------------------|----------------------------|
| ![](presentation/ss/home_guest.png)      | ![](presentation/ss/oscar_trending.png) |

| 🔍 Search & Add Movies       | ✅ Add to Top              |
|-----------------------------|----------------------------|
| ![](presentation/ss/search.png)          | ![](presentation/ss/select_movie.png)  |

| 🎞️ Your Top Movies (List View) | 🧾 Edit Rating         |
|--------------------------------|------------------------|
| ![](presentation/ss/top_movies_list.png)    | ![](presentation/ss/edit.png)       |

---
## 🎥 Demo Video

Want to see it in action? This demo shows some of the features this site has:

📺 [Watch the demo on YouTube](https://www.youtube.com/watch?v=Ff19muasS8A)

### 🧪 Features demonstrated:
- 🧾 Creating an account
- 🔎 Searching for movies via TMDB API
- 🎞️ Adding movies from both *search* and *trending/Oscar* sections
- ✏️ Editing ratings and reviews
- 🗑️ Deleting movies from your top list
- 🧩 Sorting view: *list* vs. *grid*
- 🚪 Logging out
- 🔐 Testing restricted access when logged out (add/top page)

> 💡 *Click the link to open the video in full screen.*

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.x  
- `pip` or `venv`  
- TMDB API Key (get one [here](https://www.themoviedb.org/documentation/api))  
- Set the following **environment variables** in your IDE or deployment platform:

```bash
FLASK_SECRET_KEY=your-secret-key
TMDB_API_KEY=your-tmdb-key
```

> 💡 In local development, you can add these in your IDE's run configuration (e.g., PyCharm > Run/Debug Configurations > Environment Variables).


---

### 🛠 Installation

```bash
git clone https://github.com/RuginaAlex/my-top-movies.git
cd my-top-movies
pip install -r requirements.txt
python main.py
```

Visit `http://127.0.0.1:8081` in your browser.

---



## ⚙️ Tech Stack

| Tech        | Purpose                           |
|-------------|------------------------------------|
| Flask       | Backend web framework              |
| Flask-Login | User authentication                |
| SQLite      | Lightweight database               |
| Bootstrap 5 | Frontend styling                   |
| Jinja2      | HTML templates with logic          |
| TMDB API    | Fetching movie data                |
| Render      | Free cloud deployment              |
| UptimeRobot | Keep-alive pinging for free tier   |

---

## 🤝 Contributions

This project is a personal educational app built to showcase full-stack Python + Flask skills.

If you’d like to contribute, open a pull request or reach out via:

- 📧 [LinkedIn](https://www.linkedin.com/in/mircea-alexandru-rugin%C4%83-1b461b270/)
- 💻 [GitHub](https://github.com/RuginaAlex)

---

## 🔗 Credits

Movie data provided by [TMDB API](https://www.themoviedb.org/documentation/api)  
Icons by [Bootstrap Icons](https://icons.getbootstrap.com/)  
Project built by **Mircea-Alexandru Rugină**
