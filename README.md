<h1 align="center">🗳️ Poll Application 🗳️</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-v0.1-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/Miralhas/poll-app" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
</p>

> This project is a polling application developed using Django. It is designed to allow users to authenticate themselves, create polls and vote.

### 🏠 [Homepage](https://github.com/Miralhas/poll-app)

![image](https://github.com/Miralhas/django-polls/assets/89564433/5148d7cd-b8dc-454f-a3dc-c7ec264485dd)

## Features
 - User Authentication
	 - The project provides a user authentication feature, which allows users to register and login to the application. The user authentication ensures that only authenticated users can create polls.
	  <br>
 - Poll Creation 
	 - Authenticated users can create polls. The number of options for a poll is dynamic and determined by the user. The poll and its options are stored using Django's ORM system.
	<br>
- Poll Voting and Display
	- All polls are displayed on the index page. Users can cast their votes on a poll. The vote count for each option in a poll is updated when a vote is cast. The polls and their options are retrieved using Django's ORM system.
![image](https://github.com/Miralhas/django-polls/assets/89564433/0fde03ee-c6b3-488a-ab14-69f3691a88f0)
- Poll Management
	- The owner of a poll can end or delete it. If a poll is ended, it is updated to reflect its ended status. If a poll is deleted, it is removed from the database.

## Installation Steps
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the following command to start the Django development server:
	-  `python manage.py runserver`
4. Visit http://127.0.0.1:8000/ in your web browser to access the application.
## Author

👤 **Victor Miralhas**

- Github: **[@Miralhas](https://github.com/Miralhas)**


## 📝 License

Copyright © 2023 **[Victor Miralhas](https://github.com/Miralhas)**.<br />

