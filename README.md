# Connectly API

A Django REST Framework API for a social media platform. Built for MO-IT152 at Malayan Colleges Laguna.

**Team:** John Paul P., Kurosh Avendaño, Kristine Paul Garcia

## Overview

Connectly lets users create profiles, write posts, and leave comments. This is the Week 3 version where we switched to Class-Based Views and added proper validation through DRF serializers.

## What We Built

Three main models: Users, Posts, and Comments. Users can make posts, and anyone can comment on posts. Everything connects through foreign keys so posts link to their authors and comments link to both posts and users.

The API validates everything automatically now. If you try to create a post without content or link to a user that doesn't exist, it returns proper error messages.

## Running the Project

```bash
python -m venv venv
.\venv\Scripts\activate
pip install django djangorestframework
python manage.py migrate
python manage.py runserver
```

Server runs at http://127.0.0.1:8000/

## API Routes

**Users**
- GET /posts/users/ - list all users
- POST /posts/users/ - create user (username, email required)

**Posts**
- GET /posts/posts/ - list all posts
- POST /posts/posts/ - create post (content, author required)

**Comments**
- GET /posts/comments/ - list all comments
- POST /posts/comments/ - create comment (text, post, author required)

## Testing

Import `Week3_JohnPaulP_Results.postman_collection.json` into Postman. It has all the test requests including examples that work and ones that show validation errors.

## Tech Stack

Python 3.14, Django 6.0.1, Django REST Framework 3.16.1, SQLite

## Files

Main code is in the `posts` folder. Models are in models.py, validation in serializers.py, and the API views in views.py. Settings are in the `connectlyproject` folder.
