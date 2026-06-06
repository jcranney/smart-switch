import numpy as np
import scipy.optimize as opt

# r = R_1 R_2 R_a R_b
R1 = 0
R2 = 1
RA = 2
RB = 3

TARGET_VOO = 4.0
TARGET_VCO = 2.5
TARGET_VOC = 1.0


def voo(r: np.ndarray) -> float:
    return 5 * r[R2] / (r[R1] + r[R2]) - TARGET_VOO


def vco(r: np.ndarray) -> float:
    return (
        5 * r[R2] * r[RA] / (r[R1] * r[R2] + r[R1] * r[RA] + r[R2] * r[RA]) - TARGET_VCO
    )


def voc(r: np.ndarray) -> float:
    return (
        5 * r[R2] * r[RB] / (r[R1] * r[R2] + r[R1] * r[RB] + r[R2] * r[RB]) - TARGET_VOC
    )


def cost(r: np.ndarray) -> np.ndarray:
    return np.r_[voo(r), vco(r), voc(r)]


if __name__ == "__main__":
    x0 = np.r_[1e3, 1e3, 1e3]
    bounds = opt.Bounds([0] * 3, [1e6] * 3)
    res = opt.least_squares(lambda x: cost(np.r_[3.3e3, x]), x0, verbose=2, bounds=bounds)
    print(res)
