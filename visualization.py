import matplotlib.pyplot as plt

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

    ax.set_title("Bloch Vector Representation")

    plt.show()

def plot_experiment(c0, c1):

    states = ['|0>', '|1>']
    counts = [c0, c1]

    plt.bar(states, counts)
    plt.title("Simulated Measurement Results")
    plt.ylabel("Counts")
    plt.show()