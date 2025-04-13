## Active Directory API & Reporting

1. Clone the repo
2. Copy `config/settings_template.json` to `settings.json`
3. Fill in your AD credentials
4. Run the API:
   ```bash
   pip install -r requirements.txt
   uvicorn api.main:app --reload
   ```
5. Open http://127.0.0.1:8000/docs for Swagger UI

Available Reports
- ```/users:``` All users
- ```/inactive-users:``` Inactive accounts
- ```/groups:``` AD groups and members

Project Structure
```
ad-api-project/
├── config/
│   └── settings_template.json
├── reports/
│   └── *.py  # individual report generators
├── api/
│   ├── ad_connector.py
│   └── main.py
├── templates/
│   └── *.html  # optional for HTML reports
├── README.md
├── requirements.txt
└── run.py
