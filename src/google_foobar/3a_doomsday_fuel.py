from fractions import Fraction, gcd
import numpy as np


def find_states(m):
    ts = []
    nts = []

    for i in range(len(m)):
        if sum(m[i]) == 0:
            ts.append(i)
        else:
            nts.append(i)

    return ts, nts


def find_denominator(FR):
    fractions = [Fraction(p).limit_denominator() for p in FR]
    lcm = next(f.denominator for f in fractions if f.denominator != 1)

    for f in fractions:
        if f.denominator != 1:
            lcm = lcm * f.denominator // gcd(lcm, f.denominator)

    return [(f * lcm).numerator for f in fractions] + [lcm]


def solution(m):
    # Find terminal states (ts) and non-terminal states (nts)
    ts, nts = find_states(m)
    if 0 in ts:
        return [1] + [0] * len(ts[1:]) + [1]

    # Convert to matrix
    M = np.matrix(m, dtype=float)[nts, :]

    # Convert to probabilities (divide by sum of row)
    M = M / M.sum(1)

    # Find R, Q matrices
    #   R: probability of nts -> ts
    #   Q: probability of nts -> nts
    R, Q = M[:, ts], M[:, nts]

    # Calculate F=(I-Q)^-1
    #   F: fundamental matrix
    #   I: identity matrix of Q
    #   Q: probability of nts -> nts
    I = np.identity(len(Q))
    F = (I - Q) ** -1

    # Calculate F*R (dot product)
    #   F: fundamental matrix
    #   R: probability of nts -> ts
    FR = F * R

    # Find denominator
    return find_denominator(FR[0].A1)


print "([[0,0,0,0,0]]): expected=[1, 1] actual={}".format(
    solution(
        [
            [0, 0, 0, 0, 0],
        ]
    )
)
# pylint: disable=line-too-long
print "([[0,2,1,0,0],[0,0,0,3,4],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]): expected=[7, 6, 8, 21] actual={}".format(
    solution(
        [
            [0, 2, 1, 0, 0],
            [0, 0, 0, 3, 4],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    )
)
# pylint: disable=line-too-long
print "([[0,1,0,0,0,1],[4,0,0,3,2,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]): expected=[0, 3, 2, 9, 14] actual={}".format(
    solution(
        [
            [0, 1, 0, 0, 0, 1],
            [4, 0, 0, 3, 2, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
    )
)
