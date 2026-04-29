import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models

# 1. Configurações básicas
IMG_SIZE = (224, 224)
BATCH_SIZE = 32

# 2. Carregando as imagens automaticamente das pastas
datagen = ImageDataGenerator(rescale=1./255) # Normaliza as cores

train_data = datagen.flow_from_directory(
    'dataset_final/train',
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='binary'
)

val_data = datagen.flow_from_directory(
    'dataset_final/val',
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='binary'
)

# 3. Criando a estrutura da Rede Neural
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(1, activation='sigmoid') # Saída: 0 para uma classe, 1 para outra
])

model.compile(optimizer='adam', loss='binary_cross_entropy', metrics=['accuracy'])

# 4. Treinamento
print("\n--- Iniciando o Treinamento ---")
model.fit(train_data, validation_data=val_data, epochs=10)

# 5. Salvando o resultado
model.save('modelo_farmtech.h5')
print("\n✅ Treinamento concluído! Modelo salvo como 'modelo_farmtech.h5'")
