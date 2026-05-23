# Enterprise Playwright Python Framework

## Setup

python -m venv .venv

## Activate venv

Windows:
.venv\Scripts\activate

## Install dependencies

pip install -r requirements.txt

## Install browsers

playwright install

## Run tests

pytest

## Generate Allure Report

allure serve reports/allure-results

## GitHub Actions

Workflow runs daily at 5 AM EST.