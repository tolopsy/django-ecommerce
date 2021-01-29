# AN E-COMMERCE DJANGO PROJECT. 

This is an e-commerce django project with all the fundamental features of an online store. I named it Oloja

The templates used in the frontend is designed by https://boostrapious.com. 

The templates are great for learning how to build an e-commerce website.

## Follow the following steps to run this in your local machine

```json
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python manage.py runserver
```
## Follow the following steps to run the asynchronous task manager (Celery + RabbitMQ)

1. Install RabbitMQ on Linux by executing the command below from the shell
   ```json
   apt-get install rabbitmq
   ```
   
   If you're using macOS or Windows, click [here](https://www.rabbitmq.com/download.html) to download the standalone version of RabbitMQ.

2. After installing, RabbitMQ, execute the following commmand to launch RabbitMQ
   ```json
   rabbitmq-server
   ```

3. Open a new shell, change directory to your project  directory and start your 
   celery worker with the  following command
   ```json
   celery -A myshop worker -l info
   ```
   Note that celery has been installed when you ran 'pip install -r requirements.txt'

4. To monitor asynchronous tasks with Flower - a web application for monitoring 
   celery. Open a new shell and run the following command from your project directory.

   ```json
   celery -A myshop flower
   ```

##  Technologies used
1. Weasyprint - To create pdf receipt for orders. Find implementation in 
   views.py of orders app (line 44 - 52).

2. Celery - To handle asynchronous tasks - Example: sending order mails 
   to customers. Find implementation in celery.py of ecommmerce folder, tasks.py of orders app and line 28 of views.py

3. RabbitMQ - Used as message broker for celery

4. Flower -  Used to monitor Celery
