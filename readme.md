# Flask App with Continuous Deployment to Google App Engine

This repository contains a simple Flask web application with continuous deployment to Google App Engine using GitHub Actions. 
The project demonstrates how to create a Flask app and deploy to App Engine automatically when changes are pushed to the `main` branch.

## Project Structure

- `main.py`: Main Flask application file (doesn't do much).
- `requirements.txt`: List of Python dependencies.
- `templates/index.html` - Jinja html to show the table
- `.github/workflows/appengine.yml`: GitHub Actions workflow for continuous deployment.

## Notes

The GCP SA has to have the following authorisations to work correctly:
- App Engine Deployer
- App Engine Service Admin
- Cloud Build Service Account
- Service Account User
- Storage Object User
