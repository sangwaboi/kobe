import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 3.5))
ax.set_xlim(0, 100)
ax.set_ylim(0, 50)
ax.set_aspect('equal', adjustable='box')
ax.set_title("Ball in a 100x50 Arena (No Path Trace)")
ax.set_xlabel("X")
ax.set_ylabel("Y")

# Parameters
radius = 2.0
dt = 0.1     # Time step
speed = 7.0  # Speed 
random_factor = 0.5  # Factor for random motion

# Initial position and velocity
pos = np.array([20.0, 40.0])        # Starting in the upper-left region
vel = np.array([speed, -speed/2])   # Example initial velocity vector

# Create a Circle patch for the ball
ball = plt.Circle(pos, radius=radius, fc='blue')
ax.add_patch(ball)

# Draw a rectangle to visualize the boundary
rect = plt.Rectangle((0,0), 100, 50, fill=False, ec='black', lw=2)
ax.add_patch(rect)

def update(frame):
    global pos, vel

    # Introduce random variations in velocity for more randomness
    vel += random_factor * (np.random.rand(2) - 0.5)

    # Move the ball
    pos += vel * dt

    # Check collision with left/right boundaries
    if pos[0] - radius < 0:
        pos[0] = radius
        vel[0] = -vel[0]
    elif pos[0] + radius > 100:
        pos[0] = 100 - radius
        vel[0] = -vel[0]

    # Check collision with bottom/top boundaries
    if pos[1] - radius < 0:
        pos[1] = radius
        vel[1] = -vel[1]
    elif pos[1] + radius > 50:
        pos[1] = 50 - radius
        vel[1] = -vel[1]

    # Update the circle patch center
    ball.center = (pos[0], pos[1])

    return (ball,)

anim = FuncAnimation(
    fig, update, frames=300, interval=20, blit=True
)

plt.show()
