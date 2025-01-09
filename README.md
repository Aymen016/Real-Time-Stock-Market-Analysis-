# 📈 Stock Market Kafka Real-Time Data Engineering Project

Welcome to the **Stock Market Kafka Real-Time Data Engineering Project**! In this project, we will build an end-to-end real-time data pipeline using cutting-edge technologies to process and analyze stock market data. 

## 🚀 Project Overview
This project involves processing **real-time stock market data** using **Apache Kafka**, storing it on **AWS S3**, analyzing it using **Athena**, and cataloging it with **Glue**. The pipeline demonstrates the operational side of Data Engineering, focusing on building and managing the data flow.

## 🏗️ Architecture
![Architecture](Architecture.jpg)

The architecture consists of:
1. **Data Ingestion**: Streaming stock market data using Kafka.
2. **Data Storage**: Storing the processed data in AWS S3.
3. **Data Cataloging**: Using AWS Glue to create a catalog for S3 data.
4. **Data Querying**: Leveraging Athena to query data directly from S3.
5. **Processing and Analysis**: Using Python for additional transformations and analysis.

## 🛠️ Technologies Used
We utilize the following technologies for building and managing this data pipeline:

- **Programming Language**: Python 🐍
- **Amazon Web Services (AWS)**:
  - S3 (Simple Storage Service) 🗂️
  - Athena 📊
  - Glue Crawler 🕷️
  - Glue Catalog 📚
  - EC2 🖥️
- **Apache Kafka** 🟧

## 📊 Dataset
We use a stock market dataset that includes processed index data. While you can use any dataset for this project, we focus on building the pipeline.

Dataset Link: [indexProcessed.csv](https://github.com/Aymen016/Real-Time-Stock-Market-Analysis/dataset/indexProcessed.csv)


---

## 🔑 Key Steps in the Project
1. **Set up Apache Kafka**: Stream real-time data.
2. **Use AWS EC2**: Host your Kafka producer and consumer scripts.
3. **Store Data on S3**: Use AWS S3 for reliable data storage.
4. **Create Glue Catalog**: Enable schema-based querying with Glue Crawlers.
5. **Query with Athena**: Run SQL queries directly on S3 data.
6. **Python Analysis**: Use Python to process, clean, and analyze data further.

---

## ✨ Features
- **Real-time data processing**: Process stock market data in real time.
- **Scalable architecture**: Built on AWS and Kafka for high availability.
- **SQL Querying**: Analyze data stored in S3 with SQL via Athena.
- **Automation**: Glue Crawlers automate schema updates.

---

## 📂 Project Structure
```plaintext
📂 Stock-Market-Real-Time-Data-Engineering
├── 📜 producer.py        # Kafka producer script
├── 📜 consumer.py        # Kafka consumer script
├── 📜 analysis.py        # Python data analysis script
├── 📂 data               # Folder for local data files
├── 📜 README.md          # Project documentation
└── 📜 requirements.txt   # Python dependencies
