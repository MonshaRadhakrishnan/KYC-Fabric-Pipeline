# KYC-Fabric-Pipeline

# KYC Document Processing Pipeline  
## Microsoft Fabric | PySpark | Delta Lake | OneLake  

Automated KYC document ingestion and validation pipeline built on Microsoft Fabric,  
inspired by RAKBANK's compliance processing use case.  

**Outcome:** Processes scalable KYC document batches (simulated 20+ per run) with automated expiry flagging,  
confidence scoring, and SQL-queryable Delta tables.  

## Architecture  
 <img width="1458" height="644" alt="architecture" src="https://github.com/user-attachments/assets/e25b4f9c-3447-4d18-9279-99d47c69d843" />


## Tech stack  
- Microsoft Fabric (Lakehouse, Data Pipeline, SQL endpoint)  
- PySpark / Delta Lake  
- OneLake (Bronze / Silver / Gold medallion architecture)  

## What it does  
1. Lands raw JSON documents in Bronze layer  
2. Transforms and enriches with PySpark (expiry status, confidence flags)  
3. Writes to Delta table with full ACID compliance  
4. Exposes SQL endpoint for KYC ops queries  

