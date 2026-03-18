# KYC-Fabric-Pipeline

# KYC Document Processing Pipeline  
## Microsoft Fabric | PySpark | Delta Lake | OneLake  

Automated KYC document ingestion and validation pipeline built on Microsoft Fabric,  
inspired by RAKBANK's compliance processing use case.  

**Outcome:** Processes 20+ KYC documents per run with automated expiry flagging,  
confidence scoring, and SQL-queryable Delta tables.  

## Architecture  
[architecture diagram image here]  

## Tech stack  
- Microsoft Fabric (Lakehouse, Data Pipeline, SQL endpoint)  
- PySpark / Delta Lake  
- OneLake (Bronze / Silver / Gold medallion architecture)  

## What it does  
1. Lands raw JSON documents in Bronze layer  
2. Transforms and enriches with PySpark (expiry status, confidence flags)  
3. Writes to Delta table with full ACID compliance  
4. Exposes SQL endpoint for KYC ops queries  

