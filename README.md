# Retail Sales Data Engineering and Business Intelligence Project

## Project Overview

This project demonstrates the implementation of an end-to-end Retail Sales Data Engineering and Business Intelligence solution. The objective is to ingest, clean, transform, validate, and prepare retail transaction data for analytics and reporting. The curated dataset is then used to build interactive Power BI dashboards that provide actionable business insights.

The solution follows a complete data engineering workflow including data ingestion, data quality checks, transformation logic, revenue calculation, PII masking, and dashboard reporting.

## Business Objective

Retail organizations generate large volumes of transaction data from multiple channels. Raw datasets often contain:

* Missing values
* Duplicate records
* Inconsistent product information
* Data quality issues
* Personally Identifiable Information (PII)

The objective of this project is to create a clean and standardized dataset that enables business users to analyze:

* Revenue performance
* Product performance
* Category trends
* Regional sales insights
* Customer behavior


## Dataset Description

The source dataset consists of three worksheets:

### retail_data1

Retail transaction records containing customer, product, and payment information.

### retail_data2

Additional retail transaction records used to extend the transaction dataset.

### product_details

Master product reference table containing:

* product_id
* product_name
* category
* price

---

## Data Engineering Workflow

### Step 1: Data Ingestion

The Excel workbook is loaded into Python using Pandas.

Data Sources:

* retail_data1
* retail_data2
* product_details

---

### Step 2: Data Consolidation

The two transaction datasets are combined into a single transaction table.

```python
retail_df = pd.concat(
    [retail1, retail2],
    ignore_index=True
)
```

### Step 3: Data Validation

Validation checks include:

* Record count validation
* Missing value detection
* Duplicate record detection
* Data type validation

---

### Step 4: Data Cleaning

Cleaning activities performed:

* Null value handling
* Duplicate removal
* Standardization of product information
* Data type conversion

---

### Step 5: Product Master Mapping

Product attributes are standardized using the product master table.

Mapped Fields:

* product_name
* category
* price

---

### Step 6: Revenue Calculation

Revenue is calculated using:

Revenue = Price × Quantity × (1 − Discount / 100)

This field is used throughout the dashboard for business analysis.

---

### Step 7: PII Masking

Sensitive customer information is masked before publishing.

Examples:

Email:

```text
john@gmail.com
```

becomes

```text
j***@gmail.com
```

Phone:

```text
9876543210
```

becomes

```text
******3210
```

---

### Step 8: Export Curated Dataset

The final cleaned dataset is exported as:

```text
clean_retail_sales.csv
```

---

## Final Curated Dataset

The curated dataset contains the following fields:

* transaction_id
* customer_id
* customer_name
* product_id
* product_name
* category
* quantity
* price
* discount
* city
* payment_method
* payment_status
* transaction_date
* revenue
* masked_email
* masked_phone

---

## Power BI Dashboard

The Power BI report is organized into four business-focused pages.

### Page 1 – Executive Summary

KPIs:

* Total Revenue
* Total Orders
* Total Customers
* Average Order Value

Visuals:

* Revenue Trend
* Revenue by Category
* Revenue by City
* Interactive Slicers

---

### Page 2 – Revenue Analysis

Visuals:

* Revenue Trend
* Revenue by Payment Method
* Revenue by City
* Revenue by Payment Status

---

### Page 3 – Product Performance

Visuals:

* Top 10 Products
* Bottom 10 Products
* Quantity Sold by Product
* Product Performance Table

---

### Page 4 – Category Trends & Regional Insights

Visuals:

* Revenue by Category
* Quantity by Category
* Category Revenue by City
* City vs Category Matrix

---

## Key Business Metrics

The following KPIs are implemented in Power BI:

### Total Revenue

```DAX
Total Revenue =
SUM(clean_retail_sales[revenue])
```

### Total Orders

```DAX
Total Orders =
DISTINCTCOUNT(clean_retail_sales[transaction_id])
```

### Total Customers

```DAX
Total Customers =
DISTINCTCOUNT(clean_retail_sales[customer_id])
```

### Average Order Value

```DAX
Average Order Value =
DIVIDE(
    [Total Revenue],
    [Total Orders]
)
```

---

## Technologies Used

| Component               | Technology                |
| ----------------------- | ------------------------- |
| Data Processing         | Python                    |
| Data Analysis           | Pandas                    |
| Development Environment | Jupyter Notebook / Kaggle |
| Data Storage            | CSV                       |
| Dashboarding            | Power BI                  |
| Documentation           | Microsoft Word            |
| Version Control         | GitHub                    |

---

## Project Deliverables

* Data Engineering Pipeline (.ipynb and .py)
* Curated Dataset (clean_retail_sales.csv)
* Power BI Dashboard (.pbix)
* Project Documentation (.docx)
* Architecture Diagram
* Data Flow Diagram
* GitHub Repository

---

## Conclusion

This project successfully demonstrates an end-to-end retail analytics solution that combines data engineering and business intelligence practices. Raw retail transaction data was transformed into a clean, validated, and analytics-ready dataset. The curated data was then used to create interactive Power BI dashboards that provide actionable insights into revenue, product performance, category trends, and regional sales performance.
