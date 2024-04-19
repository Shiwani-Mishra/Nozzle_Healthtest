import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class SensorSimulator:
    def __init__(self, num_samples, min_voltage, max_voltage, noise_level):
        self.num_samples = num_samples
        self.min_voltage = min_voltage
        self.max_voltage = max_voltage
        self.noise_level = noise_level

    def generate_data(self):
        voltages = np.random.uniform(self.min_voltage, self.max_voltage, self.num_samples)
        noise = np.random.normal(0, self.noise_level, self.num_samples)
        return voltages + noise

class SensorAnalyzer:
    def analyze_data(self, data, min_voltage, max_voltage):
        mean = np.mean(data)
        std_dev = np.std(data)
        data_range = np.max(data) - np.min(data)
        # Simulated logic to identify faulty nozzles
        faulty_nozzles = [i for i, voltage in enumerate(data) if voltage < 0.5 * (min_voltage + max_voltage)]
        return mean, std_dev, data_range, faulty_nozzles

class GUI:
    def __init__(self, root, sensor_simulator, sensor_analyzer):
        self.root = root
        self.root.title("Nozzle Health Monitor")

        self.sensor_simulator = sensor_simulator
        self.sensor_analyzer = sensor_analyzer

        self.plot_frame = tk.Frame(self.root)
        self.plot_frame.pack()

        self.plot_button = tk.Button(self.plot_frame, text="Generate Data", command=self.update_plot)
        self.plot_button.pack()

        self.plot_canvas = plt.figure(figsize=(6, 4))
        self.plot_canvas = plt_canvas = FigureCanvasTkAgg(self.plot_canvas, master=self.plot_frame)
        self.plot_canvas.get_tk_widget().pack()

        self.analysis_frame = tk.Frame(self.root)
        self.analysis_frame.pack()

        self.mean_label = tk.Label(self.analysis_frame, text="Mean: ")
        self.mean_label.pack()

        self.std_dev_label = tk.Label(self.analysis_frame, text="Standard Deviation: ")
        self.std_dev_label.pack()

        self.range_label = tk.Label(self.analysis_frame, text="Range: ")
        self.range_label.pack()

        self.faulty_label = tk.Label(self.analysis_frame, text="Faulty Nozzles: ")
        self.faulty_label.pack()

    def update_plot(self):
        data = self.sensor_simulator.generate_data()
        mean, std_dev, data_range, faulty_nozzles = self.sensor_analyzer.analyze_data(data,
                                                                                        self.sensor_simulator.min_voltage,
                                                                                        self.sensor_simulator.max_voltage)

        plt.clf()
        plt.plot(data)
        plt.xlabel("Sample")
        plt.ylabel("Voltage")
        plt.title("Sensor Data")
        self.plot_canvas.draw()

        self.mean_label.config(text="Mean: {:.2f}".format(mean))
        self.std_dev_label.config(text="Standard Deviation: {:.2f}".format(std_dev))
        self.range_label.config(text="Range: {:.2f}".format(data_range))
        self.faulty_label.config(text="Faulty Nozzles: {}".format(faulty_nozzles))

if __name__ == "__main__":
    root = tk.Tk()
    sensor_simulator = SensorSimulator(num_samples=100, min_voltage=0, max_voltage=5, noise_level=0.1)
    sensor_analyzer = SensorAnalyzer()
    app = GUI(root, sensor_simulator, sensor_analyzer)
    root.mainloop()
