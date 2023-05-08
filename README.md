# Meeting Manager Demo

## Description

This is an assignment project of Software Engineering developed by Yun-Zhong Qiu, Zhi-Bin Jian,Jian-Feng Wu, Zi-Tao Tang, and Di-Chu Wu.
The project is constructed and developed for technical identification and academic 
communication, which is non-profit. During the project development, we took advice from website blogs, experienced developers and outstanding technical documents, providing us a lot of help.

The content of project is about a meeting managing system, which provide simple functions of meeting online registration and scheduling. Such functions are very common on GitHub nowadays, our work is not original. To be honest, we just want to practice our coding capability on Web Apps.

Due to the limitation of ability and resource, the current project is certainly far from perfect. **We are looking forward for your advices!**

## Environment

### Hardware
Please use Windows version **upper-than Windows7**. Other platforms are not tested.

### Software

Please use **Python==3.7**, here is a installing tutorial for installing it:

https://www.cnblogs.com/telwanggs/p/10043142.html



Please use **MySQL==5.7**, here is a installing tutorial for installing it:

https://www.cnblogs.com/7q4w1e/p/9989129.html



Python package managing tools like **Anaconda3** is recommended!



## How to run this project

### Initialization

#### Database

After installing MySQL, use the commands below **in MySQL** to create database and authorize:

```mysql
CREATE DATABASE huiyi DEFAULT CHARACTER SET utf8 collate utf8_general_ci;
CREATE USER 'huiyi '@'%' IDENTIFIED BY '123456';
GRANT ALL PRIVILEGES ON huiyi.* TO 'huiyi '@'%' WITH GRANT OPTION;
ALTER USER 'huiyi '@'%' IDENTIFIED BY '123456' PASSWORD EXPIRE NEVER; 
ALTER USER 'huiyi '@'%' IDENTIFIED WITH mysql_native_password BY '123456';
FLUSH PRIVILEGES;
```

Then, open **Command Prompt** and use the commands below to sign in database and load data:

```sql
use huiyi
source huiyi.sql
```

In the project files, you can find a file named **settings.py**, in which we defined a structure **DATABASES** as a configure path of database. We use the following configuration to run locally on our machine:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'huiyi',
        'USER': 'huiyi',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'", 'charset': 'utf8', },
    }
}
```

Be careful to change the variables **‘NAME’**, **‘USER’**, **‘PASSWORD’** if you created different login data in the above steps. Also, if you have a robust server, you can modify variables **‘HOST’**,**‘’PORT’** to connect it.

#### Virtual Environment

Suppose you have successfully installed Anaconda3, **open Anaconda3 Prompt** and use the commands below to create a virtual environment and install needed packages in requirements.txt:

```makefile
conda create -n DjangoMK1 python=3.7
conda env list
conda activate DjangoMK1
pip  install -r  requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

Here we use the name **DjangoMK1** and pip source **TUNA**, feel free to choose your favorite choice.

#### Running!

As for this demo, we use our favorite python IDE: PyCharm. 

First, **Right Click** in project file and choose **Open in PyCharm**, like this:


![image-20230508154149847](README.assets/56w9ja-1683534959708-79.png)

Then, find the file named **manage.py** in project folder, like this:

![image-20230508154254927](README.assets/image-20230508154254927-1683531779593-5-1683534139230-33.png)

Click **Terminal**, and then choose **Command Prompt**, like this:

![image-20230508154450389](README.assets/image-20230508154450389-1683531894558-7-1683534141897-35.png)

Activate previously created virtual environment **DjangoMK1**, like this:

![image-20230508154639047](README.assets/image-20230508154639047-1683532002538-9-1683534143564-37.png)

Run command `python manage.py runserver` to run the whole project, like this:

![image-20230508154831130](README.assets/image-20230508154831130-1683532115417-11-1683534145501-39.png)

If you cannot get the above output, please double-check whether there is a configuration error, environment collision or software failure. Press **Ctrl** button and **Left Click** the blue URL, you should get the running program like this:

![image-20230508155103475](README.assets/image-20230508155103475-1683534147636-41.png)

Now, you have successfully build the whole project! Cheers! Here are some additional integrated commands in this program:

| COMMAND                            | DESCRIPTION                                                  |
| ---------------------------------- | ------------------------------------------------------------ |
| check <app_name>                   | check for problems in whole Django program                   |
| diffsettings                       | show difference between current configuration and default    |
| flush                              | delete all data from database                                |
| makemigrations                     | create a new migration based on the detected model           |
| migrate                            | synchronize the database state with the current model set and migration set |
| **runserver <server_address>**     | enable the lightweight development Web server that Django provides us |
| shell                              | launch the Python interactive interpreter with the Django environment |
| startapp <app_name>                | create a new application                                     |
| startproject <project_name>        | create a new project                                         |
| test [test_label [test_label ...]] | run the test code for all installed apps                     |

## How to use this project

In this project we define two kinds of users: **Common Users** and **Administrators**.

### Common Users

For **Common Users**, the available functions are listed below:

#### sign in

![image-20230508160350198](README.assets/image-20230508160350198-1683533032330-13-1683533035045-15-1683534151666-43.png)

#### log in

![image-20230508160401783](README.assets/image-20230508160401783-1683533043565-17-1683534154042-45.png)

#### get announcement information

![image-20230508160410487](README.assets/image-20230508160410487-1683533051959-19-1683534157175-47.png)

#### modify personal information

![image-20230508160420202](README.assets/image-20230508160420202-1683533061659-21-1683534159281-49.png)

#### get current meeting list and attend meetings

![image-20230508160428616](README.assets/image-20230508160428616-1683534161455-51.png)

#### search the meetings user attend or initiate

![image-20230508160437483](README.assets/image-20230508160437483-1683534163135-53.png)

#### initiate a meeting

![image-20230508160444346](README.assets/image-20230508160444346-1683534164612-55.png)

### Administrators

For **Administrators**, the available functions are listed below:

#### log in

![image-20230508160637852](README.assets/image-20230508160637852-1683533199462-23-1683534167229-57.png)

#### make an announcement

![image-20230508160646096](README.assets/image-20230508160646096-1683533207869-25-1683534169327-59.png)

#### manage meetings

![image-20230508160657454](README.assets/image-20230508160657454-1683534171210-61.png)

#### manage meeting rooms

![image-20230508160703419](README.assets/image-20230508160703419-1683534172825-63.png)

#### manage users

![image-20230508160710092](README.assets/image-20230508160710092-1683534174583-65.png)

## Further Information

For additional development information, please read the docs and PPT in project file.

Here, we demonstrate some of the designing process of this project:

### Database Interaction

![image-20230508161114014](README.assets/image-20230508161114014-1683534176881-67.png)

### System Environment Diagram

![image-20230508161158145](README.assets/image-20230508161158145-1683534178447-69.png)

### Level 1 Data Flow Diagram

![image-20230508161233263](README.assets/image-20230508161233263-1683534180951-71.png)

### Entity-Relationship Diagram

![image-20230508161304652](README.assets/image-20230508161304652-1683534182870-73.png)

### Module Structure Diagram

![image-20230508161335171](README.assets/image-20230508161335171-1683533618411-27-1683534185150-75.png)
