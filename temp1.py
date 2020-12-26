# 导入库
import tensorflow as tf
import numpy as np
from tensorflow import keras
#定义和编译一个神经网络
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
# 编译 并指定 loss optimizer
model.compile(optimizer='sgd', loss='mean_squared_error')
#提供数据
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-2.0, 1.0, 4.0, 7.0, 10.0, 13.0], dtype=float)
#培训
model.fit(xs, ys, epochs=500)
#预测
print(model.predict([10.0]))