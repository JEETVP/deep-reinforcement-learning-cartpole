# Deep Reinforcement Learning con DQN en CartPole-v1

Implementación de deep reinforcement learning con DQN, para resolver el entorno Cartpole-V1 de Gymnasium, utilizando pytorch para la construcción y entrenamiento de la red neuronal y gymnasium para el entorno de aprendizaje por refuerzo

---

## Entorno: CartPole-v1

El entorno proporciona un vector de estado con 4 valores:

1. Posición del carrito.
2. Velocidad del carrito.
3. Ángulo del poste.
4. Velocidad angular del poste.

El agente puede realizar 2 acciones:

- `0`: mover el carrito hacia la izquierda.
- `1`: mover el carrito hacia la derecha.

El objetivo es mantener el poste equilibrado durante el mayor número posible de pasos.

---

## Arquitectura del modelo

La red neuronal utilizada tiene la siguiente estructura:


Entrada: 4 variables
        ↓
Capa totalmente conectada: 128 neuronas
        ↓
ReLU
        ↓
Capa totalmente conectada: 128 neuronas
        ↓
ReLU
        ↓
Salida: 2 Q-values

Y cada salida representa el valor estimado de realizar una acción en el estado actual

---

# Funcionamiento de DQN

El agente utiliza los siguientes elementos:

Policy Network: Red neuronal principal que aprende los valores Q de cada acción.

Target Network: Copia de la red utilizada para calcular los objetivos más estables durante el entrenamiento.

Experience Replay: Experiencias del agente almacenadas en el replay buffer.

Epsilon-Greedy: Utiliza estrategia de exploración y explotación

---

# Ecuación de Bellman

El valor objetivo se calcula utilizando la ecuación:

Q objetivo = recompensa + gamma * máximo Q del siguiente estado

Donde:

reward: recompensa obtenida.
gamma: factor de descuento.
Q(s', a'): valor estimado de las acciones futuras.

En esta implementación se utiliza:

gamma = 0.99

# Función de perdida

La función compara el Q-value predicho por la red con el Q-value objetivo calculado mediante la ecuación de Bellman.

# Hiperparametros Principales

Batch size:      64
Gamma:           0.99
Learning rate:   0.001

Epsilon inicial: 1.0
Epsilon final:   0.05
Epsilon decay:   500

Episodios:       300

# Resultados
Los resultados fueron:

Reward promedio:       125.5
Mejor episodio:        132
Peor episodio:         116
Desviación estándar:   3.76

Estos resultados muestran que el agente aprendió una política consistente para controlar el entorno, aunque el entrenamiento presentó variaciones en el desempeño.

# Estructura del Proyecto

deep-reinforcement-learning-cartpole/
│
├── dqn_cartpole.ipynb
├── dqn_cartpole.pth
├── README.md
├── requirements.txt
├── .gitignore
│
└── results/
    ├── reward_training.png
    ├── reward_moving_average.png
    ├── loss_training.png
    ├── evaluation_metrics.json
    └── test_rewards.csv

# Instalación

1. Crear entorno virtual
2. Instalar dependencias
3. Ejecución

# Limitaciones

El entrenamiento de DQN puede ser inestable.
El rendimiento puede variar entre ejecuciones.
El agente necesita múltiples interacciones con el entorno para aprender.
Una arquitectura más compleja puede requerir mayor tiempo de entrenamiento y recursos computacionales.
El modelo funciona específicamente con el espacio de estados y acciones de CartPole-v1.

# Tecnologías utilizadas

Python
PyTorch
Gymnasium
NumPy
Matplotlib
Jupyter Notebook
