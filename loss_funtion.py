import numpy as np
import matplotlib.pyplot as plt

# ============================================
# 1. FUNCIONES DE PÉRDIDA IMPLEMENTADAS
# ============================================

def mse_loss(y_true, y_pred):
    """Mean Squared Error - Para regresión"""
    return np.mean((y_true - y_pred) ** 2)

def mae_loss(y_true, y_pred):
    """Mean Absolute Error - Para regresión"""
    return np.mean(np.abs(y_true - y_pred))

def binary_crossentropy(y_true, y_pred):
    """Binary Cross-Entropy - Para clasificación binaria"""
    # Clip para evitar log(0)
    y_pred = np.clip(y_pred, 1e-7, 1 - 1e-7)
    return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

# ============================================
# 2. EJEMPLO PRÁCTICO: REGRESIÓN
# ============================================

print("=" * 50)
print("EJEMPLO 1: PREDICCIÓN DE PRECIOS DE CASAS")
print("=" * 50)

# Valores reales (en miles de dólares)
precios_reales = np.array([200, 250, 180, 300, 220])
print(f"Precios reales: {precios_reales}")

# Modelo malo
predicciones_malas = np.array([150, 280, 160, 250, 200])
print(f"Predicciones malas: {predicciones_malas}")
print(f"MSE (modelo malo): {mse_loss(precios_reales, predicciones_malas):.2f}")
print(f"MAE (modelo malo): {mae_loss(precios_reales, predicciones_malas):.2f}")

# Modelo bueno
predicciones_buenas = np.array([198, 252, 182, 298, 218])
print(f"\nPredicciones buenas: {predicciones_buenas}")
print(f"MSE (modelo bueno): {mse_loss(precios_reales, predicciones_buenas):.2f}")
print(f"MAE (modelo bueno): {mae_loss(precios_reales, predicciones_buenas):.2f}")

# ============================================
# 3. EJEMPLO PRÁCTICO: CLASIFICACIÓN
# ============================================

print("\n" + "=" * 50)
print("EJEMPLO 2: CLASIFICACIÓN DE SPAM")
print("=" * 50)

# 1 = spam, 0 = no spam
emails_reales = np.array([1, 0, 1, 1, 0])
print(f"Etiquetas reales: {emails_reales}")

# Probabilidades predichas
modelo_malo = np.array([0.4, 0.6, 0.3, 0.5, 0.7])
print(f"Predicciones malas: {modelo_malo}")
print(f"BCE (modelo malo): {binary_crossentropy(emails_reales, modelo_malo):.3f}")

modelo_bueno = np.array([0.95, 0.05, 0.92, 0.88, 0.08])
print(f"\nPredicciones buenas: {modelo_bueno}")
print(f"BCE (modelo bueno): {binary_crossentropy(emails_reales, modelo_bueno):.3f}")

# ============================================
# 4. VISUALIZACIÓN: EFECTO DEL ERROR
# ============================================

print("\n" + "=" * 50)
print("GENERANDO GRÁFICAS...")
print("=" * 50)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Gráfica 1: Comparación MSE vs MAE
errores = np.linspace(-10, 10, 100)
mse_values = errores ** 2
mae_values = np.abs(errores)

axes[0, 0].plot(errores, mse_values, label='MSE', linewidth=2)
axes[0, 0].plot(errores, mae_values, label='MAE', linewidth=2)
axes[0, 0].set_xlabel('Error (y_real - y_pred)')
axes[0, 0].set_ylabel('Pérdida')
axes[0, 0].set_title('MSE vs MAE: Sensibilidad al Error')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# Gráfica 2: Binary Cross-Entropy
y_pred_range = np.linspace(0.01, 0.99, 100)
bce_y1 = -np.log(y_pred_range)  # Cuando y_true = 1
bce_y0 = -np.log(1 - y_pred_range)  # Cuando y_true = 0

axes[0, 1].plot(y_pred_range, bce_y1, label='y_true = 1 (spam)', linewidth=2)
axes[0, 1].plot(y_pred_range, bce_y0, label='y_true = 0 (no spam)', linewidth=2)
axes[0, 1].set_xlabel('Predicción (probabilidad)')
axes[0, 1].set_ylabel('Pérdida')
axes[0, 1].set_title('Binary Cross-Entropy')
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3)

# Gráfica 3: Simulación de entrenamiento
epochs = 100
learning_rate = 0.01

# Simulación simple de descenso de gradiente
loss_history = []
weight = 5.0  # Peso inicial
target = 10.0  # Objetivo

for epoch in range(epochs):
    prediction = weight
    loss = (target - prediction) ** 2
    loss_history.append(loss)
    
    # Gradient descent
    gradient = -2 * (target - prediction)
    weight = weight - learning_rate * gradient

axes[1, 0].plot(loss_history, linewidth=2, color='red')
axes[1, 0].set_xlabel('Época')
axes[1, 0].set_ylabel('Pérdida (MSE)')
axes[1, 0].set_title('Entrenamiento: Reducción de Pérdida')
axes[1, 0].grid(True, alpha=0.3)

# Gráfica 4: Comparación final
x = ['Modelo Malo', 'Modelo Bueno']
mse_comparison = [
    mse_loss(precios_reales, predicciones_malas),
    mse_loss(precios_reales, predicciones_buenas)
]

axes[1, 1].bar(x, mse_comparison, color=['red', 'green'], alpha=0.7)
axes[1, 1].set_ylabel('MSE')
axes[1, 1].set_title('Comparación: Modelo Malo vs Bueno')
axes[1, 1].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('loss_functions_demo.png', dpi=300, bbox_inches='tight')
print("✅ Gráfica guardada como 'loss_functions_demo.png'")

plt.show()

# ============================================
# 5. RESUMEN CONCEPTUAL
# ============================================

print("\n" + "=" * 50)
print("RESUMEN")
print("=" * 50)
print("""
┌─────────────────────────────────────────────┐
│ FUNCIÓN DE PÉRDIDA                          │
├─────────────────────────────────────────────┤
│ ¿Qué es?                                    │
│ → Métrica que mide qué tan mal predice     │
│                                             │
│ ¿Para qué sirve?                            │
│ → Guiar el ajuste de pesos del modelo      │
│                                             │
│ Tipos principales:                          │
│ • MSE/MAE → Regresión                      │
│ • Cross-Entropy → Clasificación            │
│                                             │
│ Proceso:                                    │
│ 1. Predicción                              │
│ 2. Calcular pérdida                        │
│ 3. Backpropagation (calcular gradientes)   │
│ 4. Ajustar pesos                           │
│ 5. Repetir hasta convergencia              │
└─────────────────────────────────────────────┘
""")