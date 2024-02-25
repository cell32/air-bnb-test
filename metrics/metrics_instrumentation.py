# metrics_instrumentation.py

from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from flask import Flask, Response, jsonify, session
from flask import request
from sqlalchemy import text

app = Flask(__name__)

# /health endpoint
def db_health_check_endpoint(db,app):
    @app.route('/health')
    def health():
        try:
            # Check the database connection by executing a simple query
            db.session.execute(text('SELECT 1'))
            db_status = "Database connection OK"
            status_code = 200

        except Exception as e:
            db_status = f"Database connection error: {str(e)}"
            status_code = 500

        return jsonify({'db_status': db_status, 'status': 'OK' if status_code == 200 else 'Database connection error'}), status_code

def setup_db_health_check(db,app):
    db_health_check_endpoint(db, app)

# /metrics endpoint
def setup_prometheus_metrics_endpoint(app):   
    @app.route('/metrics')
    def metrics():
        metrics_data = generate_latest()

        return Response(metrics_data, mimetype=CONTENT_TYPE_LATEST)

def setup_prometheus_metrics(app):
    setup_prometheus_metrics_endpoint(app)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)