// Field metadata for the risk form. Mirrors GET /schema from the API
// (webapp/api/app/schema.py). Kept static so the form renders even if the
// API is briefly unavailable.

export type SymptomField = {
  field: string;
  labelTh: string;
  labelEn: string;
};

export const SYMPTOM_FIELDS: SymptomField[] = [
  { field: "smoking", labelTh: "การสูบบุหรี่", labelEn: "Smoking" },
  { field: "yellow_fingers", labelTh: "นิ้วเหลือง", labelEn: "Yellow fingers" },
  { field: "anxiety", labelTh: "ความวิตกกังวล", labelEn: "Anxiety" },
  { field: "peer_pressure", labelTh: "แรงกดดันจากเพื่อน", labelEn: "Peer pressure" },
  { field: "chronic_disease", labelTh: "โรคเรื้อรัง", labelEn: "Chronic disease" },
  { field: "fatigue", labelTh: "ความเหนื่อยล้า", labelEn: "Fatigue" },
  { field: "allergy", labelTh: "การแพ้", labelEn: "Allergy" },
  { field: "wheezing", labelTh: "หายใจมีเสียง", labelEn: "Wheezing" },
  { field: "alcohol_consuming", labelTh: "การดื่มแอลกอฮอล์", labelEn: "Alcohol consuming" },
  { field: "coughing", labelTh: "การไอ", labelEn: "Coughing" },
  { field: "shortness_of_breath", labelTh: "หายใจลำบาก", labelEn: "Shortness of breath" },
  { field: "swallowing_difficulty", labelTh: "กลืนลำบาก", labelEn: "Swallowing difficulty" },
  { field: "chest_pain", labelTh: "เจ็บหน้าอก", labelEn: "Chest pain" },
];

export const AGE_MIN = 1;
export const AGE_MAX = 120;

export type Gender = "M" | "F";

export type FormState = {
  gender: Gender;
  age: number;
} & Record<string, boolean | Gender | number>;

export const DEFAULT_FORM: FormState = {
  gender: "M",
  age: 60,
  ...Object.fromEntries(SYMPTOM_FIELDS.map((f) => [f.field, false])),
};

export type PredictResponse = {
  label: "YES" | "NO";
  probability: number;
  risk: "low" | "moderate" | "high";
  threshold: number;
};

export const RISK_LABEL_TH: Record<PredictResponse["risk"], string> = {
  low: "ต่ำ",
  moderate: "ปานกลาง",
  high: "สูง",
};

export const API_URL =
  process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";
