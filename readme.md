# Sensores

En la siguiente tabla se muestran los sensores del dispositivo, junto a sus protocolos
y pines utilizados, como asi tambien el intervalo de tiempo en que deberían realizar la medicion

| Sensor  | Variables     | Tipo    | Pines   | Voltaje | t muestreo |
| ------- | ------------- | ------- | ------- | ------- | ---------- |
| MQ7     | CO            | Analog  | ADS115  | 5V      |            |
| GP2Y10  | Polvo 2.5     | Analog  | ADS115  | 5V      |            |
| ML8511  | Rad UV        | Digital | ADS115  | 5V      |            |
| BH1750  | Luminosidad   | Digital | I2C     | 3V3     |            |
| ccs811  | CO2, VOC      | Digital | I2C     | 3V3     |            |
| ds18b20 | Temp Exterior | Digital | 4       | 3V3     |            |
| ds18b20 | Temp Interior | Digital | 33      | 3V3     |            |
| INMP441 | Ruido         | Digital | WS: 5   | 3V3     |            |
|         |               |         | SCK: 18 |         |            |
|         |               |         | SD: 19  |         |            |
| BME280  | T,H,P         | Dig     | I2C     | 3V3     |            |
| MPU6050 | vibraciones   | Dig     | I2C     | 3V3     |            |
| divisor | voltaje bat   | Analog  | 36      | -       |            |

**Perifericos**

- Microcontrolador ESP32

  | Perifericos | Tipo    | Pines    | Voltaje |
  | ----------- | ------- | -------- | ------- |
  | cooler bajo | Digital | 2        | 5V      |
  | cooler alto | Digital | 13       | 5V      |
  | mux ADS115  | Digital | I2C      | 5V      |
  | oled 128x64 | Digital | I2C      | 3V3     |
  | RTC DS3231  | Digital | I2C      | 3V3     |
  | Buzzer      | Digital | 12       | 3V3     |
  | Neopixel    | Digital | 26       | 3V3     |
  | Pulsador    | Digital | 0        | 3V3     |
  | SIM808      | Digital | rx2: 16  | 4V2     |
  |             |         | tx2: 17  |         |
  |             |         | pKey: 32 |         |
  |             |         | stat: 39 |         |

**Software**

- Basado en RTOS
- Actualización OTA
- Blynk

# Blynk (no editado, esto es de CO2)

En la aplicacion de blynk se enviaran los datos como se muestra en la tabla.

| Pines virtuales | Datos                          | Tipo   | Origen | Envio      |
| --------------- | ------------------------------ | ------ | ------ | ---------- |
| V2              | Calibracion a 400ppm           | Evento | Blynk  | User       |
| V4              | Alarma On/Off                  | Dato   | Blynk  | User       |
| V5              | Alarma State                   | Dato   | Sensor | On Change  |
| V6              | Medición CO2 ppm               | Dato   | Sensor | Periodic   |
| V7              | Tiempo de muestra              | Dato   | Blynk  | User       |
| V8              | LED On/Off                     | Dato   | Blynk  | User       |
| V9              | LED state                      | Dato   | Sensor | On change  |
| V10             | Umbral verde/amarillo          | Dato   | Blynk  | User       |
| V11             | Umbral amarillo/rojo           | Dato   | Blynk  | User       |
| v12             | Umbral default                 | Evento | Blynk  | User       |
| v13             | Etiqueta Area                  | Evento | Blynk  | User       |
| V20             | Instensidad WiFi 0-100%        | Dato   | Sensor | Periodic   |
| V21             | Version de Firmware Actual     | Dato   | Sensor | On connect |
| V22             | Chip ID                        | Dato   | Sensor | On connect |
| V23             | Product ID                     | Dato   | Sensor | On connect |
| V24             | SSID red conectada             | Dato   | Sensor | On connect |
| V27             | Status                         | Evento | Blynk  | On change  |
| V28             | Version de Firmware disponible | Dato   | Sensor | On connect |
| V29             | Actualizar Firmware            | Evento | Blynk  | User       |
| V30             | Ubidots ON/OFF                 | Dato   | Sensor | On change  |
| V33             | Ubidots Token                  | Dato   | Sensor | On change  |
| V40             | Thingspeak ON/OFF              | Evento | Blynk  | On change  |
| V41             | Thingspeak API                 | Dato   | Blynk  | On change  |
| V50             | HTTP API ON/OFF                | Dato   | Blynk  | On change  |
| V51             | HTTP API URI                   | Dato   | Blynk  | On change  |
| V60             | MQTT ON/OFF                    | Dato   | Blynk  | On change  |
| V61             | MQTT Broker                    | Dato   | Blynk  | On change  |
| V62             | MQTT PORT                      | Dato   | Blynk  | On change  |
| V63             | MQTT TOPIC                     | Dato   | Blynk  | On change  |

# Archivos

## config.h(no editado, esto es de CO2)

En este archivo se ubican todas las configuraciones del dispositivo, y estructuras de datos para la manipulación de parámetros de configuración, las funciones loadConfig y saveConfig, recuperan y guardan los parámetros de configuración en la memoria SPIFFS del ESP32.

Se declaran dos tipos de datos `cmd_control_t` y `data_t`, estos datos son la base de informacion del dispositivo.

Funciones públicas de config.h

```c++
 int  loadConfig();
```

Carga las configuraciones desde la memoria SPIFFS.

```c++
int saveConfig();
```

Guarga las configuraciones en la memoria SPIFFS.

```c++
int sizeOfDataArray();
```

Retorna la cantidad de elementos data_t reqistrados.

```c++
Conexion_WiFi_s getWifiConfig();
void putWifiConfig(Conexion_WiFi_s inCommingData);
```

Obtiene o guarda las configuraciones del WiFi.

## blink_interfaz.h (no editado, esto es de CO2)

En este archivo se desarrolla toda la interaccion con blynk, se lo instancia en una tarea en RTOS, los mensajes o parametros a transmitir se los envia por una cola.

Funciones públicas de blynk_interfaz.h

```c++
 void blynk_launch();
```

Crea las Queues para la recepcion de datos a la tarea, crea la tarea y la asocia al APP_CORE.

```c++
void sendToBlynk(blynk_data_t *msg);
```

Envia el dato a la Queue de la tarea de Blynk.

```c++
void setBlynkDataMsg(blynk_data_t *msg,
                     int pin,
                     int value,
                     char *value_str = NULL,
                     char *property = NULL ,
                     char *value_prop = NULL);
```

Carga los datos en el buffer a ser enviado a la tarea de blynk.

## logica_control.h (no editado, esto es de CO2)

En este archivo se escribe toda la logica de control, se interpretan los comandos que vienen de Blynk o de cualquier otra plataforma que se pueda programar.

Funciones públicas de logica_control.h

```c++
void control_launch();
```

Crea las Queues para la recepcion de datos a la tarea, crea la tarea y la asocia al APP_CORE.

```c++
void sendToControl(data_t *msg);
```

Envia el dato a la Queue de la tarea de control.

## sensor_task.h (no editado, esto es de CO2)

En esta tarea se toma los datos del sensor y se configuran los datos para enviar a las tareas del LED, buzzer y Blynk a travez de sus respectivas Queues.

Esta tarea recibe datos a travez de su propia Queue donde puede recibir comandos para almacenar parametros y configurar el sensor.

Se definen dos tipos de datos `sensor_cmd_t` y `sensor_config_t`.

Funciones públicas de sensor_task.h

```c++
void sensores_launch();
```

Crea la Queue para el envio de datos y crea la tarea en el APP_CORE.

```c++
void sendToSensores(sensor_config_t *msg);
```

Envia el dato a la Queue de la tarea del sensor.

## wifi_conection.h (no editado, esto es de CO2)

En este archivo se escriben las funciones para la gestion de la conexion WiFi, ofreciendo dos opciones, la primera de conexion a travez de WiFiManager y la segunda a travez de conexion directa si ya estan guardadas las credenciales WiFi.

Funciones públicas de wifi_conection.h

```c++
bool detectSavedSSID(String ssid_obj);
```

Funcion para detectar si esta disponible la red WiFi preconfigurada. Retorna `true` si se encuentra la red pasada por parametro.

```c++
void wifi_manager_launch();
```

Ejecuta la rutina de WiFiManager, posee un timeout de 180 segunsdos, de manera que no es bloqueante.

```c++
void wifi_launch();
```

Ejecuta la rutina para conectarse a la red WiFi preconfigurada o guardada previamente.

## ota.h (no editado, esto es de CO2)

En este archivo se escribe la rutina utilizada para la actualizacion de firmware a traves de HTTP OTA.

Funciones públicas de ota.h

```c++
void update_software(String download_path);
```

Ejecuta la peticion HTTP a la direccion pasada por parametro.

## led_task.h (no editado, esto es de CO2)

En este archivo se encapsula la gestion del led RGB WS2812b, se crean dos tipos de datos, `color_t` y `led_t`.

Funciones públicas de led_task.h

```c++
void led_launch();
```

Crea la Queue para el envio de datos y crea la tarea en el APP_CORE.

```c++
void sendToLed(led_t *msg);
```

Envia el dato a la Queue de la tarea del led.

## buzzer_task.h (no editado, esto es de CO2)

En esta funcion se encapsula el uso del buzzer, se declaran un tipo de dato `buzzer_t`.

Funciones públicas de buzzer_task.h

```c++
void buzzer_launch();
```

Crea la Queue para el envio de datos y crea la tarea en el APP_CORE.

```c++
void sendToBuzzer(buzzer_t *msg);
```

Envia el dato a la Queue de la tarea del buzzer.
