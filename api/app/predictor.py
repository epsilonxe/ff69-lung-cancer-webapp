"""Loads the ELM weight checkpoint and turns a patient record into a
risk prediction. Pure numpy -- no dependency on the research package.
"""
from __future__ import annotations

import os

import numpy as np

from .schema import risk_level

CHECKPOINT = os.environ.get(
    "MODEL_PATH",
    os.path.join(os.path.dirname(__file__), os.pardir, "model", "elm_lung_cancer.npz"),
)


def _sigmoid(x: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-np.clip(x, -30, 30)))


class Predictor:
    def __init__(self, path: str = CHECKPOINT):
        ckpt = np.load(path, allow_pickle=True)
        self.W = ckpt["W"].astype(float)
        self.b = ckpt["b"].astype(float)
        self.u = ckpt["u"].astype(float)
        self.age_mu = float(ckpt["age_mu"])
        self.age_sd = float(ckpt["age_sd"])
        self.features = [str(f) for f in ckpt["features"]]
        self.threshold = float(ckpt["threshold"])
        self.hidden_nodes = int(ckpt["L"])

    def _vectorize(self, record: dict) -> np.ndarray:
        vals = []
        for key in self.features:
            if key == "GENDER":
                vals.append(1.0 if str(record[key]).strip().upper() == "M" else 0.0)
            elif key == "AGE":
                vals.append((float(record[key]) - self.age_mu) / self.age_sd)
            else:
                vals.append(1.0 if bool(record[key]) else 0.0)
        return np.asarray(vals, float)

    def predict(self, record: dict) -> dict:
        x = self._vectorize(record)
        h = _sigmoid(x @ self.W.T + self.b)
        prob = float(_sigmoid(2.0 * (h @ self.u)))
        return {
            "label": "YES" if prob > self.threshold else "NO",
            "probability": prob,
            "risk": risk_level(prob),
            "threshold": self.threshold,
        }
