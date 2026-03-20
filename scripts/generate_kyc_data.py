import json, random, os
from datetime import datetime, timedelta

names = [
    "Ahmed Al Mansoori", "Fatima Al Rashidi", "Mohammed Al Zaabi",
    "Sara Al Hammadi", "Khalid Al Mazrouei", "Maryam Al Nuaimi",
    "Sultan Al Kaabi", "Noura Al Suwaidi", "Saeed Al Ameri",
    "Hessa Al Falasi", "Rashid Al Muhairi", "Aisha Al Marri",
    "Abdullah Al Neyadi", "Maitha Al Khaili", "Juma Al Qubaisi",
    "Shamma Al Dhaheri", "Hamdan Al Ghafri", "Latifa Al Blooshi",
    "Zayed Al Mansouri", "Reem Al Shamsi"
]

doc_types = ['Emirates ID', 'Passport', 'Residence Visa']
sources = ['mobile_app', 'branch_scan', 'web_portal']

os.makedirs('kyc_raw', exist_ok=True)

for i, name in enumerate(names):
    dob = datetime(1970 + i, (i % 12) + 1, (i % 28) + 1)
    issue = datetime(2020 + (i % 4), (i % 12) + 1, 1)
    expiry = issue + timedelta(days=365 * (2 + i % 3))

    record = {
        "customer_id": f"UAE-2024-{i+1:03d}",
        "full_name": name,
        "document_type": doc_types[i % 3],
        "document_number": f"784-{dob.year}-{1000000 + i}-1",
        "date_of_birth": dob.strftime("%Y-%m-%d"),
        "nationality": "AE",
        "issue_date": issue.strftime("%Y-%m-%d"),
        "expiry_date": expiry.strftime("%Y-%m-%d"),
        "address": f"Villa {i+1}, Al Barsha {(i % 3) + 1}, Dubai",
        "employer": ["Emirates NBD", "ADCB", "FAB", "RAKBANK"][i % 4],
        "upload_timestamp": datetime.utcnow().isoformat() + "Z",
        "source_system": sources[i % 3],
        "extraction_confidence": round(0.85 + random.uniform(0, 0.14), 2)
    }

    with open(f"kyc_raw/customer_{i+1:03d}.json", "w") as f:
        json.dump(record, f, indent=2)

print("Generated 20 KYC JSON files in kyc_raw/")