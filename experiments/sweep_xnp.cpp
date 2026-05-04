#include "../src/simulation.h"
#include <string>

int main() {

    for (double xnp : {2.0, 3.0, 4.0, 5.0, 6.0}) {

        Params p;
        p.VM = 3000;
        p.VT = 1000;
        p.XNP = xnp;
        p.XNT = 0.0;
        p.HEDEG = -20.0;

        Trajectory traj = run_simulation(p);

        std::string filename = "output/csv/xnp_" + std::to_string((int)xnp) + ".csv";

        save_to_csv(traj, filename);
    }

    return 0;
}
