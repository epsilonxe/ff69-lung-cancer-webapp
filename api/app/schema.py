"""Input-field metadata for the lung-cancer risk form.

`key`   -- the dataset feature name (matches the checkpoint's feature order)
`field` -- the snake_case name used in the JSON request/response
`type`  -- "sex" | "age" | "binary"  (drives the frontend control)
Labels come from the full report, Table 3.1 (tab:features).
"""
from __future__ import annotations

SEX_FIELD = {
    "key": "GENDER",
    "field": "gender",
    "type": "sex",
    "label_th": "เพศ",
    "label_en": "Gender",
    "options": [
        {"value": "M", "label_th": "ชาย", "label_en": "Male"},
        {"value": "F", "label_th": "หญิง", "label_en": "Female"},
    ],
}

AGE_FIELD = {
    "key": "AGE",
    "field": "age",
    "type": "age",
    "label_th": "อายุ",
    "label_en": "Age",
    "min": 1,
    "max": 120,
    "unit_th": "ปี",
}

# (dataset key, snake field, Thai label, English label)
_SYMPTOMS = [
    ("SMOKING", "smoking", "การสูบบุหรี่", "Smoking"),
    ("YELLOW_FINGERS", "yellow_fingers", "นิ้วเหลือง", "Yellow fingers"),
    ("ANXIETY", "anxiety", "ความวิตกกังวล", "Anxiety"),
    ("PEER_PRESSURE", "peer_pressure", "แรงกดดันจากเพื่อน", "Peer pressure"),
    ("CHRONIC DISEASE", "chronic_disease", "โรคเรื้อรัง", "Chronic disease"),
    ("FATIGUE", "fatigue", "ความเหนื่อยล้า", "Fatigue"),
    ("ALLERGY", "allergy", "การแพ้", "Allergy"),
    ("WHEEZING", "wheezing", "หายใจมีเสียง", "Wheezing"),
    ("ALCOHOL CONSUMING", "alcohol_consuming", "การดื่มแอลกอฮอล์", "Alcohol consuming"),
    ("COUGHING", "coughing", "การไอ", "Coughing"),
    ("SHORTNESS OF BREATH", "shortness_of_breath", "หายใจลำบาก", "Shortness of breath"),
    ("SWALLOWING DIFFICULTY", "swallowing_difficulty", "กลืนลำบาก", "Swallowing difficulty"),
    ("CHEST PAIN", "chest_pain", "เจ็บหน้าอก", "Chest pain"),
]

SYMPTOM_FIELDS = [
    {"key": k, "field": f, "type": "binary", "label_th": th, "label_en": en}
    for (k, f, th, en) in _SYMPTOMS
]

FEATURE_SCHEMA = [SEX_FIELD, AGE_FIELD, *SYMPTOM_FIELDS]

# field (snake) -> dataset key
FIELD_TO_KEY = {f["field"]: f["key"] for f in FEATURE_SCHEMA}

RISK_BANDS = [
    {"level": "low", "label_th": "ต่ำ", "max": 0.33},
    {"level": "moderate", "label_th": "ปานกลาง", "max": 0.66},
    {"level": "high", "label_th": "สูง", "max": 1.01},
]


def risk_level(prob: float) -> str:
    for band in RISK_BANDS:
        if prob < band["max"]:
            return band["level"]
    return "high"
