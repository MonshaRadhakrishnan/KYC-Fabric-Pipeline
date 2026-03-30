# KYC-Fabric-Pipeline

# KYC Document Processing Pipeline  
## Microsoft Fabric | PySpark | Delta Lake | OneLake  

Automated KYC document ingestion and validation pipeline built on Microsoft Fabric,  
inspired by RAKBANK's compliance processing use case.  

**Outcome:** Processes scalable KYC document batches (simulated 20+ per run) with automated expiry flagging,  
confidence scoring, and SQL-queryable Delta tables.  

## Architecture  
 <img width="1458" height="644" alt="architecture" src="https://github.com/user-attachments/assets/e25b4f9c-3447-4d18-9279-99d47c69d843" />


## Tech Stack
- Microsoft Fabric (Lakehouse, Data Pipeline, SQL Endpoint, Power BI)
- Azure Document Intelligence (prebuilt-idDocument model)
- PySpark / Delta Lake (Medallion architecture: Bronze / Silver / Gold)
- OneLake (single storage layer, no data duplication)

---

## Pipeline Architecture
<img width="1272" height="452" alt="image" src="https://github.com/user-attachments/assets/23aee48c-f189-4a98-8d58-8167106f7ed8" />


---

## KYC Operations Dashboard
<img width="1200" height="623" alt="image" src="https://github.com/user-attachments/assets/938c04c9-d258-40b0-8de6-5b26a161a0dc" />


---

## What This Project Does

1. Ingests raw KYC JSON documents into the Bronze layer (OneLake)  
2. Calls Azure Document Intelligence API for OCR-based field extraction  
3. Validates and enriches data using PySpark:
   - Expiry status  
   - Confidence flags  
   - AML tags
4. Writes enriched data to Silver Delta tables  
5. Aggregates into Gold layer:
   - Compliance summary  
   - Expiry alerts  
   - Risk Bands  
6. Serves a live Power BI dashboard via Lakehouse SQL Endpoint with auto-refresh  


## Business Outcome

Processes 20+ KYC documents per pipeline run with:
- Automated expiry detection  
- AI-driven confidence scoring  
- AML flag propagation

Significantly reduces manual review effort for compliance teams.
