# PyIMU_3Dvisualizer
IMU 3D visualizer with Python, OpenGL and MPU6050

Note: The "Yaw" mode is not implemented yet.

_Simulador 3D para acelerometro/gyroscopio MPU6050_
![](https://drive.google.com/uc?export=view&id=1g5SrGnZ_wfWsqmL7pKUehwe6HWRJV3sw)
## Comenzando 🚀

### Pre-requisitos 📋

* Python 3
* Tkinter
* pySerial
* pyOpenGL

* MPU6050
* Microcontroller
* USB-Serial Converter


## Wiki 📖

Puedes ver más acerca del proyecto en el video [demo](https://www.youtube.com/watch?v=vh91z3-3ncE)

Para comenzar es necesario contar con el microcontrolador encargado adquirir los datos del
MPU6050 y enviarlos de forma serial.

Aqui hay algunos ejemplos de como hacerlo utilizando:
* [Microcip PIC16F1709 MCU](https://github.com/MA-Lugo/PIC16F1709_MPU6050_ex)
* [STM32F1 MCU](https://github.com/MA-Lugo/STM32F1_MPU6050_lib/blob/main/Core/Src/main.c)

### Formato de la trama de datos:
En la siguiente imagen se muestra el formato de la trama de datos necesarios.

![](https://drive.google.com/uc?export=view&id=1YwkYYE5qgLod-2wsBejAZDGvy2fpD29x)

## Pruebas 🛠️

![](https://drive.google.com/uc?export=view&id=1FfHM9EbRliaT2iBzzAqZF8uXnvBeMvwJ)


## Autor ✒️

* **Mario A. Lugo**  [MA-Lugo](https://github.com/MA-Lugo)
