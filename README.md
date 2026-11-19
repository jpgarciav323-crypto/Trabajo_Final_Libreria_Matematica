# Trabajo Final: Librería Matemática en Python

**Materia:**  Informática 1  
**Docente:** Joaquín Sánchez  
**Estudiante:** Juan Pablo García  

---

## 1. Descripción e Instrucciones de Ejecución

Este proyecto implementa una librería matemática propia (`libreria_matematica.py`) desarrollada en Python sin utilizar el módulo estándar `math` para los cálculos principales, junto con un archivo de verificación (`pruebas.py`) que valida cada función y calcula su error absoluto frente a `math`.

### Cómo ejecutar el proyecto
1. Asegúrese de tener ambos archivos (`libreria_matematica.py` y `pruebas.py`) en la misma carpeta.
2. Abra una terminal en dicha carpeta y ejecute el archivo de pruebas:
   ```bash
   python pruebas.py
   ---

## 2. Métodos Utilizados, Intervalos y Tolerancias

* **Exponencial ($e^x$) y constante $e$:** Aproximados mediante la serie de Taylor $\sum_{k=0}^{N-1} \frac{x^k}{k!}$ utilizando $30$ términos ($35$ términos internos dentro de Newton-Raphson), logrando un error de $0.00 \times 10^0$ en $e^1 \approx 2.71828183$ y $1.78 \times 10^{-15}$ en $e^2$.
* **Constante $\pi$:** Aproximada con la serie de Nilakantha $3 + 4 \sum_{k=1}^{N} \frac{(-1)^{k+1}}{(2k)(2k+1)(2k+2)}$ usando $1000$ términos, obteniendo $3.14159265$ (error absoluto de $2.50 \times 10^{-10}$).
* **Funciones Trigonométricas ($\sin(x)$, $\cos(x)$, $\tan(x)$):** Para mejorar la precisión con ángulos grandes o armónicos altos, los argumentos en radianes se reducen primero al intervalo $[-\pi, \pi]$. Seno y coseno se calculan mediante sus series de Taylor con $15$ términos (error de $0.00 \times 10^0$ en $\sin(\pi/6) = 0.5$ y $\cos(0) = 1.0$). La tangente se calcula como $\sin(x)/\cos(x)$, validando una tolerancia de $|\cos(x)| < 10^{-6}$ para reportar indefinitud en puntos como $\pi/2$.
* **Logaritmo Natural ($\ln(x)$):** Implementado mediante el método iterativo de Newton-Raphson para resolver $e^y - x = 0$ partiendo de $y_0 = 0$. Se utilizó una tolerancia de $|e^{y_n} - x| < 10^{-7}$ y un máximo de $100$ iteraciones. Se verificó su funcionamiento en el intervalo $[0.5, 2.0]$ (logrando error de $0.00 \times 10^0$ en $\ln(1)$ y $\ln(2)$) y se rechazaron entradas $x \le 0$ ($\ln(0)$ y $\ln(-5)$).
* **Máximo Común Divisor ($\text{mcd}$):** Implementado con el algoritmo de Euclides usando el operador módulo (`%`). Garantiza resultados no negativos con enteros negativos ($\text{mcd}(-15, 0) = 15$, $\text{mcd}(-24, -36) = 12$) y retorna $0$ para $(0, 0)$.

---

## 3. Comparación de Sumas Parciales de Fourier (Onda Cuadrada)

Se evaluó la aproximación de una onda cuadrada de amplitud $1$ y periodo $2\pi$ mediante $S_N(x) = \frac{4}{\pi} \sum_{k=0}^{N-1} \frac{\sin((2k+1)x)}{2k+1}$ para $N = 1, 5, 15$ términos impares:

| Punto evaluado ($x$) | Valor ideal | $N = 1$ ($S_1(x)$ / Error) | $N = 5$ ($S_5(x)$ / Error) | $N = 15$ ($S_{15}(x)$ / Error) |
| :--- | :---: | :---: | :---: | :---: |
| **$x = \pi/2$** | $1.0$ | $1.273240$ (Err: $0.273240$) | $1.063467$ (Err: $0.063467$) | $1.021232$ (Err: $0.021232$) |
| **$x = 3\pi/2$** | $-1.0$ | $-1.273240$ (Err: $0.273240$) | $-1.063467$ (Err: $0.063467$) | $-1.021232$ (Err: $0.021232$) |
| **$x = 0.1$** | $1.0$ | $0.127112$ (Err: $0.872888$) | $0.601865$ (Err: $0.398135$) | $1.177965$ (Err: $0.177965$) |

### Análisis de la convergencia
Al aumentar el número de términos $N$ de $1$ a $15$, la aproximación se acerca cada vez más al valor ideal de la onda cuadrada ($1.0$ o $-1.0$) y el error disminuye progresivamente:
* En los centros de cada semiciclo ($x = \pi/2$ y $x = 3\pi/2$), el error baja de $0.2732$ con $N=1$ a apenas $0.0212$ con $N=15$.
* Cerca de la discontinuidad en $x = 0.1$, con $N=1$ la onda apenas sube a $0.1271$ (error de $0.8729$), mientras que con $N=15$ alcanza $1.1780$ (error de $0.1780$), mostrando el sobrepico característico cercano al salto brusco (fenómeno de Gibbs) antes de estabilizarse en $1.0$.---

