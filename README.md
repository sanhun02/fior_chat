# FiorChat

FiorChat is a real-time chat application using Django and Tailwind. It features being able to sign up & log out, joining chat rooms, creating a chat room, and a hub showing the messages of all the rooms a user joined.

![fior_chat](https://user-images.githubusercontent.com/113066180/220245788-545f7271-0e98-41bb-9d85-65789ce3741c.gif)

## Setup

First clone the repository:

```bash
$ git clone https://github.com/sanhun02/fior_chat.git
$ cd fior_chat
```

Install project dependencies:

```bash
$ pip install -r requirements.txt
```

Create database tables and a superuser account:

```bash
$ py manage.py migrate
$ py manage.py createsuperuser
```

Now you are able to run the development server:

```bash
$ py manage.py runserver
```
