import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def animate_trajectory(RM1, RM2, RT1, RT2, skip=50, save_path=None):

    RM1 = RM1[::skip]
    RM2 = RM2[::skip]
    RT1 = RT1[::skip]
    RT2 = RT2[::skip]

    fig, ax = plt.subplots(figsize=(10,6))

    all_x = np.concatenate([RM1, RT1])
    all_y = np.concatenate([RM2, RT2])

    ax.set_xlim(0.975*np.min(all_x), 1.025*np.max(all_x))
    ax.set_ylim(0.975*np.min(all_y), 1.025*np.max(all_y))
    # ax.set_aspect('equal')

    missile_dot, = ax.plot([], [], 'ro', label="Missile")
    target_dot,  = ax.plot([], [], 'bo', label="Target")

    missile_path, = ax.plot([], [], 'r--', alpha=0.5)
    target_path,  = ax.plot([], [], 'b--', alpha=0.5)
    los_line,     = ax.plot([], [], 'g-',  alpha=0.3)

    ax.legend()
    ax.grid()

    def init():
        return missile_dot, target_dot, missile_path, target_path, los_line

    def update(frame):
        missile_dot.set_data([RM1[frame]], [RM2[frame]])
        target_dot.set_data ([RT1[frame]], [RT2[frame]])

        missile_path.set_data(RM1[:frame], RM2[:frame])
        target_path.set_data (RT1[:frame], RT2[:frame])

        los_line.set_data(
            [RM1[frame], RT1[frame]],
            [RM2[frame], RT2[frame]]
        )

        dist = np.hypot(RM1[frame] - RT1[frame],
                        RM2[frame] - RT2[frame])

        ax.set_title("Intercept 💥" if dist < 50 else "Proportional Navigation")

        return missile_dot, target_dot, missile_path, target_path, los_line

    frames = min(len(RM1), len(RT1))

    ani = FuncAnimation(
        fig,
        update,
        frames=frames,
        init_func=init,
        interval=20,
        blit=True
    )

    if save_path:
        ani.save(save_path, writer="pillow")
    else:
        plt.show()

    return ani


if __name__ == "__main__":
    import numpy as np

    data = np.loadtxt("../output/csv/run_default.csv",
                      delimiter=",",
                      skiprows=1)

    RM1, RM2, RT1, RT2 = data[:, :4].T

    animate_trajectory(RM1, RM2, RT1, RT2)