# StarshipWeb
**A website for the future** <br>
This is an inspiring website with the goal of giving latest news about SpaceX's Starship rocket to rocket nerds. <br>
### About websites:
There is a website for the user page, where the user can get the latest news about Starship or contact the website admin. <br>
**Link to the user website: https://starshipweb.onrender.com** <br>
There is also a website for the admin. The admin can use that panel to see who wants to contact them. <br> 
**Link to the admin website:[ https://starshipweb.onrender.com](https://starshipweb-admin-panel.onrender.com)**

# User Website
### HomePage:
The homepage is were it inspires everyone! It contains a beautiful video of Super Heavy catch in the background. ![Screenshot 2025-01-14 at 9 30 03 AM](https://github.com/user-attachments/assets/d34175dd-409e-4c5a-9825-5b695cd4622f)

### SideBar:
In the sidebar, there are 4 different buttons, and each button takes you to a separate page. 
![Screenshot 2025-01-14 at 9 30 58 AM](https://github.com/user-attachments/assets/caaf1a0f-97f6-44af-9ac2-d9d570f087af)

### Page 1: Latest News 
In this page, the usser can find the latest news about Starship. 
![Screenshot 2025-01-14 at 9 33 27 AM](https://github.com/user-attachments/assets/b24ce8ff-311e-43a7-b28c-f8b565e5cecf)
*The image used in the background of this page is from SpaceX*

### Page 2 Multi-Cam:
In this page, the user can see multiple live camera feeds (from YouTube) of Starbase texas. 
![Screenshot 2025-01-14 at 9 55 04 AM](https://github.com/user-attachments/assets/98081ef6-1cf2-49c5-9542-13ccb16eb772)

### Page 3: Road Closures 
In this page, the user can see the schedule for road closures (HW4 at Starbase). The closures are loaded from a databse (`closures.db` file).
![Screenshot 2025-01-14 at 9 34 45 AM](https://github.com/user-attachments/assets/3020cc5f-e2ed-4c96-a096-f8e3c15c2020)

### Page 4: Contact Us
In this page the user can contact the website's admin. The user can enter their name, email and their message. These infos (name, email and message) will be dumped into a databse (`contact.db` file).
![Screenshot 2025-01-14 at 9 40 29 AM](https://github.com/user-attachments/assets/325e02f0-4962-4410-abae-5367d0a775d8)

# Admin Website:
This website has only one page, showing the messages (including their Email and Name) sent by the user. The datas are being loaded from `contact.db` databse file. This page gets updated anytime the a new user sends a new message (with Email and Name)
![Screenshot 2025-01-14 at 9 57 33 AM](https://github.com/user-attachments/assets/2300b703-f36b-41a5-b799-342a1c499ec1)
