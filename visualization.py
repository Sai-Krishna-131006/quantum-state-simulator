import matplotlib.pyplot as plt
import numpy as np

def plot_probabilities(p0, p1):
    states = ['|0>', '|1>']
    probs = [p0, p1]

    plt.bar(states, probs)
    plt.ylim(0,1)
    plt.title("Measurement Probabilities")
    plt.ylabel("Probability")
    plt.show()


def plot_bloch(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.quiver(0,0,0,x,y,z,color='blue')

    ax.set_xlim([-1,1])
    ax.set_ylim([-1,1])
    ax.set_zlim([-1,1])

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    u = np.linspace(0, 2*np.pi, 50)
    v = np.linspace(0, np.pi, 50)

    x_s = np.outer(np.cos(u), np.sin(v))
    y_s = np.outer(np.sin(u), np.sin(v))
    z_s = np.outer(np.ones(np.size(u)), np.cos(v))

    ax.plot_wireframe(x_s, y_s, z_s, color='lightgray', alpha=0.3)

    ax.set_title("Bloch Vector Representation")
    plt.grid(True)
    plt.show()

def plot_experiment(c0, c1):

    states = ['|0>', '|1>']
    counts = [c0, c1]

    plt.bar(states, counts)
    plt.title("Simulated Measurement Results")
    plt.ylabel("Counts")
    plt.show()