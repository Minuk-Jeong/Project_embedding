import argparse
import os
import tempfile
import time

import tensorflow as tf
from sionna.channel import RayleighBlockFading


def main():
    parser = argparse.ArgumentParser(description="Shared 4x4 Rayleigh H source for OAI rfsim")
    parser.add_argument("--out", default="/tmp/oai_sionna_h44.txt", help="shared snapshot file path")
    parser.add_argument("--update-us", type=int, default=1000000, help="update period in microseconds")
    parser.add_argument("--seed", type=int, default=None, help="optional RNG seed")
    args = parser.parse_args()

    if args.seed is not None:
        tf.random.set_seed(args.seed)

    tf.config.run_functions_eagerly(True)
    tf.config.threading.set_intra_op_parallelism_threads(1)
    tf.config.threading.set_inter_op_parallelism_threads(1)
    tf.config.set_visible_devices([], "GPU")

    chan = RayleighBlockFading(num_rx=1, num_rx_ant=4, num_tx=1, num_tx_ant=4)
    update_s = max(args.update_us, 1000) / 1e6

    seq = 0
    out_dir = os.path.dirname(os.path.abspath(args.out)) or "."
    os.makedirs(out_dir, exist_ok=True)
    print(f"[shared-rayleigh-4x4] writing snapshots to {args.out}, period={update_s:.6f}s")

    while True:
        h, _ = chan(batch_size=1, num_time_steps=1)
        vals = []
        for r in range(4):
            for t in range(4):
                hij = h[0, 0, r, 0, t, 0, 0]
                vals.append(float(tf.math.real(hij).numpy()))
                vals.append(float(tf.math.imag(hij).numpy()))

        fd, tmp_path = tempfile.mkstemp(prefix="oai_sionna_h44_", suffix=".tmp", dir=out_dir)
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                f.write(f"{seq} 4 4 ")
                f.write(" ".join(f"{v:.10f}" for v in vals))
                f.write("\n")
                f.flush()
                os.fsync(f.fileno())
            os.replace(tmp_path, args.out)
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)

        if seq % 10 == 0:
            print(f"[shared-rayleigh-4x4] seq={seq} h00={vals[0]:.6f}+j{vals[1]:.6f}")
        seq += 1
        time.sleep(update_s)


if __name__ == "__main__":
    main()

