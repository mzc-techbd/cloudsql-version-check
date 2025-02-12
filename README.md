# cloudsql-version-check
org 내 Cloud SQL Instance 중 개발자 커뮤니티에서 지원 종료(EOL)된 Cloud SQL for MySQL 및 PostgreSQL의 버전 체크

Google Docs : https://cloud.google.com/sql/docs/mysql/extended-support

##
### Git Clone
```bash
Git Clone https://github.com/mzc-techbd/cloudsql-version-check.git
```

### Install the client library
```bash
pip install --upgrade google-cloud-asset
```

### execution
```bash
python main.py
```

## 코드 설명
- Google Cloud Asset Inventory API를 사용하여 sqladmin.googleapis.com 활성화 되어있는 프로젝트 추출
- REST API 사용하여 추출된 프로젝트 내 인스턴스 조회
  - docs: https://cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/list
