# A/B Test: Conversion Rate Analysis
## Overview
Statistical A/B test analyzing whether a redesigned landing page significantly improves user conversion rates. Built to simulate the kind of booking funnel experiments run by e-commerce and travel companies.
## Key Finding
The new page did not produce a statistically significant improvement in conversions. Recommendation: do not ship the new page.
## Methodology

Two-proportion Z-test using scipy / statsmodels
Cleaned mismatched group/page assignments prior to testing
Removed duplicate user IDs to ensure one observation per user
Sample size: ~290,000 users

## Tools

Python 3.9 (pandas, scipy, statsmodels, numpy)
Tableau Public (dashboard link coming soon)

## Data Source
Ecommerce AB Testing 2022 Dataset via Kaggle