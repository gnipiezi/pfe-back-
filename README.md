# boaa

## How to set up

1. Install dependencies via `pip install -r requirements` (use a virtual environment)
2. Run migrations using `python boaa/manage.py migrate`
3. Create a superuser account using `python boaa/manage.py createsuperuser`
4. Create fixtures for apartments `python boaa/manage.py create_fake_apartments 10 1` (check CLI if you want to know about more advanced parameters)
5. Create fixtures for recordings `python boaa/manage.py create_fake_sensor_readings 5 10` (check CLI if you want to know about more advanced parameters)
6. Serve up your project using `python boaa/manage.py runserver`
7. Enjoy the API at `http://localhost:8000`

## Use Docker to do the same

1. `docker-compose up`
2. `docker-compose exec django python /boaa/boaa/manage.py migrate`
3. `docker-compose exec django python /boaa/boaa/manage.py createsuperuser`
4. `docker-compose exec django python /boaa/boaa/manage.py create_fake_apartments 10 1`
5. `docker-compose exec django python /boaa/boaa/manage.py create_fake_sensor_readings 5 10`

Then you can browse your backend on `localhost:8000` and your frontend on `localhost:3010`

## Some documentation quirks

### Environment variables

- `CORS_ALLOWED_ORIGINS` (only preset in debug setting)
- `DEFAULT_LOGIN_PASSWORD` (`123supersecure` used when creating fixtures)

### Special endpoints

You can query `/sensor/reading/SENSORID` to get a list of readings for that sensor.
You can query `/sensor/reading/SENSOR1,SENSOR2,etc` to get a list of readings for all sensors specified.
They take two query string parameters: `?start_date` and `?end_date`

## To-DO

0. ~~Add `/sensor/reading` to the APIDoc somehow (I give up, DRF sucks on this)~~
1. Actually read data from Tecomon sensors
2. Create a production config as well
