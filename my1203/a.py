from from_sensor_code import MyClassifier

gildong = MyClassifier()

gildong.read('pandas_simple.csv')
#gildong.heatmap()
gildong.run_all(['Humidity', 'Temperature', 'Pressure'], 'class', 5)
gildong.draw_4_accuracy()