# FiorChat

FiorChat is a real-time chat application using Django and Tailwind. It features being able to sign up & log out, joining chat rooms, creating a chat room, and a hub showing the messages of all the rooms a user joined.

![](https://onedrive.live.com/?authkey=%21AAXhXaea5dJ5JVQ&cid=1436CA54A043A2DD&id=1436CA54A043A2DD%211788&parId=1436CA54A043A2DD%21202&o=OneUp)

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
