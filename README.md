<h1 align="center">
  Road View
</h1>

<h5 align="center">
	Finding routes from satellite images
</h5>

<p align="center">
	<strong>
		<a href="https://drive.google.com/file/d/1A2OZsPJdHoHygQeAqDwPBMyf1xojDAg8/view?usp=sharing">Demo Video</a>
		•
		<a href="http://52.140.73.56">Website</a>
	</strong>
</p>

### About
---------
A machine learning solution to extract road from satellite images. In disaster zones, especially in developing countries, maps and accessibility information are crucial for crisis response. This project overcomes the challenge of automatically extracting roads and street networks from satellite images.

The project uses a UNET model, achieving an accuracy of 97% and is hosted on MS Asure.

<p align="center">
	<img src = "https://user-images.githubusercontent.com/35189722/119429631-d1bd8000-bd2c-11eb-96e2-3493b49f0c88.png" align = "center" width = "60%"/>
</p>

### Dataset used
----------------

This dataset was obtained from [Road Extraction Challenge Track](https://competitions.codalab.org/competitions/18467) in [DeepGlobe Challenge](http://deepglobe.org/challenge.html). For more details on the dataset refer the related publication - [DeepGlobe 2018: A Challenge to Parse the Earth through Satellite Images](https://arxiv.org/abs/1805.06561)

### TechStack
-------------

<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/> <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=TensorFlow&logoColor=white"/> 
<img src="https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=Keras&logoColor=white"/> <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white"/>
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"/> <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/>
<img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white"/>

### Features
------------
- Find routes from satellite images
- History of each user
- Login/ Signup


### To get the code
-------------------
Clone the repository

    $ git clone https://github.com/ManasUniyal/RoadView.git

If this is your first time using Github, review https://help.github.com to learn the basics.

### To run the application locally
----------------------------------
1. Clone the project to your system
2. Create a virtual environment
3. Install all the requirements

        $ pip install -r requirements.txt 
        
4. Make migrations
        
        $ python manage.py makemigrations
        $ python manage.py migrate
        
5. Run the project

        $ python manage.py runserver
        
6. Access the deployed web application at: http://localhost:8000/

### Contributors
----------------
- [Manas Uniyal](https://www.github.com/ManasUniyal)
- [Rajat Kumar](https://github.com/991rajat)

### License
-----------
The MIT License 2021.

### Note
--------
Feel free to contribute to the repo by making a PR or raising an issue <br>
Do give a ⭐ if you like the project
