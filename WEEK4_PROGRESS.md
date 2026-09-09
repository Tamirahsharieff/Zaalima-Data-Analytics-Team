# Week 4 Progress

## Completed
- Connected Metabase to the PostgreSQL Telco Churn database
- Verified the Customer Churn table in Metabase
- Created the Customer Churn Dashboard
- Added churn visualizations for contract, internet service, payment method, paperless billing, and churn distribution
- Added an interactive Contract filter
- Started dashboard organization for Week 4 visualization and deployment

## API
- FastAPI churn prediction API remains operational
- Single and batch prediction endpoints are available

## Next Steps
- Finish dashboard filters
- Add customer value/LTV segmentation
- Complete Docker containerization
- Finalize technical documentation

## Week 4 Deployment & API Testing

### Docker Deployment
- Containerized the FastAPI churn prediction application using Docker.
- Built the Docker image successfully.
- Started the churn-api container with port 8000:8000.
- Verified the container was running using docker ps.

### API Testing
- Tested the FastAPI /predict endpoint through Swagger UI.
- Dockerized API returned HTTP 200 successfully.
- Example prediction returned:
  - Churn prediction: 0 (No Churn)
  - Churn probability: approximately 28.6%

### Dashboard
- Connected Metabase to the PostgreSQL telco_churn database.
- Created the Customer Churn Dashboard.
- Added churn visualizations by contract, internet service, payment method, paperless billing, tenure, monthly charges, senior citizen status, and other customer segments.
- Added interactive dashboard analysis for customer churn risk.

### Week 4 Status
- Database connection: Complete
- Metabase dashboard: Complete
- FastAPI deployment: Complete
- Docker containerization: Complete
- API testing: Complete
- Technical documentation: Complete

### Final Project Sign-Off
- Project development, deployment, dashboard, API testing, Docker containerization, and documentation completed.