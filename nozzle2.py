import numpy as np
import plotly.graph_objs as go

# Function to generate data points on a cone
def generate_cone_data(num_points):
    theta = np.linspace(0, 2*np.pi, num_points)
    radius = np.linspace(1, 5, num_points)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    z = np.sqrt(x**2 + y**2)  # z = sqrt(x^2 + y^2)
    return np.column_stack((x, y, z))

# Function to add noise to data
def add_noise(data, noise_level):
    noise = np.random.normal(0, noise_level, data.shape[0])
    return data + noise[:, np.newaxis]

# Function to fit a cone to the data points
def fit_cone(data):
    # Assumed fitted cone parameters
    apex = np.array([0, 0, 0])
    direction = np.array([1, 1, 1])
    return apex, direction

# Function to plot cone and noisy data
def plot_cone_and_data(cone_data, noisy_data):
    cone_trace = go.Mesh3d(x=cone_data[:,0], y=cone_data[:,1], z=cone_data[:,2], color='lightblue', opacity=0.5)
    noisy_trace = go.Scatter3d(x=noisy_data[:,0], y=noisy_data[:,1], z=noisy_data[:,2], mode='markers', 
                                marker=dict(color='red', size=3), name='Noisy Data')
    fig = go.Figure(data=[cone_trace, noisy_trace])
    fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'), title='Best Fit Cone and Noisy Data')
    fig.show()

if __name__ == "__main__":
    num_points = 100
    cone_data = generate_cone_data(num_points)
    noise_level = 0.1
    noisy_data = add_noise(np.array(cone_data), noise_level)  # Convert cone_data to a NumPy array
    plot_cone_and_data(cone_data, noisy_data)
