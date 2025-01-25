import requests
import json
import mysql.connector
from mysql.connector import Error

# Function to get weather data
def get_weather(city):
    api_key = 'e3a1d9d346914529bbe151920252301'  
    base_url = 'http://api.weatherapi.com/v1/forecast.json'  

    url = f"{base_url}?key={api_key}&q={city}&aqi=no&days={'1'}"
    
    try:
        
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json() 
            d = data['location']['localtime']
            l = data['location']['name']
            c = data['location']['country']
            t = data['current']['temp_c']
            h = data['current']['humidity']
            hi = data['current']['heatindex_c']
            p = data['current']['precip_mm']
            return [d,l,c,t,h,hi,p]
        else:
            print(f"Error {response.status_code}: Unable to fetch data.")
    except Exception as e:
        print(f"An error occurred: {e}")

def forecast(city,days):
    api_key = 'e3a1d9d346914529bbe151920252301'  
    base_url = 'http://api.weatherapi.com/v1/forecast.json'  

    url = f"{base_url}?key={api_key}&q={city}&aqi=no&days={str(days)}"

    try:
        
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json() 
            with open("weather_data.json", "w") as file:
                json.dump(data, file, indent=4)

            ans = []
            for i in range(days):
                l = data['location']['name']
                ct = data['location']['country']
                d = data['forecast']['forecastday'][i]['date']
                maxt = data['forecast']['forecastday'][i]['day']['maxtemp_c']
                mint = data['forecast']['forecastday'][i]['day']['mintemp_c']
                h = data['forecast']['forecastday'][i]['day']['avghumidity']
                c = data['forecast']['forecastday'][i]['day']['condition']['text']
                p = data['forecast']['forecastday'][i]['day']['totalprecip_mm']

                ans.append([l,ct,d,maxt,mint,h,c,p])

            return ans
        else:
            print(f"Error {response.status_code}: Unable to fetch data.")

    except Exception as e:
        print(f"An error occurred: {e}")

def crud(city,option):
    try:
        connection = mysql.connector.connect(
            host='localhost', 
            user='root',      
            password='shaurya',  
            database='project' 
        )

        if connection.is_connected():
            print("Connected to MySQL server")
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print("Connected to database:", record)

            if option==1:   #Create and add to table
                data = get_weather(city)
                print(data)
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS weather (
                    Id INT AUTO_INCREMENT PRIMARY KEY,
                    Local_time VARCHAR(255) NOT NULL,
                    Name VARCHAR(255) NOT NULL,
                    Country VARCHAR(255) NOT NULL,
                    Temperature FLOAT NOT NULL,
                    Humidity FLOAT NOT NULL,
                    Heat_Index FLOAT NOT NULL,
                    Precipitation FLOAT NOT NULL
                );
                """)
                insert_query = "INSERT INTO weather (local_time,name,country,temperature,humidity,heat_index,precipitation) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                data = tuple(data)
                cursor.execute(insert_query, data)
                connection.commit()
                print("Data inserted successfully.")

                return data
            
            elif option==2:
                cursor.execute("SELECT * FROM weather;")
                rows = cursor.fetchall()
                return rows
            
            elif option==3:
                query = "DELETE from weather;"
                cursor.execute(query)
                connection.commit()
                return 'All rows dropped'

            else:
                print('Wrong option')

    except Error as e:
        print("Error while connecting to MySQL:", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")


rows = crud('london',2)
print(rows)