# Jobfind
### Job matcher application
The aim of this project is to design a web application that enables users to find as well as post jobs.It provides an easy and convenient search application for the job seekers to find their desired jobs and for the employers to find the right candidate. Job seekers can register with the application and update their details and skill set.Also, the employers can post details of any open job positions.The web application will then match job seekers with any current job openings based on their interest, skillset, experience etc.
<br/><br/>



### THE ENTITY RELATION DIAGRAM OF THE PROJECT 

<img src="https://github.com/adityachirania/jobfind/blob/master/image.png" height = 700 width = 700>

###   Requirements 
1.Python version >= 3.5
2.Django  version >= 2.2.9

### Running instructions <br>
1. Clone/download the repository <br>
2.Change directories into your project file .<br>
3. Set up a virtual environment with the steps mentioned in the blog : <br>  https://tutorial.djangogirls.org/en/django_installation/<br>
4.Run "python manage.py makemigrations jobfinder"<br>
5.Run "python manage.py migrate"<br>
6. All users on the site will not have admin access by default because they are clients. So to create a user with admin access run "python manage.py createsuperuser" and enter a username and password.<br>
7.Run it by "python manage.py runserver"<br>
8.Go to "localhost:PORT NO. " (Port no. is the port server runs on). This way you may experience the client portal . It has some things yet to complete which shall be added in the next version.<br>
9.Go to "localhost:PORT/admin" . This will lead you to the admin portal and is fully functional and does all CRUD operations and displays all records in a pleasent UI.You may login into this admin portal with superuser you have created.<br>

