#include "simulation.h"

int main() {

    Params p;
    p.VM = 3000;
    p.VT = 1000;
    p.XNP = 4.0;
    p.XNT = 0.0;
    p.HEDEG = -20.0;

    Trajectory traj = run_simulation(p);

    save_to_csv(traj, "../output/csv/run_default.csv");

    return 0;
}
